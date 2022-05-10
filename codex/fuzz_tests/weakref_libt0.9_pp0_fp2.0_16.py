import weakref
import gc
import pygame

class ObjectManager:
    """
    This class is used to keep track of all the sprites. It makes it easier for
    subclasses to do the collision detection on all sprites, rather than doing it
    on each object.
    
    You can add any object to the object manager with the add() function.
    Whenever an object wants to be removed from the object manager, it calls
    remove() on itself.
    """
    def __init__(self) :
        self.sprites = [] # List containing all the sprites.

    def add(self, sprite) :
        """
        Adds a sprite to the game manager.
        """
        self.sprites.append(sprite)
        
    def remove(self, sprite):
        """
        Removes a sprite from the game manager.
        """
        # We first make sure that the sprite is in the list at all.
        if sprite in self.sprites:
            # If it is in the list, remove it.
            self.sprites.remove(sprite)
            
class GameUtility:
