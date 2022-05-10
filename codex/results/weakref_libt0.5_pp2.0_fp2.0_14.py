import weakref

from . import app, gui, config, qtutils
from .i18n import N_
from .models import prefs
from .qtutils import (
    add_action,
    create_action,
    create_menu,
    connect_action,
    connect_boolean_action,
    connect_button,
    connect_combo_action,
    connect_radio_action,
    connect_toggle_action,
    connect_spinbox_action,
    connect_slider_action,
    connect_action_bool,
    connect_action_int,
    connect_action_string,
    connect_action_menu,
    connect_toggle_button,
    connect_action_button,
    connect_radio_button,
    connect_action_shortcut,
    connect_action_list,
    connect_list_action,
    connect_list_toggle,
    connect_list_radio,
    connect_list_action_bool,
    connect_list_action_int,
    connect_list_action_string,
    connect_list_action_menu
