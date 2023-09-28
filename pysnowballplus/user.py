from pysnowballplus import api_ref
from pysnowballplus import utls

def watch_list():
    url = api_ref.watch_list
    return utls.fetch(url)

def watch_stock(id):
    url = api_ref.watch_stock + str(id)
    return utls.fetch(url)