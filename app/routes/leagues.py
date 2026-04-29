from fastapi import APIRouter
from app.services.footystats import get_all_leagues, get_league_table

router = APIRouter()

@router.get("/")
def leagues():
    return get_all_leagues()

@router.get("/{league_id}/table")
def table(league_id:int):
    return get_league_table(league_id)

