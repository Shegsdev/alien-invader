class Settings:
	"""To store all game settings"""

	def __init__(self):
		"""Initialize game settings"""
		# screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0, 0, 255)

		# ship settings
		self.ship_speed = 1.5
