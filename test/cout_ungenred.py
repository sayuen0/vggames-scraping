# count ungenred
import os
import pandas as pd


dirname = os.path.join("../data", "genre_2017_filled", "20201003-012640")
newfilename = os.path.join(dirname, "vgsales_1.csv")

d_2020 = pd.read_csv(newfilename)

print("2020のジャンル不明データ数: " + str(((d_2020["New_Genre"] == "undefined") & (d_2020["Platform"] != "Series")).sum()))
