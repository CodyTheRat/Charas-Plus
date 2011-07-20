# Builder
# This module stores all of the classes necessary to the building of the actual character file.
# It has the part class, the list manager, 

class CharacterPart:
	""" Class that will contain metadata, which will be decided at a later point! """
	def __init__(self):
		pass

class Character:
	""" Class that contains part data for the character. The builder reads off of this and then
		constructs the character image. """
	
	def __init__(self):
		self.parts = {
			# Stores part instances for later access.
			# Lists indicate layers, from deepest to highest.
			'template': 0,
			'head': {
				'eyeL': 0,
				'eyeR': 0,
				'mouth': 0,
				'hair': 0,
				'misc': [0,0,0,0]
				},
			'body': {
				'top': 0,
				'handL': 0,
				'handR': 0,
				'bottom': 0,
				'footL': 0,
				'footR': 0,
				'misc': [0,0,0,0]
				},
			'accessories': [0,0,0,0,0,0,0,0]}
	
	def swapParts(self, part, subpart, newval, subindex=0):
		if subpart == 'misc':
			self.parts[part][subpart] = newval
		else:
			self.parts[part][subpart][subindex] = newval