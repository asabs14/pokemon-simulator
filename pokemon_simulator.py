from pokemon_type import PokemonType
from pokemon import Pokemon
from trainer import Trainer

# Type instantiations
fire = PokemonType("Fire", ["Grass"], ["Water"])
water = PokemonType("Water", ["Fire"], ["Grass"])
grass = PokemonType("Grass", ["Water"], ["Fire"])

# Pokemon instantiations        
charmander = Pokemon("Charmander", 17, fire, 170, False)
squirtle = Pokemon("Squirtle", 20, water, 200, False)
bulbasaur = Pokemon("Bulbasaur", 18, grass, 180, False)

# Trainer instantiations
alex = Trainer("Alex", [charmander, bulbasaur], 2, 0)
gary = Trainer("Gary", [squirtle], 1, 0)

# Main game
alex.attack_trainer(gary)