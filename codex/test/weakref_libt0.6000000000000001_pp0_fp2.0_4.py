import weakref

import freeOrionAIInterface as fo  # pylint: disable=import-error

import AIFleetOrder
import AITarget
import CombatRatingsAI
import FleetUtilsAI
import ExplorationAI
import MilitaryAI
import MoveUtilsAI
import PlanetUtilsAI
import PriorityAI
import ResourcesAI
import TechsListsAI
import AIAbstractMissionType
import AIDependencies
import AITarget
import ColonisationAI

# TODO: rename this module to something more meaningful
# TODO: split this module into several smaller modules

# debug printing: 1 for basic info, 2 for detailed info
PRINT_MILITARY_DEBUG = 1
PRINT_DEBUG = 0

# TODO: rename to more meaningful variable names, add comments explaining the logic
SHIP_STAT_MULTIPLIERS = [0.1, 0.2, 0.3, 0.5, 0.8]

# TODO: add comments explaining the logic
