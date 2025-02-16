# myproject/mylib/mylib.py
import time
import schedule
import yfinance as yf


def get_stock_price(ticker):
    """
    指定したティッカーの最新株価を取得する関数
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    if not data.empty:
        # 最新の終値を返す
        return data['Close'].iloc[-1]
    return None


def notify_user(ticker, price):
    """
    しきい値を超えた場合の通知処理（コンソール表示）
    """
    print(f"【通知】{ticker}の株価がしきい値を超えました！ 現在の株価: {price}")


def check_stocks(tickers, thresholds):
    """
    複数の銘柄の株価を取得し、しきい値を超えている場合は通知する関数
    """
    for ticker in tickers:
        price = get_stock_price(ticker)
        if price is None:
            print(f"{ticker}の株価データ取得に失敗しました。")
            continue
        print(f"{ticker}の現在の株価: {price}")
        if ticker in thresholds and price > thresholds[ticker]:
            notify_user(ticker, price)


def run_schedule_multiple(tickers, thresholds, interval_minutes=10):
    """
    scheduleライブラリを使い、複数銘柄の株価チェックを定期的に実行する関数

    Parameters:
      tickers: 監視対象の株式ティッカーのリスト
      thresholds: 各ティッカーのしきい値を格納した辞書
      interval_minutes: チェック間隔（分）
    """

    def job():
        check_stocks(tickers, thresholds)

    schedule.every(interval_minutes).minutes.do(job)

    print("複数銘柄の株価監視ツールを開始します。Ctrl+Cで終了してください。")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("監視ツールを終了します。")
