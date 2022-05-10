import threading
threading.stack_size(2**27)
import sys
sys.path.append("../")

from card_game.envs.card_game_env import CardGameEnv
from card_game.envs.card_game_env_test import CardGameEnvTest
from card_game.envs.card_game_env_test_single import CardGameEnvTestSingle
from card_game.envs.card_game_env_test_multi import CardGameEnvTestMulti

from agent.agent import Agent
from agent.agent_random import AgentRandom

from player.player_model import PlayerModel
from player.player_random import PlayerRandom
from player.player_rule_based import PlayerRuleBased
from player.player_rule_based_v2 import PlayerRuleBasedV2
from player.player_rule_based_v3 import PlayerRuleBasedV3
from player.player_rule_based_v4 import PlayerRuleBasedV4
from player.player_rule_based_v5 import PlayerRuleBasedV5

from utils.utils import Utils

from config import Config


