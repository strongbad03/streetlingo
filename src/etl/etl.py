import cld3
import fiona
import geopandas as gpd
from iso639 import languages
import numpy as np
import os
import pandas as pd
import requests
import string
from time import perf_counter
import zipfile


def fetch_data(url):
    r = requests.get(url, stream=True)
    r.raise_for_status()

    print('Downloading data from U.S. Census website')
    with open('us_roads.gdb.zip', 'wb') as handle:
        for block in r.iter_content(1024):
            handle.write(block)


def lid_text(text):
    two_letter = cld3.get_language(text)[0]
    # three_letter = languages.get(alpha2=two_letter).part3
    # name = languages.get(alpha2=two_letter).name
    return two_letter


def load_data(file):
    print('Loading data from geodatabase')
    df = gpd.read_file(file, driver='FileGDB', layer='Roads')
    return df


def lid_data(df, column):
    df = df.apply(lambda x: lid_text(x))
    print(df.head())


def test_lid_speed(num_words, len_words):
    """How long does a LID take on average?"""
    # make a random series of n-grams to LID
    random_ngrams = []
    timings = []
    alpha = list(string.ascii_lowercase)
    i = 0
    while i < num_words:
        j = 0
        word = ''
        while j < len_words:
            word += np.random.choice(alpha)
            print(word)
            j+=1
        random_ngrams.append(word)
        i+=1

    # LID grams and average timing
    for quad in random_ngrams:
        start = perf_counter()
        lid_text(quad)
        stop = perf_counter()
        duration = stop - start
        timings.append(duration)
    print(f'''Per-LID timing for {num_words} words with {len_words} characters \
averages to ~{np.average(timings): 0.6f} seconds.''')
    print(f'''Total time taken is {np.sum(timings)}.''')
    return random_ngrams


def unzip_data(archive):
    print('Unzipping data file')
    if os.path.exists('./data'):
        pass
    else:
        os.mkdir('data')
    with zipfile.ZipFile(archive, 'r') as zip_ref:
        zip_ref.extractall(path='data')
