import pandas as pd
from os import listdir 
import math
import time

data = pd.read_csv('data/2010_fixtures_df.csv')
# data = pd.read_csv('data/2010_fixtures_df.csv')
# data1 = pd.read_csv('data/2011_fixtures_df.csv')
# data2 = pd.concat([data, data1])
# clean = data2.reset_index(drop=True)
# folder = listdir('data')
# print(len(folder))
# df_list = []
# for i in range(2010, 2022):
#     df_list.append(pd.read_csv(f'data/{i}_fixtures_df.csv'))

# df = pd.concat(df_list)
# df = df.reset_index(drop=True)
# df.to_csv('data/2010-2022.csv')
# for i in data.index[288:300]:
#     if math.isnan(data['Home Team Goals'].iloc[i]) == False:
#         print(data['Home Team Goals'])

# for i in range(100):
#     pause_points = [(i*10)-1 for i in range(10)]
#     if i in pause_points:
#         print('sleeping for 1 minute - API only allows 10 requests per minute')
#         time.sleep(2)
#     print(i)
df_list = []
for i in range(2019, 2022):
    df_list.append(pd.read_csv(f'data/{i}_fixtures_df.csv'))

df = pd.concat(df_list)
df = df.reset_index(drop=True)
df.to_csv('data/2019-2022.csv')