import time
from pysnowballplus import cons
from pysnowballplus import api_ref
from pysnowballplus import utls
from pysnowballplus import snowball_wrapper as sw

def quotec(symbols):
    url = api_ref.realtime_quote+symbols
    return sw.quotec_todf(utls.fetch_without_token(url))


def quote_detail(symbol):
    return sw.quote_detail_todf(utls.fetch(api_ref.realtime_quote_detail+symbol))


def pankou(symbol):
    url = api_ref.realtime_pankou+symbol
    return sw.pankou_todf(utls.fetch(url))


def kline(symbol, days=100):
    dict_data = utls.fetch(api_ref.kline.format(symbol, int(time.time()*1000), days))
    return sw.kline_todf(dict_data)
