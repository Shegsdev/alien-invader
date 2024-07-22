class Settings:
	"""To store all game settings"""

	def __init__(self):
		"""Initialize game settings"""
		# screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0, 0, 255)
		self.bullets_allowed = 3

		# ship settings
		self.ship_speed = 1.5

		# bullet settings
		self.bullet_speed = 2.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)

		# alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		self.fleet_direction = 1 # 1 represents right; -1 represents left
