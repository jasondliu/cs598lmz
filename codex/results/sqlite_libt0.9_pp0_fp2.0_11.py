import ctypes
import ctypes.util
import threading
import sqlite3


log = logging.getLogger(__name__)

bluez_services = {'OBEX File Transfer': '0x1106', 'OBEX Object Push': '0x1105',
                  'OBEX Phonebook Access': '0x1130', 'Dial-up Networking': '0x1103',
                  'Generic Networking': '0x1202', 'Hardcopy Cable Replacement Profile (HCRP)': '0x1122',
                  'Fax Service': '0x1111', 'Serial Port Profile (SPP)': '0x1101',
                  'Lazy Sniff': '0x1MLS', 'Personal Area Networking User': '0x1116',
                  'Personal Area Networking Client': '0x1115', 'Headset Profile': '0x1108',
                  'A/V Remote Control Target': '0x110c', 'A/V Remote Control': '0x110e',
                  'SIM Access Profile (SAP)': '0x112D'}

bluez_adapter = None
bluez_adapter_path = None
bluez_ad
