from src.etl.etl import *
import fiona

archive = 'us_roads.gdb'
url = 'https://www2.census.gov/geo/tiger/TGRGDB19/tlgdb_2019_a_us_roads.gdb.zip'
test_text = "影響包含對氣候的變化以及自然資源的枯竭程度"


if __name__ == "__main__":
    # fetch_data(url) # download streets geodatabase
    # file = unzip_data(archive)
    # layers = fiona.listlayers(archive)
    # load_data(file)
    print(lid_text(test_text))
