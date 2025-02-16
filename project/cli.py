import argparse
from project.lib import lib

# def main():
#     # コマンドライン引数の設定
#     parser = argparse.ArgumentParser(description="株価通知ツール")
#     parser.add_argument("--ticker", type=str, default="AAPL", help="監視する株のティッカー")
#     parser.add_argument("--threshold", type=float, default=150.0, help="通知のしきい値")
#     parser.add_argument("--interval", type=float, default=10, help="チェック間隔（分）")
#     args = parser.parse_args()
#
#     print("株価通知ツールを起動します...")
#     # lib の関数を使って定期実行を開始
#     lib.run_schedule(args.ticker, args.threshold, args.interval)
#
# if __name__ == "__main__":
#     main()

def main():
    parser = argparse.ArgumentParser(description="複数銘柄の株価通知ツール")
    parser.add_argument("--tickers", type=str, default="AAPL,GOOGL,AMZN",
                        help="監視する株のティッカー（カンマ区切り）")
    parser.add_argument("--thresholds", type=str, default="AAPL:150.0,GOOGL:250.0,AMZN:330.0",
                        help="各ティッカーのしきい値（例: AAPL:150.0,GOOGL:250.0,AMZN:330.0）")
    parser.add_argument("--interval", type=float, default=10, help="チェック間隔（分）")
    args = parser.parse_args()

    """
    ＜コンソール上での実行例＞※複数銘柄で実行
    python -m project --tickers AAPL,GOOGL,AMZN --thresholds AAPL:100.0,GOOGL:100.0,AMZN:100.0 --interval 0.1
    
    ＜実行結果＞
    AAPLの現在の株価: 244.60000610351562
    【通知】AAPLの株価がしきい値を超えました！ 現在の株価: 244.60000610351562
    GOOGLの現在の株価: 185.22999572753906
    【通知】GOOGLの株価がしきい値を超えました！ 現在の株価: 185.22999572753906
    AMZNの現在の株価: 228.67999267578125
    【通知】AMZNの株価がしきい値を超えました！ 現在の株価: 228.67999267578125
    監視ツールを終了します。
    """

    # カンマ区切りの文字列をリストに変換
    tickers = args.tickers.split(",")

    # thresholds をパースして辞書に変換
    thresholds = {}
    for pair in args.thresholds.split(","):
        try:
            ticker, threshold = pair.split(":")
            thresholds[ticker] = float(threshold)
        except ValueError:
            print(f"しきい値の指定形式に誤りがあります: {pair}")
            return

    print("複数銘柄の株価通知ツールを起動します...")
    lib.run_schedule_multiple(tickers, thresholds, args.interval)


if __name__ == "__main__":
    main()