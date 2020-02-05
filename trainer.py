# A class representing a Trainer having at most 6 pokemon (this is a game limitation, not a code limitation)
class Trainer:
  def __init__(self, name, pokemons, potion_cnt, active_pokemon_index=0):
    self.name = name
    self.pokemons = pokemons
    self.potion_cnt = potion_cnt
    if active_pokemon_index >= len(pokemons):
      active_pokemon_index = 0
    self.active_pokemon_index = active_pokemon_index
    
  def switch_active_pokemon(self, pokemon_index):
      if pokemon_index >= len(self.pokemons):
        print("Invalid pokemon")
        return False
      elif self.pokemons[pokemon_index].is_knocked_out:
        print("Pokemon is knocked out. Select another")
        return False
      else:
        self.active_pokemon_index = pokemon_index
        return True
    
  def use_potion(self):
    if self.potion_cnt <= 0:
      print("No more potions remaining...")
      return
    self.potion_cnt -= 1
    self.pokemons[self.active_pokemon_index].gain_health(20)
    print("{} potions remaining".format(self.potion_cnt))

  # Attack another Trainer's active pokemon with this Trainer's active pokemon
  def attack_trainer(self, other):
    self_index = self.active_pokemon_index
    other_index = other.active_pokemon_index
    self.pokemons[self_index].attack(other.pokemons[other_index])
    if other.pokemons[other_index].is_knocked_out:
      other.active_pokemon_index = 0
      print("Checking for next available pokemon...")
      while not other.switch_active_pokemon(other.active_pokemon_index):
        if other.active_pokemon_index >= len(other.pokemons) - 1:
          print("{} has no more pokemon available...{} wins!".format(other.name, self.name))
          break
        other.active_pokemon_index += 1