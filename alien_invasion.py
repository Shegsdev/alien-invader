import sys
from time import sleep

import pygame
from ship import Ship
from alien import Alien
from bullet import Bullet
from button import Button
from settings import Settings
from game_stats import GameStats

class AlienInvasion:
	"""Manage game assets and behaviour"""

	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.game_active = False
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")

		self.play_button = Button(self, "Play")

		# handle game statistics
		self.stats = GameStats(self)

		self.ship = Ship(self)
		self.aliens = pygame.sprite.Group()
		self.bullets = pygame.sprite.Group()

		self._create_fleet()

	def run_game(self):
		"""Start game loop"""
		while True:
			self._check_events()

			if self.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()

			self._update_screen()
			self.clock.tick(60)

	def _check_events(self):
		# respond to keypresses and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_play_button(self, mouse_pos):
		"""start new game when player clicks play"""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.game_active:
			# reset game settings
			self.settings.initialize_dynamic_settings()

			# hide cursor
			pygame.mouse.set_visible(False)

			self.stats.reset_stats()
			self.game_active = True

			self.bullets.empty()
			self.aliens.empty()
			self._create_fleet()
			self.ship.center_ship()

	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		# create new bullet and add it to the bullets group
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _create_fleet(self):
		# create the fleet of aliens
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size

		current_x, current_y = alien_width, alien_height
		while current_y < (self.settings.screen_height - 16 * alien_height):
			while current_x < (self.settings.screen_width - 2 * alien_width):
				self._create_alien(current_x, current_y)
				current_x += 2 * alien_width

			current_x = alien_width
			current_y += 2 * alien_height

	def _create_alien(self, x_position, y_position):
		new_alien = Alien(self)
		new_alien.x = x_position
		new_alien.rect.x = x_position
		new_alien.rect.y = y_position
		self.aliens.add(new_alien)

	def _check_fleet_edges(self):
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _update_screen(self):
		# update assets on the screen, and flip to new screen
		self.screen.fill(self.settings.bg_color)
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.ship.blitme()
		self.aliens.draw(self.screen)

		# draw the play button if the game is inactive
		if not self.game_active:
			self.play_button.draw_button()

		# display drawn screen
		pygame.display.flip()

	def _update_bullets(self):
		# update position of bullets
		self.bullets.update()

		# get rid of bullets that are off the screen
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()

	def _update_aliens(self):
		self._check_fleet_edges()
		self.aliens.update()

		# handle alien-ship collisions
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

		# handle aliens hitting the bottom of the screen
		self._check_aliens_bottom()

	def _check_bullet_alien_collisions(self):
		# check for aliens hit by a bullet
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)

		if not self.aliens:
			# destroy existing bullets and create new fleet
			self.bullets.empty()
			self._create_fleet()
			self.settings.increase_speed()

	def _ship_hit(self):
		# respond to ship being hit by alien
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1

			self.bullets.empty()
			self.aliens.empty()

			self._create_fleet()
			self.ship.center_ship()

			sleep(0.5)
		else:
			self.game_active = False
			pygame.mouse.set_visible(True)

	def _check_aliens_bottom(self):
		# check if any aliens have reached the bottom of the screen
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= self.settings.screen_height:
				# same as if ship got hit
				self._ship_hit()
				break

if __name__ == "__main__":
	ai = AlienInvasion()
	ai.run_game()