# Preview Renderer


import pygame

class PartDirectory:
    """ Class that will contain lists of instances of characterPart, which contains metadata and image strings of 
    part bitmaps. """
    def __init__(self):
        self.parts = {'eyes': [],
                      'mouths': [],
                      'hairs': [],
                      'head_misc': [],
                      'tops': [],
                      'hands': [],
                      'bottoms': [],
                      'feet': [],
                      'body_misc': [],
                      'accessories': []}
    
    def addPart(self, part_type, part_instance):
        pass

class CharacterPart:
    """Class that contains metadata, as well as image strings."""
    def __init__(self, surf, category):
        self.size = surf.get_size()
        self.image = pygame.image.tostring(surf, 'RGBA')
        self.category = category

class Character:
    """ Class that contains part data for the character. The builder reads off of this and then
    constructs the character image. """
    
    def __init__(self):
        self.parts = {
            # Stores part indices for later access
            # Lists indicate layers, from deepest to highest.
            'template': None,
            'head': {'eye_l': None,
                     'eye_r': None,
                     'mouth': None,
                     'hair': None,
                     'misc': [None,None,None,None] },
            'body': {'top': None,
                     'hand_l': None,
                     'hand_r': None,
                     'bottom': None,
                     'foot_l': None,
                     'foot_r': None,
                     'misc': [None,None,None,None] },
            'accessories': [None,None,None,None,None,None,None,None]}
    
    def SwapParts(self, part, subpart, newval, layer=0):
        pass
    

class CharacterRenderer:
    def __init__(self):
        character = Character()