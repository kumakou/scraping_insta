# scraping_insta

最初にgit clone してください
## 1.使用するパッケージのインストール
pip などで [selenium](https://selenium-python.readthedocs.io/) と [pandas](https://pandas.pydata.org/) のインストールをしてください。
```
pip install pandas
pip install selenium
```

## 2.chrome driverのインストール
[ChromeDriver](https://chromedriver.chromium.org/downloads)から自分が使っているchromeのバージョンに一番近いdriverをインストールしてdriverフォルダーに入れてください

[chromeのバージョンの確認の仕方](https://www.google.com/intl/ja/chrome/update/)

## 3.インスタのユーザー名とパスワードの設定
insta.pyの中にある
```
LOGIN_ID = "ユーザー名"
PASSWORD = "パスワード"
```
を使用するInstagramのユーザー名とパスワードに変えてください


## 4.取得したい投稿数の設定
insta.pyの中にある
```
MIN_COUNT = 10
```
の数字を変更してください

例では1つのハッシュタグあたり10件の投稿を取得します

## 5.ハッシュタグの追加
```
keywords=["cheesecheesecafe","bardelcloe","六花亭","benbencafe","カフェ美鈴","vmgcafe","wavesnow","jbハウス","吉和寿珈琲"]
```
に投稿を取得したいハッシュタグを追加してください

## 6.outputフォルダーの作成
`mkdir output`などでoutputフォルダーを作成してください

作成しないとcsvファイルが出力されません
