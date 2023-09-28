import json
import os
from pysnowballplus import api_ref
from pysnowballplus import utls

# EastMoney RPT_BOND_CB_LIST


def convertible_bond(page_size, page_count):
    url = api_ref.convertible_bond.format(page_size, page_count)
    return utls.fetch_eastmoney(url)
