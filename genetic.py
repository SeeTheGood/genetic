import random 

from phrase import Phrase, target 
from helpers import summarize
from helpers import summarize

popSize = 1000000
population = []
bestScore = 0
generation = 1

for i in range(popSize):
    population.append(Phrase())

# keep going until we find the target
while bestScore < len(target):

    for i in range (popSize):
        population[i].getFitness()
    
        if population[i].getFitness() > bestScore:
            bestScore = population[i].fitness
            summarize(generation, population[i].getContents(), bestScore)

        matingPool = []
        for parent in population:
            fitness = parent.getFitness()
            if fitness > bestScore:
                for _ in range(fitness):
                    matingPool.append(parent)

        #debug print size of mating pool
        print(f"Generation {generation}: Mating pool size = {len(matingPool)}")

        #Check if mating pool is empty
        if not matingPool:
            raise ValueError("Mating pool is empty. Check fitness calculation.")
        

        new_population = []
        
        # for each one of the parents, add it to the mating pool when its fitness higher 

        parents = population.copy()

        for i in range(len(parents)):
            parents[i].getFitness()
        for j in range(parents[i].fitness):
            matingPool.append(parents[i])

        for i in range(popSize):
            x = random.choice(matingPool)
            y = random.choice(matingPool)

            child = x.crossover(y)
            child = child.mutate(generation)

            population [i]= child

        generation += 1





    
