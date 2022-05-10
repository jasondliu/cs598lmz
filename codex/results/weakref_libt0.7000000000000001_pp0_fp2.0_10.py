import weakref

import ui
import sound

import rpg_constants
import rpg_scene

import rpg_battle
import rpg_battle_animation
import rpg_battle_party
import rpg_battle_enemy
import rpg_battle_actor
import rpg_battle_skill
import rpg_battle_item
import rpg_battle_status_window

#-------------------------------------------------------------------------------
#  'Battle' class:
#-------------------------------------------------------------------------------

class Battle( rpg_scene.Scene ):
    """RPG battle scene class."""

    #---------------------------------------------------------------------------
    #  Trait definitions:
    #---------------------------------------------------------------------------

    # Current scene state
    state = Enum( 'initial', 'animating', 'choosing_action', 'choosing_target',
                  'choosing_skill', 'choosing_item', 'actors_turn', 'enemies_turn',
                  'victory', 'game_over' )
    state_changed = Event

    # Current scene mode
    mode = Enum( 'active', 'passive' )
    mode_changed = Event

    # Current turn

