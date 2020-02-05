# A class representing a Pokemon
class Pokemon:
  def __init__(self, name, level, poke_type, health, is_knocked_out):
    self.name = name
    self.level = level
    self.type = poke_type
    self.max_health = level * 10
    self.health = health
    self.is_knocked_out = is_knocked_out
     
  def knockout(self):
    self.is_knocked_out = True
    print("{} is knocked out!".format(self.name))
  
  def revive(self):
    self.is_knocked_out = False
    print("{} has been revived!".format(self.name))
    
  def lose_health(self, value):
    self.health -= value
    self.health = min(self.health, 0)
    print("{} now has {} health".format(self.name, self.health))
    if self.health <= 0:
      self.knockout()
      
  def gain_health(self, value):
    if self.is_knocked_out:
      print("{} is knocked out and cannot be healed...".format(self.name))
    self.health += value
    self.health = min(self.health, self.max_health)
    print("{} now has {} health".format(self.name, self.health))
    
  def attack(self, other):
    multiplier = self.type.get_multiplier(other.type)
    if multiplier == 2:
      print("Super effective!")
    elif multiplier == 0.5:
      print("Not very effective...")
    health_lost = self.level * multiplier
    print("{} lost {} HP from {}'s attack!".format(other.name, health_lost, self.name))
    other.lose_health(health_lost)