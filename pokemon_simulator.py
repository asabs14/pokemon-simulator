from pokemon_type import PokemonType
from pokemon import Pokemon
from trainer import Trainer
  
fire = PokemonType("Fire", ["Grass"], ["Water"])
water = PokemonType("Water", ["Fire"], ["Grass"])
grass = PokemonType("Grass", ["Water"], ["Fire"])
        
charmander = Pokemon("Charmander", 17, fire, 170, False)
squirtle = Pokemon("Squirtle", 20, water, 200, False)
bulbasaur = Pokemon("Bulbasaur", 18, grass, 180, False)

alex = Trainer("Alex", [charmander, bulbasaur], 2, 0)
gary = Trainer("Gary", [squirtle], 1, 0)

alex.attack_trainer(gary)