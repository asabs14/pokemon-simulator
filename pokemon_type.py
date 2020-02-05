# A class representing Pokemon types
class PokemonType:
  def __init__(self, name, weaknesses, resistances):
    self.name = name
    self.weaknesses = weaknesses
    self.resistances = resistances
    
  def __repr__(self):
    return self.name
  
  # The type is super effective against these types
  def is_strong_against(self, other):
    return other.name in self.weaknesses

  # The type is not very effective against these types  
  def is_weak_against(self, other):
    return other.name in self.resistances
  
  # Method to determine how effective the type is against another type
  def get_multiplier(self, other):
    if self.is_strong_against(other):
      return 2
    elif self.is_weak_against(other):
      return 0.5
    else:
      return 1