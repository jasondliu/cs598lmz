import weakref
from unittest.mock import Mock
import os
import asyncio
import asyncpg
from aioredis import create_redis, Redis
import db
from cassiopeia import riotapi
from cassiopeia.dto.summonerapi import SummonerDto
from cassiopeia.type.core.common import MapType
from cassiopeia.type.api.exception import APIError, NotFoundError
from cassiopeia.datastores import CassiopeiaDB, SQLAlchemyDB
import dtos
import pytest
from config import Config
from logics.game import MatchLogic
from logics.player import PlayerLogic
from logics.summoner import SummonerLogic
from models.cass import Champion, Item, SummonerSpell
from models.riot import Match
from models.lol import Player, Summoner, PlayerMatch
from logics.gamequeue import GameQueueLogic
