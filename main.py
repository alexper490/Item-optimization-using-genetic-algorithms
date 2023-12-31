from typing import List
from random import choices
from random import namedtuple #revisit!!!!!!!!!!!

Genome = List[int]
Population = List[Genome]
Item = namedtuple('Item', ['name', 'value', 'weight'])

#  --- Your items ---

items = [
   Item('Laptop', 500, 2200),
   Item('Headphones', 150, 160),
   Item('Coffee Mug', 60, 350),
   Item('Notepad', 40, 333),
   Item('Water Bottle', 30,192),
]


more_items = [
   Item('Mints', 500, 2200),
   Item('Socks', 150, 160),
   Item('Tissues', 60, 350),
   Item('Phone', 40, 333),
   Item('Baseball Cap', 30,192),
] + items

# --- Genom, population, and fitness functions ---

def generate_genome(length:int) -> Genome:
   return choices([0,1], k=length)

def generate_population(size: int, genome_length: int) -> Population:
   return [generate_genome(genome_length) for _ in range(size)]

def fitness(genome: Genome, items: [Item], weight_limit: int) -> int:
   if len(genome) != len(items):
      raise ValueError("Genome and items must be same length")
   
   weigh = 0
   value = 0

   for i, item in enumerate(items):
      if genome[1] == 1:
         weight += item.weight
         value += item.value

         if weight > weight_limit:
            return 0
         
   return value




#  --built from Kie Codes--