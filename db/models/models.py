import enum

from decimal import Decimal

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Table,
)
from sqlalchemy.orm import (
    declared_attr,
    relationship,
)

from db.config import Base
from db.models.mixins import Timestamp


class SportLeague(enum.Enum):
    NBA = 1
    # two = 2
    # three = 3


class BirthPlace(Timestamp, Base):
    __tablename__ = "birth_place"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    place = Column(String(70))
    country = Column(String, index=True)

    player = relationship("Player", back_populates="people")


class Player(Base):
    # __tablename__ = "player"
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    age = Column(Integer)
    nationality = Column(String(20), index=True)

    @declared_attr
    def birth(self):
        return Column(Integer, ForeignKey("birth_place.id"), nullable=False)

    injured = Column(Boolean, default=False)
    sport_league = Column(Enum(SportLeague))


team_season_m2m_table = Table(
    'nba_team_season',
    Base.metadata,
    Column('nba_team_id', Integer, ForeignKey('nba_team.id')),
    Column('nba_season_id', Integer, ForeignKey('nba_season.id')),
)


class Team(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True)
    code = Column(String(6))
    city = Column(String(50), index=True)


class NbaTeam(Team):
    __tablename__ = "nba_team"

    # id = Column(Integer, primary_key=True)
    # name = Column(String(50), index=True)
    # code = Column(String(6))
    #


player_season_m2m_table = Table(
    'nba_player_season',
    Base.metadata,
    Column('nba_player_statistics_id', Integer, ForeignKey('nba_player_statistics.id')),
    Column('nba_season_id', Integer, ForeignKey('nba_season.id')),
)


class NbaPlayer(Player):
    __tablename__ = "nba_player"
    # id = Column(Integer, primary_key=True)
    # player = Column(Integer, ForeignKey("player.id"), nullable=False)
    # season = Column(Integer, ForeignKey("nba_season.id"), nullable=True)


class Season(Base):
    # __tablename__ = "season"
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    season_start = Column(Date)
    season_end = Column(Date)


class NbaSeason(Season):
    __tablename__ = "nba_season"
    # id = Column(Integer, primary_key=True)
    # season = Column(Integer, ForeignKey("season.id"), nullable=False)
    players = relationship(
        'NbaPlayer', secondary=player_season_m2m_table, back_populates='seasons'
    )


class NbaPlayerStatistics(Base):
    __tablename__ = "nba_player_statistics"
    id = Column(Integer, primary_key=True)
    player = Column(Integer, ForeignKey("nba_player.id"), nullable=False)
    seasons = relationship(
        'NbaSeason', secondary=player_season_m2m_table, back_populates='players'
    )
    games_played = Column(Integer)
    wins = Column(Integer)
    looses = Column(Integer)
    minutes_played = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    points = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    field_goals_made = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    field_goals_attempted = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    field_goals_percentage = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    three_point_field_goals_made = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    three_point_field_goals_attempted = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    three_point_field_goals_percentage = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    free_throws_made = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    free_throws_attempted = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    free_throws_percentage = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    offensive_rebounds = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    defensive_rebounds = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    rebounds = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    assists = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    turnovers = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    steals = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    blocks = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    personal_fouls = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    fantasy_points = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    double_doubles = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    triple_doubles = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )
    plus_minus = Column(
        Numeric(precision=8, scale=2), nullable=False, default=Decimal('0.00')
    )

    # sportleague_type = postgresql.ENUM('NBA', name='sportleague', create_type=False)
    # sportleague_type.create(op.get_bind(), checkfirst=True)
    # op.add_column('nba_player', sa.Column('sport_league', sportleague_type, nullable=True))
