# python3

import pandas as pd 
import os

os.mkdir('./csv/')

df_charge = pd.read_csv('./txt/charge.txt')
df_charge.to_csv('./csv/charge.csv', index = None)

df_time = pd.read_csv('./txt/time.txt')
df_time.to_csv('./csv/time.csv', index = None)

df_position = pd.read_csv('./txt/position.txt')
df_position.to_csv('./csv/position.csv', index = None)

df_time_nop = pd.read_csv('./txt/time_nop.txt')
df_time_nop.to_csv('./csv/time_nop.csv', index = None)
