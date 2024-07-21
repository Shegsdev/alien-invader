import sys

import pygame
from settings import Settings

class AlienInvasion:
	"""Manage game assets and behaviour"""

	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

	def run_game(self):
		"""Start game loop"""
		while True:
			# watch for keyboard and mouse events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# redraw screen
			self.screen.fill(self.settings.bg_color)

			# display drawn screen
			pygame.display.flip()
			self.clock.tick(60)


if __name__ == "__main__":
	ai = AlienInvasion()
	ai.run_game()