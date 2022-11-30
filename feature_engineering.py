import time
start=time.time()

import pickle
import pandas as pd
from feature_engineering_functions import average_stats_df
from feature_engineering_functions import creating_ml_df

#Please state the name of the saved nested dictionary generated with '02_cleaning_stats_data.py', as well as the name of the saved output files (stats DataFrame).

stats_dict_saved_name = '2019-2022_stats.csv'

df_5_output_name = '2019-2022_df_ml_5_v2.csv'
df_10_output_name = '2019-2022_df_ml_10_v2.csv'

game_stats = pd.read_csv('2019-2022_stats.csv')


#creating a list with the team id in
team_list = []
for key in game_stats.keys():
    team_list.append(key)
team_list.sort()

#creating a dictionary with the team id as key and fixture id's as values
team_fixture_id_dict = {}
for team in team_list:
    fix_id_list = []
    for key in game_stats[team].keys():
        fix_id_list.append(key)
    fix_id_list.sort()
    sub_dict = {team:fix_id_list}
    team_fixture_id_dict.update(sub_dict)
        
#the list of fixtures was first home then away, we want them in chronological order so we need to sort them.
for team in team_fixture_id_dict:
    team_fixture_id_dict[team].sort()

#we can now iterate over the fixture ID list given a team id key using the dict created above. N.B./ the number of games over which the past data is averaged. A large number will smooth out past performance where as a small number will result in the prediction being heavily reliant on very recent form. This is worth testing the ml model build phase.

#5 game sliding average.
df_ml_5 = average_stats_df(5, team_list, team_fixture_id_dict, game_stats)

#10 game sliding average.
df_ml_10 = average_stats_df(10, team_list, team_fixture_id_dict, game_stats)

df_ml_5 = pd.DataFrame(df_ml_5)
df_ml_10 = pd.DataFrame(df_ml_10)

df_ml_5.to_csv(f'data/{df_5_output_name}')
df_ml_10.to_csv(f'data/{df_10_output_name}')
