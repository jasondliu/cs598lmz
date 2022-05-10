import gc, weakref
from collections import defaultdict

import pygame

from . import pview, ptext, pviewport, pglobals
from .pview import T

class Scene(pview.View):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.actors = []
		self.add_actor(self)
		self.viewport = pviewport.Viewport(self)

	def add_actor(self, actor):
		self.actors.append(actor)
		actor.scene = self

	def draw(self, surf):
		for actor in self.actors:
			if actor.visible:
				surf.blit(actor.surf, actor.pos)

	def update(self, dt):
		for actor in self.actors:
			if actor.visible:
				actor.update(dt)

	def on_mouse_down(self, pos, button):
		for
