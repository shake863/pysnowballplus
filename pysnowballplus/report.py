import json
import os
from pysnowballplus import cons
from pysnowballplus import api_ref
from pysnowballplus import utls


def report(symbol):
    url = api_ref.report_latest_url+symbol
    return utls.fetch(url)


def earningforecast(symbol):
    url = api_ref.report_earningforecast_url+symbol
    return utls.fetch(url)
