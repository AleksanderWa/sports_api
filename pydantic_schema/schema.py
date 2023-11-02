from datetime import datetime

from pydantic import BaseModel

from db.models.models import SportLeague


class Birth(BaseModel):
    date: datetime
    place: str
    country: str


class Player(BaseModel):
    name:str
    first_name:str
    last_name:str
    age:int
    nationality:str
    birth: Birth
    injured: bool
    sport_league: SportLeague
