## ダウンロード

中央右上緑色の `Code > Download ZIP`


## 内容物

- `https://github.com/sayuen0/vggames-scraping/blob/master/vgsales_2017.csv`
    - 2017年の原本です。紹介されたやつと同じファイル
- `https://github.com/sayuen0/vggames-scraping/blob/master/vgsales.csv`
    - 今回はじめにサイトから取ったデータです。ジャンルなし、月日あり
-     

## 説明

- `1_get_2020_data.py`を実行すると`data/[取得開始時刻]/vgsales_[ページ番号].csv`という名前で1000件ずつ取得します。一覧取得なので時間は20分かかりません
- `2_`
- 説明の通りある程度のジャンルデータだけは60秒感覚でしか取得できません
    - 全体の30 ~ 40%くらいが該当します
- 最初の1ページ1000件だけ正常取得できることを確認したので、残りの2~18ページについても元データから

## やり方

- フォルダ構成とファイル構成を全く変えずに、`3_get_unfilled_genre.py`を実行してください。1分60件ペースですがデータが取得されます
- 3の開始ページを2ページ目からに設定してあるので、もし最初から取得し直すようなことになったら、そこを1にいじってください

