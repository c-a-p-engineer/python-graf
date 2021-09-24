import requests
import json
import pandas as pd
import bar_chart_race as bcr
import japanize_matplotlib

# コロナの感染者を取得
r = requests.get('https://opendata.corona.go.jp/api/Covid19JapanAll')
with open('covid19_daily.json', 'w') as f:
    f.write(r.text)

# JSONを読み込む
data = json.load(open('covid19_daily.json'))

# JSONをデータフレームにする
df = pd.DataFrame(data["itemList"])

# 整形
# 10行ごとにデータ変換
df = df.pivot_table(
    index='date',
    columns='name_jp',
    values='npatients').dropna()[::10]

# アニメーションをmp4で保存する
bcr.bar_chart_race(
    df=df,
    filename='covid19_daily.mp4',
    title='COVID-19 都道府県別感染者数',
    orientation='h',
    sort='desc',
    n_bars=10,
)
