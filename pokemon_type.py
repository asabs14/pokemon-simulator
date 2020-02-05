class PokemonType:
  def __init__(self, name, weaknesses, resistances):
    self.name = name
    self.weaknesses = weaknesses
    self.resistances = resistances
    
  def __repr__(self):
    return self.name
  
  def is_strong_against(self, other):
    return other.name in self.weaknesses
    
  def is_weak_against(self, other):
    return other.name in self.resistances
  
  def get_multiplier(self, other):
    if self.is_strong_against(other):
      return 2
    elif self.is_weak_against(other):
      return 0.5
    else:
      return 1