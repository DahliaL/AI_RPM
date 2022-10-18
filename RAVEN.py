import random
from const import TYPE_VALUES as tv, COLOR_VALUES as cv, SIZE_VALUES as sv

scenes = [1, 2, 3]
structures = [4, 5, 6]
components = [7, 8, 9] 
layouts = [10, 11, 12]
entities = [13, 14, 15]

class Entity:
  def __init__(self):
    self.type = random.choice(tv) # shape
    self.color = random.choice(cv) # greyscale value
    self.size = random.choice(sv)

  def randomizeValues(self):
    self.type = random.choice(tv) # shape
    self.color = random.choice(cv)
    self.size = random.choice(sv)
    
  def getType(self):
    return self.type
    
  def getColor(self):
    return self.color
    
  def getSize(self):
    return self.size

class RAVEN:
  def __init__(self, name):
        self.name = name
        self.scene = ''
        self.structure = ''
        self.component= ''
        self.layout = ''
        self.entity = ''

  def randomizeValues(self): 
    # RANDOM SELECTION
    self.scene = random.choice(scenes)
    self.structure = random.choice(structures)
    self.component = random.choice(components)
    self.layout = random.choice(layouts)
    self.entity = random.choice(entities)
# should look into how random random choice actually is....
    
  def getStructure(self):
    return self.structure

  def getScene(self):
    return self.scene

  def getComponent(self):
    return self.component

  def getLayout(self):
    return self.layout

  def getEntity(self):
    return self.entity