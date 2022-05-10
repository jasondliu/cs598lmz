import threading
# Test threading daemon
import time
import sys
import os
sys.path.append(os.path.abspath('..'))

from core.server import Server
from core.messages.keys import Keys
from core.messages.translator.messages_keys import MessagesKeys
from core.result import Result
from core.config import Configuration
from core.validation.helpers import db_error_message
from core.commands.add_new_car import AddNewCar
from core.commands.add_new_shop import AddNewShop
from core.commands.change_shop_location import ChangeShopLocation
from core.commands.assign_car_to_shop import AssignCarToShop
from core.commands.assign_car_to_business import AssignCarToBusiness
from core.commands.make_car_ready import MakeCarReady
from core.commands.make_car_not_ready import MakeCarNotReady
from core.commands.sign_up_business import SignUpBusiness
from core.commands.sign_up_business_owner import SignUpBusinessOwner
from core.comm
