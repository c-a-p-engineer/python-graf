import requests
import pandas as pd
import bar_chart_race as bcr
 
# CSVデータをダウンロードする
r = requests.get('https://covid.ourworldindata.org/data/ecdc/total_cases.csv')
with open('covid19.csv', 'w') as f:
    f.write(r.text)
 
# DataFrameにする
raw_df = pd.read_csv('covid19.csv', index_col='date', parse_dates=['date'])
 
# 主要な国を抽出、10行置きのDataFrameを抽出
df = raw_df.loc[:, ["Brazil",
                    "China",
                    "France",
                    "India",
                    "Iran",
                    "Italy",
                    "Japan",
                    "Spain",
                    "United Kingdom",
                    "United States"]
                ].dropna()[::3]
 
# アニメーションをmp4で保存する
bcr.bar_chart_race(
    df=df,
    filename='covid19.mp4',
    orientation='h',
    sort='desc',
    n_bars=6,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=10,
    interpolate_period=False,
    label_bars=True,
    bar_size=.95,
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    period_fmt='%B %d, %Y',
    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                      's': f'Total confirmed cases: {v.nlargest(6).sum():,.0f}',
                                      'ha': 'right', 'size': 8},
    period_length=500,
    figsize=(5, 3),
    dpi=144,
    cmap='dark12',
    title='COVID-19 Total confirmed cases by Country',
    title_size='',
    bar_label_size=7,
    tick_label_size=7,
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=False)