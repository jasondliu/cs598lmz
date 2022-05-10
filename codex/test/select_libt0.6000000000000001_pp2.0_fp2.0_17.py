import select
import sys
import time

import pygame

import constants
import level
import player
import platforms
import projectiles

def quit_game():
    """Handle the keyboard quit event."""
    pygame.quit()
    sys.exit()

def main():
    """Main loop to control the game."""
    # Initialize the pygame library
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Jumpy!")

    # Create the player
    player = player.Player()

    # Create all the levels
    level_list = []
    level_list.append(level.Level_01(player))
    level_list.append(level.Level_02(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_
