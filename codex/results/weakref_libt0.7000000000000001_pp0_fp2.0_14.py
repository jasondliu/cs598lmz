import weakref
from typing import Any, Dict, List, Optional, Tuple, Union

import torch

from ray.rllib.agents.trainer import DEFAULT_CONFIG
from ray.rllib.agents.trainer_template import build_trainer
from ray.rllib.evaluation import MultiAgentEpisode
from ray.rllib.execution.common import STEPS_SAMPLED_COUNTER, STEPS_TRAINED_COUNTER
from ray.rllib.models.catalog import ModelCatalog
from ray.rllib.optimizers import LocalSyncOptimizer
from ray.rllib.optimizers.policy_optimizer import PolicyOptimizer
from ray.rllib.optimizers.replay_buffer import ReplayBuffer
from ray.rllib.optimizers.sample_batch_builder import SampleBatchBuilder
from ray.rllib.optimizers.samplers import DefaultSampler, _compute_weights
from ray.rllib.policy.policy import Policy
from ray.rllib.policy.sample_batch import SampleBatch
from ray
