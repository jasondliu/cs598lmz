import weakref

from src.core import constants as c
from src.core.util import debug, euclid
from src.elemental.status.status import Status
from src.elemental.ability.ability import Ability
from src.elemental.ability.abstract.damage_dealer import DamageDealer
from src.elemental.ability.abstract.healer import Healer
from src.elemental.ability.abstract.utility import Utility
from src.elemental.ability.abstract.transformative import Transformative
from src.elemental.ability.abstract.offensive_area_of_effect import OffensiveAreaOfEffect
from src.elemental.ability.abstract.defensive_area_of_effect import DefensiveAreaOfEffect
from src.elemental.ability.abstract.offensive_targeted_area_of_effect import (
    OffensiveTargetedAreaOfEffect)
from src.elemental.ability.abstract.defensive_targeted_area_of_effect import (
    DefensiveTargetedAreaOfEffect)
