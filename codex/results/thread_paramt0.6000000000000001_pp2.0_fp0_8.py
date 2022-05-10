import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

from agent import Agent
from helper import Helper
from environments.gridworld import GridworldEnv
from environments.frozen_lake import FrozenLakeEnv
from environments.cliff_walking import CliffWalkingEnv
from environments.windy_gridworld import WindyGridworldEnv
from environments.taxi import TaxiEnv
from environments.acrobot import AcrobotEnv
from environments.mountain_car import MountainCarEnv
from environments.cartpole import CartPoleEnv
from environments.pong import PongEnv
from environments.lunar_lander import LunarLanderEnv
from environments.breakout import BreakoutEnv
from environments.space_invaders import SpaceInvadersEnv
from environments.ms_pacman import MsPacmanEnv
from environments.assault import AssaultEnv
from environments.beam_rider import BeamRiderEnv
from environments.enduro import EnduroEnv
from environments.kung_fu_master import KungFuMasterEnv
from
