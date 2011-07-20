# Builder
""" This module stores all of the classes necessary to the building of the actual character file.
    It has the part class, and not much else at the moment. """

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
			'template': None,
			'head': {
				'eyeL': None,
				'eyeR': None,
				'mouth': None,
				'hair': None,
				'misc': [None,None,None,None]
				},
			'body': {
				'top': None,
				'handL': None,
				'handR': None,
				'bottom': None,
				'footL': None,
				'footR': None,
				'misc': [None,None,None,None]
				},
			'accessories': [None,None,None,None,None,None,None,None]}
	
	def swapParts(self, part, subpart, newval, subindex=0):
		pass
	