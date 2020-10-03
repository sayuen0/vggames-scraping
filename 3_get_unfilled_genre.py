import pandas as pd
import os
import requests
from bs4 import BeautifulSoup, element
from time import sleep

# TODO: ジャンルがundefinedなデータについてジャンルを個別取得する
# TODO: Seriesデータはどうせ省くので飛ばして良い
# TODO: 埋める

def _sleep(n):
    print("過剰リクエスト防止のための" + str(n) + "秒sleep")
    for i in range(n, 0, -1):
        print(i)
        sleep(1)

pages = 18 + 1

time = "20201003-012640"
new_dirname = os.path.join("data", "genre_2020_filled", time)
os.makedirs(new_dirname, exist_ok=True)

dirname = os.path.join("data", "genre_2017_filled", time)
for page in range(1, pages):
    old_filename = os.path.join(dirname, "vgsales_" + str(page) + ".csv")
    d_2020 = pd.read_csv(old_filename)
    genre_2020 = []

    for i_2020, row_2020 in d_2020.iterrows():
        # Seriesデータとundefinedじゃないデータは見る必要なし
        if row_2020["Platform"] == "Series" or row_2020["New_Genre"] != "undefined":
            print(f"{row_2020['Rank']} : {row_2020['Name']} :{row_2020['New_Genre']}")
            genre_2020.append(row_2020["New_Genre"])
            continue

        # find genre
        url = row_2020["URL"]
        r = requests.get(url).text
        _sleep(60)
        soup = BeautifulSoup(r, "html.parser")
        print(f"{row_2020['Rank']}: {row_2020['Name']}")
        if soup.find("div", {"id": "gameGenInfoBox"}) == None:
            print("sub_soupにgameGenInfoBoxを見つけられなかったのでジャンル不明")
            genre_2020.append("undefined")
            continue
        # else
        h2s = soup.find("div", {"id": "gameGenInfoBox"}).find_all('h2')
        # make a temporary tag here to search for the one that contains
        # the word "Genre"
        temp_tag = element.Tag
        for h2 in h2s:
            if h2.string == 'Genre':
                temp_tag = h2
        genre_2020.append(temp_tag.next_sibling.string)


    d_2020["Genre_2020"] = genre_2020
    new_filename = os.path.join(new_dirname, "vgsales_" + str(page) + ".csv")
    d_2020.to_csv(new_filename, sep="," , encoding='utf-8', index=False)

