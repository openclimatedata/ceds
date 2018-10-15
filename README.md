[Data Package](http://frictionlessdata.io/specs/data-package/) of the
anthropogenic emissions of reactive gases and aerosols in the
[Community Emissions Data System (CEDS)](http://www.globalchange.umd.edu/ceds/)

## Data
This makes the annual data of the by country and by sector CSV files from the [Data Supplement](https://www.geosci-model-dev.net/11/369/2018/gmd-11-369-2018-assets.html) of Hoesly et al. available in a single long file format.

Changes compared to the original data:
  - country code `XKX` for Kosovo instead of `srb (kosovo)`
  - country code 'BUNKERS' instead of `global`
  - fields with value 0 are not contained in the long format file

## Preparation

Run

```
make
```

to download and process the original files, which are downloaded to `cache`.


## Reference

Hoesly, R. M., Smith, S. J., Feng, L., Klimont, Z., Janssens-Maenhout, G., Pitkanen, T., Seibert, J. J., Vu, L., Andres, R. J., Bolt, R. M., Bond, T. C., Dawidowski, L., Kholod, N., Kurokawa, J.-I., Li, M., Liu, L., Lu, Z., Moura, M. C. P., O'Rourke, P. R., and Zhang, Q.: Historical (1750–2014) anthropogenic emissions of reactive gases and aerosols from the Community Emissions Data System (CEDS), Geosci. Model Dev., 11, 369-408, https://doi.org/10.5194/gmd-11-369-2018, 2018.
