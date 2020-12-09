from src.etl.etl import *


archive = 'tlgdb_2019_a_us_roads.gdb.zip'
file = 'tlgdb_2019_a_us_roads.gdb.zip'
url = 'https://www2.census.gov/geo/tiger/TGRGDB19/tlgdb_2019_a_us_roads.gdb.zip'
test_text = "影響包含對氣候的變化以及自然資源的枯竭程度"
words = test_lid_speed(2, 2)
df = pd.DataFrame({'word':words})


if __name__ == "__main__":
    # fetch_data(url) # download streets geodatabase
    # unzip_data(archive)
    # df = load_data(file)
    # print(lid_text(test_text))
    # print(lid_text(test_text))
    # test_lid_speed(1000, 10)
    lid_df = lid_data(df, 'word')
    print(lid_df.head)