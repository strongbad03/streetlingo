from src.etl.etl import *
import dask_geopandas
import dask.array as da


archive = 'tlgdb_2019_a_us_roads.gdb.zip'
file = 'tlgdb_2019_a_us_roads.gdb.zip'
url = 'https://www2.census.gov/geo/tiger/TGRGDB19/tlgdb_2019_a_us_roads.gdb.zip'
test_text = "影響包含對氣候的變化以及自然資源的枯竭程度"


if __name__ == "__main__":
    # fetch_data(url) # download streets geodatabase
    # unzip_data(archive)
    # df = load_data(file)
    # print(lid_text(test_text))
    # ddf = dask_geopandas.from_geopandas(df, npartitions=4)
    print(lid_text(test_text))
