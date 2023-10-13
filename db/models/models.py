from decimal import Decimal

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Numeric, Date, Enum
from sqlalchemy.orm import relationship

from db.config import Base
from enums import SportLeague
from db.models.mixins import Timestamp


class BirthPlace(Timestamp, Base):
    __tablename__ = "birth_place"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    place = Column(String(70))
    country = Column(String, index=True)

    player = relationship("Player", back_populates="people")


class Player(Base):
    __tablename__ = "player"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    age = Column(Integer)
    nationality = Column(String(20), index=True)
    birth = Column(Integer, ForeignKey("birth_place.id"), nullable=False)
    injured = Column(Boolean, default=False)
    people = relationship("BirthPlace", back_populates="people")
    sport_league = Column(Enum(SportLeague))


class NbaPlayer(Player):
    __tablename__ = "nba_player"
    season = Column(Integer, ForeignKey("nba_season.id"), nullable=True)
    players = relationship("NbaSeason", back_populates="players")



class NbaSeason(Base):
    __tablename__ = "nba_season"
    id = Column(Integer, primary_key=True)
    players = relationship("NbaPlayer", back_populates="players")
    season_start = Column(Date)
    season_end = Column(Date)
    games_played = Column(Integer)
    wins = Column(Integer)
    looses = Column(Integer)
    minutes_played = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    points = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    field_goals_made = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    field_goals_attempted = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    field_goals_percentage = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    three_point_field_goals_made = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    three_point_field_goals_attempted = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    three_point_field_goals_percentage = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    free_throws_made = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    free_throws_attempted = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    free_throws_percentage = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    offensive_rebounds = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    defensive_rebounds = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    rebounds = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    assists = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    turnovers = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    steals = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    blocks = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    personal_fouls = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    fantasy_points = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    double_doubles = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    triple_doubles = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
    plus_minus = Column(Numeric(precision=8,scale=2), nulable=False, default=Decimal('0.00'))
