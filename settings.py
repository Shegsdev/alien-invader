class Settings:
	"""To store all game settings"""

	def __init__(self):
		"""Initialize game settings"""
		# screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0, 0, 255)
		self.bullets_allowed = 50

		# ship settings
		self.ship_limit = 3

		# bullet settings
		self.bullet_width = 10
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)

		# alien settings
		self.fleet_drop_speed = 10

		# game settings
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change through the game"""
		self.ship_speed = 3.5
		self.bullet_speed = 2.5
		self.alien_speed = 1.0

		self.fleet_direction = 1 # 1 represents right; -1 represents left


	def increase_speed(self):
		"""Increase speed setting"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

