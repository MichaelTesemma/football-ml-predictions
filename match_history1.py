import os
import pandas as pd
import requests
import numpy as np
from datetime import datetime


def convert_team_name(team):
    team_map = {
        'Manchester United FC': 'Man United',
        'Leicester City FC': 'Leicester',
        'Tottenham Hotspur FC': 'Tottenham',
        'Newcastle United FC': 'Newcastle',
        'Chelsea FC': 'Chelsea',
        'Huddersfield Town AFC': 'Huddersfield',
        'Crystal Palace FC': 'Crystal Palace',
        'Fulham FC': 'Fulham',
        'AFC Bournemouth': 'Bournemouth',
        'Cardiff City FC': 'Cardiff',
        'Watford FC': 'Watford',
        'Brighton & Hove Albion FC': 'Brighton',
        'Wolverhampton Wanderers FC': 'Wolves',
        'Everton FC': 'Everton',
        'Arsenal FC': 'Arsenal',
        'Manchester City FC': 'Man City',
        'Liverpool FC': 'Liverpool',
        'West Ham United FC': 'West Ham',
        'Southampton FC': 'Southampton',
        'Burnley FC': 'Burnley',
        'Aston Villa FC': 'Aston Villa',
        'Norwich City FC': 'Norwich City',
        'Sheffield United FC': 'Sheffield United'
    }
    return team_map[team] if team in team_map else team

def get_fixtures(rawDataPath, yearFrom, yearTo):
    def format_api_url(year):
        base_url = 'https://www.football-data.co.uk/mmz4281/{}{}/E0.csv'
        return base_url.format(str(year)[2:], str(year + 1)[2:])
    # def format_api_url(year):
    #     base_url = 'http://www.football-data.co.uk/mmz4281/{}/E0.csv'
    #     return base_url.format(str(year))

    def format_file_path(year):
        return os.path.join(rawDataPath, f'{year}-{year + 1}.csv')
    
    for year in range(yearFrom, yearTo + 1):
        url = format_api_url(year)
        print(url, year)
        file_path = format_file_path(year)
        try:
            if not os.path.exists(file_path) or year > yearTo - 2:
                df = pd.read_csv(url)
                df.to_csv(file_path, index=False)
                print(f'Saved fixtures for {year}...')
        except:
            print(f'Failed to save fixtures for {year}!')
            continue
        # try:
        #     df = pd.read_csv(url)
        #     df.to_csv(file_path, index=False)
        #     print(f'Saved fixtures for {year}...')
        # except:
        #     print(url, year)
        #     print(f'Failed to save fixtures for {year}!')
        #     print(file_path)
        #     continue


def get_current_fixtures(rawDataCurrentPath):
    base_url = "http://api.football-data.org/v2/competitions/"
    AUTH_TOKEN = "9f2efd00a5604f59a8f1c54860786e31"
    headers={"X-Auth-Token": AUTH_TOKEN}

    print("Getting results and fixtures for this year...")

    england_area_code = 2072
    list_competitions_url = base_url + "?areas=" + str(england_area_code)
    req = requests.get(list_competitions_url, headers=headers).json()
    premier_league_data = [x for x in req['competitions'] if x['name'] == 'Premier League'][0]
    premier_league_id = premier_league_data['id']

    matches_url = base_url + str(premier_league_id) + "/matches"
    match_data = requests.get(matches_url, headers=headers).json()['matches']

    matches_dict = {
        'Date': [match['utcDate'].split('T')[0] for match in match_data],
        'HomeTeam': [convert_team_name(match['homeTeam']['name']) for match in match_data],
        'AwayTeam': [convert_team_name(match['awayTeam']['name']) for match in match_data],
        'FTHG': [match['score']['fullTime']['homeTeam'] if match['status'] == "FINISHED" else np.nan for match in match_data],
        'FTAG': [match['score']['fullTime']['awayTeam'] if match['status'] == "FINISHED" else np.nan for match in match_data],
        'FTR': [match['score']['winner'][0] if match['status'] == "FINISHED" and match['score']['winner'] else "" for match in match_data]
    }

    df = pd.DataFrame(matches_dict)
    df.to_csv(rawDataCurrentPath, index=False)




