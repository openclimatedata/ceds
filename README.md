Data from the
anthropogenic emissions of reactive gases and aerosols in the
[Community Emissions Data System (CEDS)](http://www.globalchange.umd.edu/ceds/)
reformatted into long CSV files with country/sector resolution,

For the repository of the CEDS project see <https://github.com/JGCRI/CEDS/>.

Maintainer of this repository is Robert Gieseke (<rob.g@web.de>).

## Data
This repositoty makes the annual data of the by country and by sector CSV files from the [Data Supplement](https://www.geosci-model-dev.net/11/369/2018/gmd-11-369-2018-assets.html) of Hoesly et al. and the later update on Zenodo (http://doi.org/10.5281/zenodo.4025316) available in a single long CSV formatted file per emissions species.

Changes compared to the original data:
  - country codes are upper-cased
  - country code `XKX` for Kosovo instead of `srb (kosovo)`
  - country code 'BUNKERS' instead of `global`
  - fields with value 0 are not contained in the long format file
  - in the category file <./data/sectors.yaml>, based on table 1 in Hoesly et
    al. (2018) extra hyphens (e.g. 2-D_Other) have been removed

## Processing

Processing requires Python3 and Make.

Run

```
make
```

to download and process the original files, which are downloaded to `cache`.

## License

[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode)

## References

Hoesly, R. M., Smith, S. J., Feng, L., Klimont, Z., Janssens-Maenhout, G., Pitkanen, T., Seibert, J. J., Vu, L., Andres, R. J., Bolt, R. M., Bond, T. C., Dawidowski, L., Kholod, N., Kurokawa, J.-I., Li, M., Liu, L., Lu, Z., Moura, M. C. P., O'Rourke, P. R., and Zhang, Q.: Historical (1750–2014) anthropogenic emissions of reactive gases and aerosols from the Community Emissions Data System (CEDS), Geosci. Model Dev., 11, 369-408, https://doi.org/10.5194/gmd-11-369-2018, 2018.

O'Rourke, Patrick R, Smith, Steven J, McDuffie, Erin E, Klimont, Zbigniew, Crippa, Monica, Mott, Andrea, … Hoesly, Rachel M. (2020). CEDS v_2020_09_11 Pre-Release Emission Data (Version v_2020_09_11) [Data set]. Zenodo. http://doi.org/10.5281/zenodo.4025316
