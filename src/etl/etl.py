import cld3
import fiona
import geopandas as gpd
from iso639 import languages
import os
import requests
import zipfile


def fetch_data(url):
    r = requests.get(url, stream=True)
    r.raise_for_status()

    print('Downloading data from U.S. Census website')
    with open('us_roads.gdb.zip', 'wb') as handle:
        for block in r.iter_content(1024):
            handle.write(block)


def lid_text(text):
    print('LID')
    two_letter = cld3.get_language(text)[0]
    three_letter = languages.get(alpha2=two_letter).part3
    name = languages.get(alpha2=two_letter).name
    return two_letter, three_letter, name


def load_data(file):
    print('Loading data from geodatabase')
    df = gpd.read_file(file, driver='FileGDB', layer='Roads')
    return df

def unzip_data(archive):
    print('Unzipping data file')
    if os.path.exists('./data'):
        pass
    else:
        os.mkdir('data')
    with zipfile.ZipFile(archive, 'r') as zip_ref:
        zip_ref.extractall(path='data')
