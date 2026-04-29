import os, requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("FOOTYSTATS_API_KEY")
BASE_URL = "https://api.footystats.org"

def fetch(endpoint, params=None):
    params = params or {}
    params["key"] = API_KEY
    r = requests.get(f"{BASE_URL}/{endpoint}", params=params, timeout=30)
    r.raise_for_status()
    return r.json()

def get_all_leagues():
    return fetch("league-list")

def get_league_matches(league_id):
    return fetch("league-matches", {"league_id": league_id})

def get_league_table(league_id):
    return fetch("league-tables", {"league_id": league_id})

def get_match_details(match_id):
    return fetch("match", {"match_id": match_id})

