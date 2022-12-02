from scraper import merge_ova_to_cleaned_all, scrape_team_ova_all
from constants import OVA_FILE_PATH, DATA_PATH,FINAL_FILE,CLEANED_DATA_FILE_PATH,STANDINGS_PATH,RAW_CLEANED_DATA_FILE_PATH,CURRENT_YEAR, RAW_DATA_FILE_PATH, RAW_DATA_FILE_PATH_CURRENT
from match_history1 import get_fixtures, get_current_fixtures
from clean_data import clean_all, combine_matches, get_match_results_against
from rankings import get_rankings, get_rankings_all
# from helpers import copy_csv
from current_status import add_current_details_all, add_current_details



data_year_collect_from=2019,
data_year_available_from=2019

# merge_ova_to_cleaned_all()

# Data is in data/raw/OVAs
# scrape_team_ova_all(OVA_FILE_PATH, 2018, 2022)

# get_fixtures(RAW_DATA_FILE_PATH, 2019, 2022)

# get_current_fixtures(RAW_DATA_FILE_PATH_CURRENT)

# Data is in data/cleaned/results
# clean_all(RAW_DATA_FILE_PATH, RAW_CLEANED_DATA_FILE_PATH, data_year_available_from, CURRENT_YEAR)

# Data is in data/cleaned/standings
# get_rankings_all(2019, 2022, RAW_CLEANED_DATA_FILE_PATH, STANDINGS_PATH)

# Data is in data/cleaned/results 
# merge_ova_to_cleaned_all(OVA_FILE_PATH, RAW_CLEANED_DATA_FILE_PATH, 2019, 2022) # had to rename a lot of clubs cause of key value pair errors in 2022-2023.csv

# copy_csv(RAW_CLEANED_DATA_FILE_PATH, CLEANED_DATA_FILE_PATH)

add_current_details_all(CLEANED_DATA_FILE_PATH, CLEANED_DATA_FILE_PATH, STANDINGS_PATH, data_year_available_from, CURRENT_YEAR, data_year_available_from)

# combine_matches(CLEANED_DATA_FILE_PATH, FINAL_FILE, data_year_collect_from, CURRENT_YEAR)

# get_match_results_against(FINAL_FILE, CLEANED_DATA_FILE_PATH, DATA_PATH, data_year_available_from, CURRENT_YEAR)
