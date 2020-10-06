# count ungenred
import os
import pandas as pd
import datetime
from time import sleep

nexttime = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=9)))

def calc_end_time(df):
    count = ((df["Genre_2020"] == "undefined") & (df["Platform"] != "Series")).sum()
    print("2017シリーズデータじゃないジャンルの不明レコード数: " + str(count) )
    # end_time =  nexttime + datetime.timedelta(minutes=int(count))
    # sleep(1)
    # print("取得終了予定時刻: ",end_time.strftime("%Y/%m/%d %H:%M:%S.%f") )

pages = 18 + 1
for i in range(1, pages):
    print(i, "ページ目:")
    df = pd.read_csv(os.path.join("../data", "genre_2020_filled","20201003-012640", "vgsales_" + str(i) + ".csv"))
    calc_end_time(df)


# TODO: 調べる:
# 12 ページ目:
# 2017シリーズデータじゃないジャンルの不明レコード数: 2
# 13 ページ目:
# 2017シリーズデータじゃないジャンルの不明レコード数: 11