import sys, threading

def run():
    sys.path.append("../")
    from src.engine import Engine
    from src.utils import *

    from src.modules.model import Model
    from src.modules.view import View
    from src.modules.controller import Controller

    from src.modules.model.model_manager import ModelManager
    from src.modules.view.view_manager import ViewManager
    from src.modules.controller.controller_manager import ControllerManager

    from src.modules.model.models.game_model import GameModel
    from src.modules.view.screens.game_screen import GameScreen
    from src.modules.controller.controllers.game_controller import GameController

    from src.modules.model.models.main_menu_model import MainMenuModel
    from src.modules.view.screens.main_menu_screen import MainMenuScreen
    from src.modules.controller.controllers.main_menu_controller import MainMenuController

    from src.modules.model.models.options_model import OptionsModel
    from src.modules.view.screens.options_screen import OptionsScreen
    from src.
