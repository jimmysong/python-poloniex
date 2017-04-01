from poloniex import Poloniex, Coach

my_coach = Coach()
public = Poloniex(coach=my_coach)

tickers = public.returnTicker()

underpriced = {}
for pair in sorted(tickers.keys()):
    if not pair.startswith('BTC_'):
        continue
    ob = public.returnOrderBook(pair, 10000)
    bids = ob['bids']
    total_btc = 0
    for bid in bids:
        cost, amount = float(bid[0]), float(bid[1])
        total_btc += cost * amount
    asks = ob['asks']
    total_alt = 0
    for ask in asks:
        cost, amount = float(ask[0]), float(ask[1])
        total_alt += amount
    ticker = float(tickers[pair]['last'])
    sentiment = (ticker - total_btc/total_alt)/ticker * 100
    tmp = "{0:.4f} {1:.1f}".format(ticker * 1000, sentiment)
    val = "{} {}/{} {}".format(pair, total_alt, total_btc, tmp)
    underpriced[sentiment] = val
    print(".")

for k in sorted(underpriced.keys()):
    print(underpriced[k])
