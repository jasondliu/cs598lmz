import weakref

#from Kamaelia.UI.Pygame.Button import Button
#from Kamaelia.UI.Pygame.Text import Textbox, TextDisplayer
#from Kamaelia.Chassis.Pipeline import Pipeline
#from Kamaelia.Util.Console import ConsoleReader, ConsoleEchoer


import pygame
import pygame.font
import pygame.event
import pygame.draw
import pygame.image

from Axon.Ipc import producerFinished, shutdownMicroprocess

from Kamaelia.Util.PipelineComponent import pipeline
from Kamaelia.Chassis.Graphline import Graphline

from Kamaelia.UI.Pygame.Button import Button

from Kamaelia.Util.Console import ConsoleEchoer


class Console(Axon.Component.component):
    Inboxes = {
        "inbox" : "Receive events here",
        "control" : "For shutdown messages",
        "callback" : "For replies to callback messages",
        "reveal" : "Receive messages that tell the console to reveal itself"
    }
   
