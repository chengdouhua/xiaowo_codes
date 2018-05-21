'''
cdh
2017-11-6日
开心消消乐用户数统计、用户消费间隔天数统计
'''
# import pandas as pd
# data = pd.read_table(r'D:\work\demand\test\pay_whole.txt', sep='\t', dtype=object)
# data['pay_day'] = pd.to_datetime(data['pay_day'])
# data['user_phone'].fillna('0', inplace=True)
#
# data['value'] = 1
# data_group = data.groupby('user_phone', as_index=False)['value'].sum()
#
# data_3_user = data_group[data_group['value']>4]['user_phone'].values
# data_3 = data[data['user_phone'].isin(data_3_user)]
#
# data_3.sort_values(by=['user_phone','pay_day'], ascending=True, inplace=True)
#
# data_3['sort_id'] = data_3['pay_day'].groupby(data_3['user_phone']).rank(method='first')
# v = data_3[data_3['sort_id'].isin([1.0, 3.0, 4.0])]
# data_3_privot_1 = v.pivot(index='user_phone', columns='sort_id', values='pay_day')
# data_3_privot_1['3_jiange'] = data_3_privot_1[3] - data_3_privot_1[1]
# data_3_privot_1['4_jiange'] = data_3_privot_1[4] - data_3_privot_1[1]
# data_3_privot_1[['3_jiange', '4_jiange']].to_csv(r'D:\work\demand\test\4_up_num_jiange.csv')


#-*- coding:utf-8 -*-

import pandas as pd
import numpy as np
data = pd.read_table(r'D:\work\Precision_marketing\000000_0', sep='\001', header=None, index_col=0)
data.head()
