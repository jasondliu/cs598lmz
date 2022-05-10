import select
import sys
import time
import os

class InputModule:
	"""
	Contains all the methods necessary for reading and parsing user input.
	"""

	def __init__(self):
		"""
		Initializes the default values for a new InputModule object.

		@return			None
		"""
		self.clear_buffer()
		self.clear_screen_commands = ["clear", "cls"]
		self.exit_commands = ["exit", "quit", "q"]
		self.pause_commands = ["pause"]
		self.help_commands = ["help"]
		self.command_list = self.clear_screen_commands + self.exit_commands + self.pause_commands + self.help_commands
		self.command_tree = {}
		self.add_commands_to_tree(self.command_list, self.command_tree)
		self.help_message = ""
		self.latest_command = ""
		self.previous_command = ""
