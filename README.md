# 株価通知ツール

## 概要
このプロジェクトは、指定した株価がしきい値を超えた場合に通知を行うツールです。  
Yahoo Finance のデータ（[yfinance](https://pypi.org/project/yfinance/)）を利用し、定期的に株価をチェックします。

## フォルダ構成
以下のようなフォルダ構成になっています。

project(root) /
 ├─ project /
 │   ├─ __init__.py    # パッケージ初期化ファイル
 │   ├─ __main__.py    # エントリーポイント。python -m project で実行可能
 │   ├─ cli.py         # コマンドライン引数の処理と起動処理
 │   ├─ lib /          # ビジネスロジックをまとめたサブパッケージ
 │      ├─ __init__.py # サブパッケージ初期化ファイル
 │      ├─ lib.py      # 株価取得、通知、定期実行の関数を実装

## 必要環境
- Python 3.x
- Pythonライブラリ:
  - [yfinance](https://pypi.org/project/yfinance/)
  - [schedule](https://pypi.org/project/schedule/)

## 特徴
- **株価取得**  
  `project/lib/lib.py` 内で、yfinance を利用して指定ティッカーの株価を取得します。
　具体的には`lib.py` の `get_stock_price` 関数により、指定されたティッカーの最新株価を取得します。

- **定期実行**  
  [schedule](https://pypi.org/project/schedule/) ライブラリを使用し、定期的に株価チェックを実行します。

- **通知機能**  
  株価が設定したしきい値を超えた場合、`project/lib/lib.py` の関数によりコンソールへ通知を行います。

- **コマンドライン操作**  
  `project/cli.py` でコマンドライン引数を受け取り、監視対象ティッカー、しきい値、チェック間隔を指定できます。

　**＜コンソール上での実行例＞※複数銘柄で実行**
    python -m project --tickers AAPL,GOOGL,AMZN --thresholds AAPL:100.0,GOOGL:100.0,AMZN:100.0 --interval 0.1
    
　**＜実行結果＞**
    AAPLの現在の株価: 244.60000610351562
    【通知】AAPLの株価がしきい値を超えました！ 現在の株価: 244.60000610351562
    GOOGLの現在の株価: 185.22999572753906
    【通知】GOOGLの株価がしきい値を超えました！ 現在の株価: 185.22999572753906
    AMZNの現在の株価: 228.67999267578125
    【通知】AMZNの株価がしきい値を超えました！ 現在の株価: 228.67999267578125
    監視ツールを終了します。