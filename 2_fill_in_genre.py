from bs4 import BeautifulSoup, element
import urllib
import pandas as pd
import numpy as np
import requests
import re
from time import sleep
from datetime import datetime


# undefined を数える
def print_undefined_genre_count(df):
    print((df["Genre"] == "undefined").sum())

d_2020 = pd.read_csv("./data/vgsales_20201001-035031.csv")
d_2017 = pd.read_csv("./vgsales_2017.csv")


# 関数を作成する
# 一つの2020に対して突き合わせを行う
for i_2020, row_2020 in d_2020.iterrows():
    for i_2017, row_2017 in d_2017.iterrows():
        print(row_2020["Rank", "Name", "Genre"])
        print(row_2017["Rank", "Name", "Genre"])
        print(row_2020["Name"] == row_2017["Name"])


# 関数を1-19でループする

# TODO: 付き合わせてジャンルを埋める
# TODO: 上書きする
# TODO: 2020でundefinedの数を数える