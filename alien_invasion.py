import sys

import pygame

class AlienInvasion:
	"""Manage game assets and behaviour"""

	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()

		self.screen = pygame.display_set_mode((1200, 800))
		pygame.display_set_caption("Alien Invasion")

	def run_game(self):
		"""Start game loop"""
		while True:
			# watch for keyboard and mouse events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# display drawn screen
			pygame.display.flip()
			self.clock.tick(60)


if __name__ == "__main__":
	ai = AlienInvasion()
	ai.run_game()