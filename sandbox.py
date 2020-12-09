import pandas as pd
import dask as dd
import dask.array as da
import geopandas as gpd

df = gpd.read_file('./data/tlgdb_2019_a_us_roads.gdb', driver='FileGDB', layer='Roads')