from pysnowballplus import api_ref
from pysnowballplus import utls
from pysnowballplus import snowball_wrapper as sw

def watch_list():
    url = api_ref.watch_list
    return utls.fetch(url)

def watch_stock(id):
    url = api_ref.watch_stock + str(id)
    return sw.watch_stock_todf(utls.fetch(url))