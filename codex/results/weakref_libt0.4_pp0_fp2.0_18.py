import weakref

from lib.common import helpers

class Module:

    def __init__(self, mainMenu, params=[]):

        self.info = {
            'Name': 'Invoke-Mimikatz',

            'Author': ['@JosephBialek', '@gentilkiwi'],

            'Description': ("Runs PowerSploit's Invoke-Mimikatz function "
                            "to extract plaintexts passwords, hash, PIN code and kerberos tickets from memory. "
                            "This module is compatible with both PowerSploit's Invoke-Mimikatz and "
                            "the reimplementation Invoke-Mimikatz included with Empire."),

            'Background' : True,

            'OutputExtension' : None,
            
            'NeedsAdmin' : True,

            'OpsecSafe' : True,

            'MinPSVersion' : '2',
            
            'Comments': [
                'https://github.com/gentilkiwi/mimikatz'
            ]
        }

        # any options needed by the module, settable during runtime
