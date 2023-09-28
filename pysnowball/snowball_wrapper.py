#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pytz

bj_tz = pytz.timezone('Asia/Shanghai')


def kline_todf(kline_dict):
    """
    转换kline接口到DataFrame
    :param kline: ball.kline()
    :return: DataFrame
    """
    df = pd.DataFrame(kline_dict['data']['item'], columns=kline_dict['data']['column'])
    timestamp_idx = df.columns.get_loc('timestamp')
    df.insert(timestamp_idx, 'datetime',
              pd.to_datetime(df.timestamp, unit='ms', utc=True).dt.tz_convert(bj_tz))
    return df


def watch_stock_todf(stock_dict):
    """
    转换watch_stock接口到DataFrame
    :param stock_dict: ball.stock()
    :return: DataFrame
    """

    stocks_df = pd.DataFrame(stock_dict['data']['stocks'])
    created_idx = stocks_df.columns.get_loc('created')
    stocks_df.insert(created_idx, 'created_dt',
                     pd.to_datetime(stocks_df.created, unit='ms', utc=True).dt.tz_convert(bj_tz))
    return stocks_df
