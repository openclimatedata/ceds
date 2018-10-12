import pandas as pd
import json

from pathlib import Path
from pandas.testing import assert_series_equal


root = Path(__file__).parents[1]

datapath = root / "cache/Supplemental_Data_Correction/Data Supplement"

files = datapath.glob("*sector_country*.csv")

metadata = json.load(open(root / "datapackage.json", "r"))

units = {i["name"]: i["schema"]["fields"][-1]["unit"]
        for i in metadata["resources"] if "schema" in i}

def read_ceds_csv(path):
    """Read a CEDS by country CSV file and return the global sum."""
    df = pd.read_csv(path)
    assert len(df.units.unique()) == 1
    df = df.drop(["em", "units"], axis=1)
    df = df.set_index("country")
    df.columns = [int(i[1:]) for i in df.columns]
    df = df.T
    df.index.name = "year"
    df = df.sum(axis=1)
    return df

def update_code(code):
    if code == "srb (kosovo)":
        return "XKX"
    elif code == "global":
        return "BUNKERS"
    else:
        return code.upper()


for f in files:
    df = pd.read_csv(f)
    control_sum = read_ceds_csv(str(f).replace("_sector", ""))
    assert len(df.units.unique()) == 1
    assert len(df.em.unique()) == 1
    unit = df.iloc[0].units

    df = df.drop(["em", "units"], axis=1)
    df = df.set_index(["country", "sector"])
    df.columns = [int(i[1:]) for i in df.columns]
    df = df.loc[~(df==0).all(axis=1)]
    species, _, _  = f.name.partition("_")

    df = df.reset_index()

    df = df.melt(
        id_vars=["country", "sector"], var_name="year")
    df = df.set_index(["country", "sector", "year"])
    df = df.loc[~(df==0).all(axis=1)]

    filename = root / "data" / str(species.lower() + ".csv")
    print(filename, unit)
    # Check that unit in metadata is same as in file.
    assert units[species.lower()] == unit

    # Comparison check with data from country file.
    annual_sum = df.groupby("year").sum()["value"]
    assert_series_equal(control_sum, annual_sum, check_names=False)

    df = df.sort_values(["country", "sector", "year"])
    df = df.reset_index().rename(columns={
        "country": "Code",
        "sector": "Sector",
        "year": "Year",
        "value": "Value"
    })

    df.Code = df.Code.apply(update_code)
    df.to_csv(filename, index=False)
