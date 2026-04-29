from fastapi import APIRouter
from datetime import datetime, timedelta
from app.services.footystats import get_all_leagues, get_league_matches, get_match_details

router = APIRouter()

def filter_by_date(target):
    result = []
    leagues = get_all_leagues().get("data", [])
    for league in leagues[:50]:
        try:
            matches = get_league_matches(league.get("id")).get("data", [])
            filtered = [m for m in matches if str(m.get("date","")).startswith(target)]
            if filtered:
                result.append({
                    "league": league.get("name"),
                    "league_logo": league.get("image"),
                    "matches": filtered
                })
        except:
            continue
    return result

@router.get("/today")
def today():
    return filter_by_date(datetime.utcnow().date().isoformat())

@router.get("/tomorrow")
def tomorrow():
    return filter_by_date((datetime.utcnow().date()+timedelta(days=1)).isoformat())

@router.get("/{match_id}")
def match_details(match_id:int):
    return get_match_details(match_id)
