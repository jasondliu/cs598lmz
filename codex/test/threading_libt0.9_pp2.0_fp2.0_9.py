import threading
threading.stack_size(5120000)

from Market import Market

from ZTradeEnv import PortfolioManager, MarketManager

from baselines import logger
from baselines.common.vec_env import SubprocVecEnv
from baselines.common.cmd_util import make_atari_env, make_mujoco_env
from baselines.common.tf_util import get_session
from baselines.run import main
from zipline.pipeline.classifiers import Classifier, Categorical
from zipline.pipeline import Pipeline
from zipline.pipeline.data import USEquityPricing
from zipline.pipeline.factors import Returns, RSI, SimpleMovingAverage, AverageDollarVolume
from zipline.utils.numpy_utils import int64_dtype

class StockEnv(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

