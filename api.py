import time
start=time.time()

import requests
import pandas as pd
import math
from os import listdir

YEAR = 2017
YEAR_str = str(YEAR)

request_league_ids = False
request_fixtures = True
request_missing_game_stats = True
api_key = "8e97d665523a3691213379e0d80a7044"
base_url = 'https://v2.api-football.com/'


# # Request Functions


def get_api_data(base_url, end_url):
    url = base_url + end_url
    headers = {'X-RapidAPI-Key': api_key}
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        raise RuntimeError(f'error {res.status_code}')
    res_t = res.text
    return res_t


def slice_api(api_str_output, start_char, end_char):
  e = len(api_str_output) - end_char
  s = start_char
  output = api_str_output[s:e]
  return output


def save_api_output(save_name, jason_data, json_data_path=''):
    writeFile = open(json_data_path + save_name + '.json', 'w')
    writeFile.write(jason_data)
    writeFile.close()
    
    
def read_json_as_pd_df(json_data, json_data_path='', orient_def='records'):
    output = pd.read_json(json_data_path + json_data, orient=orient_def)
    return output

# # Requesting Data

# def req_prem_fixtures_id(season_code, year=YEAR_str):
#     #request to the api for the data
#     premier_league_fixtures_raw = get_api_data(base_url, f'/fixtures/league/{season_code}/')

#     #cleaning the data in preparation for loading into a dataframe
#     premier_league_fixtures_sliced = slice_api(premier_league_fixtures_raw, 33, 2)

#     #saving the clean data as a json file
#     save_api_output(f'{year}_fixtures', premier_league_fixtures_sliced, json_data_path = 'data/')

#     #loading the json file as a DataFrame
#     premier_league_fixtures_df = read_json_as_pd_df(f'{year}_fixtures.json', json_data_path='data/')
#     return premier_league_fixtures_df

# # requesting data using the league id's of seasons

# if request_league_ids:
#     leagues = premier_league_fixtures_raw = get_api_data(base_url, 'leagues/search/premier_league')

# if YEAR == 2010:
#     season_id = 701
# elif YEAR == 2011:
#     season_id = 700
# elif YEAR == 2012:
#     season_id = 699
# elif YEAR == 2013:
#     season_id = 698
# elif YEAR == 2014:
#     season_id = 697
# elif YEAR == 2015:
#     season_id = 696
# elif YEAR == 2016:
#     season_id = 56
# elif YEAR == 2017:
#     season_id= 37
# elif YEAR == 2018:
#     season_id= 2
# elif YEAR == 2019:
#     season_id = 524
# elif YEAR == 2020:
#     season_id = 2790
# elif YEAR == 2021:
#     season_id = 3456
# elif YEAR == 2022:
#     season_id= 4335
# else:
#     print('please lookup season id and specify this as season_id variable')

# #requesting the fixture list using the function req_prem_fixture_id
# if request_fixtures:
#     fixtures = req_prem_fixtures_id(season_id, YEAR_str)
    

# def load_prem_fixtures_id(year=YEAR_str):
#     premier_league_fixtures_df = read_json_as_pd_df(f'{year}_fixtures.json', json_data_path='data/')
#     return premier_league_fixtures_df


# fixtures = load_prem_fixtures_id()

# # Cleaning up the Fixture List

# fixtures = pd.read_json(f'data/{YEAR_str}_fixtures.json', orient='records')

# #creating clean past fixture list DataFrame       

# for i in fixtures.index:
#     x1 = str(fixtures['homeTeam'].iloc[i])[12:14]
#     x = int(x1)
#     fixtures.at[i, 'HomeTeamID'] = x

# for i in fixtures.index:
#     x1 = str(fixtures['awayTeam'].iloc[i])[12:14]
#     x = int(x1)
#     fixtures.at[i, 'AwayTeamID'] = x

# for i in fixtures.index:
#     x = str(fixtures['event_date'].iloc[i])[:10] 
#     fixtures.at[i, 'Game Date'] = x

# for i in fixtures.index:
#     x = str(fixtures['homeTeam'][i]['team_name']) 
#     fixtures.at[i, 'Home Team'] = x
    
# for i in fixtures.index:
#     x = str(fixtures['awayTeam'][i]['team_name']) 
#     fixtures.at[i, 'Away Team'] = x
    
# for i in fixtures.index:
#     x = str(fixtures['homeTeam'][i]['logo']) 
#     fixtures.at[i, 'Home Team Logo'] = x
    
# for i in fixtures.index:
#     x = str(fixtures['awayTeam'][i]['logo']) 
#     fixtures.at[i, 'Away Team Logo'] = x
 
# fixtures_clean = pd.DataFrame({'Fixture ID': fixtures['fixture_id'], 'Game Date': fixtures['Game Date'], 'Home Team ID': fixtures['HomeTeamID'], 'Away Team ID': fixtures['AwayTeamID'], 'Home Team Goals': fixtures['goalsHomeTeam'], 'Away Team Goals': fixtures['goalsAwayTeam'], 'Venue': fixtures['venue'], 'Home Team': fixtures['Home Team'], 'Away Team': fixtures['Away Team'], 'Home Team Logo': fixtures['Home Team Logo'], 'Away Team Logo': fixtures['Away Team Logo']})

# fixtures_clean.to_csv(f'data/{YEAR_str}_fixtures_df.csv', index=False)

# Stiching Clean Fixture List

# all_fixtures = []
# for i in range(2010, 2022):
#     all_fixtures.append(pd.read_csv(f'data/{i}_fixtures_df.csv'))

# combined = pd.concat(all_fixtures)
# combined = combined.reset_index(drop=True)
# combined.to_csv('data/2010-2022.csv', index=False)

# Requesting Specific Stats

fixtures_clean = pd.read_csv(f'data/{YEAR_str}_fixtures_df.csv')


def req_prem_stats(start_index, end_index):
    for i in fixtures_clean.index[start_index:end_index]:
        if math.isnan(fixtures_clean['Home Team Goals'].iloc[i]) == False:
            fix_id = str(fixtures_clean['Fixture ID'].iloc[i])
            fixture_raw = get_api_data(base_url, '/statistics/fixture/' + fix_id + '/')
            fixture_sliced = slice_api(fixture_raw, 34, 2)
            save_api_output('json/2017/' + fix_id, fixture_sliced)
            print('sleeping for 6 seconds - API only allows 10 requests per minute')
            with open("2017.txt", 'w') as f:
                f.write(f'the id number is {fix_id} and index is {i + 1}')
            print(f'Getting match number {i}')
            time.sleep(6)

req_prem_stats(0, 50)



