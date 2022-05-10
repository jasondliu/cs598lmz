import sys, threading
threading.Thread(target=lambda: sys.stdout.write('')).start()
from pprint import pprint
from rl_bot.agent import Agent
from rl_bot.gym_bot.envs.gym_bot import GymBot
from rl_bot.utils.logger import logger_factory
from rl_bot.utils.save import create_dirs
from rl_bot.wrapper.gym_wrapper import GymWrapper
from rl_bot.utils.load import load_config_from_yaml

def main():
    config = load_config_from_yaml('../config.yaml')

    create_dirs('../', config['root'], config['name'])

    logger = logger_factory(config['log_file'], config['name'])

    env = GymBot(config, logger)
    env = GymWrapper(env)

    agent = Agent(env, config, logger)
    scores = agent.train()

    # save model
    agent.save_model(config['root'], config['name'])

    # save scores
