import os
import pandas as pd


# undefined を数える

# dirname = os.path.join("data", "genre_2017_filled", "20201003-012640")
dirname = os.path.join("data", "genre_2017_filled", "2020_base")
os.makedirs(dirname, exist_ok=True)

d_2020 = pd.read_csv("data/20201003-012640/vgsales_1.csv")
# d_2020 = pd.read_csv("./vgsales_2020_base.csv")
d_2017 = pd.read_csv("./vgsales_2017.csv")

print("2020のジャンル不明データ数: " + str(((d_2020["Genre"] == "undefined") & (d_2020["Platform"] != "Series")).sum()))
# 関数を作成する
# 一つの2020に対して突き合わせを行う
new_genres = []
for i_2020, row_2020 in d_2020.iterrows():
    # デバッグ用中断
    # if i_2020 >= 10:
    #     new_genres.append("undefined")
    #     continue
    found = False
    for i_2017, row_2017 in d_2017.iterrows():
        if row_2020["Name"] == row_2017["Name"]:
            print(str(row_2020["Rank"]), row_2020["Name"], row_2017["Genre"])
            new_genres.append(row_2017["Genre"])
            # row_2020["Genre"] = row_2017["Genre"]
            found = True
            break
    if not found:
        print(str(row_2020["Rank"]) + " : " + row_2020["Name"] + " s genre was undefined...")
        new_genres.append("undefined")

    # if name not found in 2017, genre 2020 is undefined

d_2020["New_Genre"] = new_genres
newfilename = os.path.join(dirname, "vgsales_1.csv")
d_2020.to_csv(newfilename, sep=",", encoding='utf-8', index=False)

print("2020のジャンル不明データ数: " + str(((d_2020["New_Genre"] == "undefined") & (d_2020["Platform"] != "Series")).sum()))

def create_single_2017_genred_csv(d_2020, d_2017):
    new_genres = []
    for i_2020, row_2020 in d_2020.iterrows():
        # 中断
        # if i_2020 >= 10:
        #     new_genres.append("undefined")
        #     continue
        found = False
        for i_2017, row_2017 in d_2017.iterrows():
            if row_2020["Name"] == row_2017["Name"]:
                print(str(row_2020["Rank"]), row_2020["Name"], row_2017["Genre"])
                new_genres.append(row_2017["Genre"])
                # row_2020["Genre"] = row_2017["Genre"]
                found = True
                break
        if not found:
            print(str(row_2020["Rank"]) + " : " + row_2020["Name"] + " s genre was undefined...")
            new_genres.append("undefined")

        # if name not found in 2017, genre 2020 is undefined

    d_2020["Genre"] = new_genres
    newfilename = os.path.join(dirname, "vgsales_1.csv")
    d_2020.to_csv(newfilename, sep=",", encoding='utf-8', index=False)

# TODO: 関数を1-19でループする
# TODO: しなくていいかも

# TODO: 2020でundefinedの数を数える
