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
    df['date'] = df.datetime.dt.date
    df.set_index('date', inplace=True)
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


def quotec_todf(quotec_dict):
    """

    :param quotec_dict:
    :return:
    """
    df = pd.DataFrame(quotec_dict['data'])
    timestamp_idx = df.columns.get_loc('timestamp')
    df.insert(timestamp_idx, 'datetime',
              pd.to_datetime(df.timestamp, unit='ms', utc=True).dt.tz_convert(bj_tz))
    return df


def pankou_todf(pankou_dict):
    # print(pankou_dict)

    df = pd.DataFrame([pankou_dict['data']])
    timestamp_idx = df.columns.get_loc('timestamp')
    df.insert(timestamp_idx, 'datetime',
              pd.to_datetime(df.timestamp, unit='ms', utc=True).dt.tz_convert(bj_tz))
    return df


def quote_detail_todf(detail_dict, need_all=False):
    # print(detail_dict['data']['market'])
    # print(detail_dict['data']['quote'])
    # print(detail_dict['data']['others'])
    # print(detail_dict['data']['tags'])

    market_df = pd.DataFrame([detail_dict['data']['market']])
    quote_df = pd.DataFrame([detail_dict['data']['quote']])
    others_df = pd.DataFrame([detail_dict['data']['others']])
    tags_df = pd.DataFrame(detail_dict['data']['tags'])

    timestamp_idx = quote_df.columns.get_loc('timestamp')
    quote_df.insert(timestamp_idx, 'datetime',
                    pd.to_datetime(quote_df.timestamp, unit='ms', utc=True).dt.tz_convert(bj_tz))

    if need_all:
        return (quote_df, market_df, others_df, tags_df)
    else:
        return quote_df


def minute_todf(minute_dict):
    df = pd.DataFrame(minute_dict['data']['items'])
    timestamp_idx = df.columns.get_loc('timestamp')
    df.insert(timestamp_idx, 'datetime',
              pd.to_datetime(df.timestamp, unit='ms', utc=True).dt.tz_convert(bj_tz))
    return df


def trade_todf(trade_dict):
    df = pd.DataFrame(trade_dict['data']['items'])
    timestamp_idx = df.columns.get_loc('timestamp')
    df.insert(timestamp_idx, 'datetime',
              pd.to_datetime(df.timestamp, unit='ms', utc=True).dt.tz_convert(bj_tz))
    return df
