class Settings():
	"""A class to store all the settings for alien invasion"""
	def __init__(self):
		"""Initialize the games static settings"""
		# screen settings
		self.screen_width = 800
		self.screen_height = 600

		# holds the tile width and height
		self.tileWidth = 64
		self.tileHeight = 64
		self.height_modifier = 5
