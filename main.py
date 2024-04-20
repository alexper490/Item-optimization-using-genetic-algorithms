from typing import List, Callable, Tuple
from random import choices, randint, randrange, random
from collections import namedtuple

Genome = List[int]
Population = List[Genome]
FitnessFunc = Callable[[Genome], int]
PopulateFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]
Item = namedtuple('Item', ['name', 'value', 'weight'])

#  --- Your items ---

items = [
   Item('Laptop', 500, 2200),
   Item('Headphones', 150, 160),
   Item('Coffee Mug', 60, 350),
   Item('Notepad', 40, 333),
   Item('Water Bottle', 30,192),
]

# --- More items ---

more_items = [
   Item('Mints', 500, 2200),
   Item('Socks', 150, 160),
   Item('Tissues', 60, 350),
   Item('Phone', 40, 333),
   Item('Baseball Cap', 30,192),
] + items

# --- Genome, Population, And Fitness Functions ---

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

# --- Crossover Function ---

def selection_pair(population: Population, fitness_func: FitnessFunc) -> Population:
   return choices(
      population=population,
      weights=[fitness_func(genome) for genome in population],
      k=2
   )

def single_point_crossover(a:Genome, b: Genome) -> Tuple[Genome, Genome]:
   if len(a) != len(b):
      raise ValueError("Genomes a and b must be the same length")
   length = len(a)
   if length < 2:
      return a, b
   p = randint(1, length -1)
   return a[0:p] + b[p:], b[0:p] + a[p:]

# --- Mutation Function ---

def mutation(genome: Genome, num: int = 1, probabilty: float = 0.5) -> Genome:
   for _ in range(num):
      index = randrange(len(genome))
      genome[index] = genome[index] if random() > probabilty else abs(genome[index] - 1)
      return genome
   

# --- Evolutionary Main Loop ---
   

def run_evolution(
      populate_func: PopulateFunc,
      fitness_func: FitnessFunc,
      fitness_limit: int,
      selection_func: SelectionFunc = selection_pair,
      crossover_func: CrossoverFunc = single_point_crossover,
      mutation_func: MutationFunc = mutation,
      generation_limit: int = 100
) -> Tuple[Population, int]:
   

#  --built from Kie Codes