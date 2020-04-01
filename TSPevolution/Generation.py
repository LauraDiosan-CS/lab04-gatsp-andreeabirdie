from random import randint

from Chromosome import Chromosome


class Generation:

    def __init__(self, populationSize, weights, nrCities):
        self.__populationSize = populationSize
        self.__weights = weights
        self.__population = []
        self.__nrCities = nrCities

    def evaluate(self, c):
        totalWeight = 0
        repr = c.__getattribute__("repres")
        for i in range(len(repr) - 1):
            totalWeight += self.__weights[repr[i]][repr[i + 1]]
        totalWeight += self.__weights[repr[len(repr) - 1]][repr[0]]
        return totalWeight

    def initializePopulation(self):
        for i in range(self.__populationSize):
            c = Chromosome(self.__nrCities)
            c.__setattr__("fitness", self.evaluate(c))
            self.__population.append(c)

    def getPopulation(self):
        return self.__population

    def setPopulation(self, pop):
        self.__population = pop

    def bestIndividual(self):
        individual = self.__population[0]
        for i in range(1, len(self.__population)):
            enemy = self.__population[i]
            if enemy.__getattribute__("fitness") < individual.__getattribute__("fitness"):
                individual = enemy
        return individual

    def worstIndividual(self):
        individual = self.__population[0]
        for i in range(1, len(self.__population)):
            enemy = self.__population[i]
            if enemy.__getattribute__("fitness") > individual.__getattribute__("fitness"):
                individual = enemy
        return individual

    def evolveElite(self):
        best =None
        for i in range(self.__populationSize):
            mom = self.__population[randint(0, self.__populationSize - 1)]
            dad = self.__population[randint(0, self.__populationSize - 1)]
            if dad.__getattribute__("fitness")< mom.__getattribute__("fitness"):
                mom, dad = dad, mom
            child = mom.crossover(dad)
            child.mutation()
            child.__setattr__("fitness", self.evaluate(child))
            if best is None or child.__getattribute__("fitness") < best.__getattribute__("fitness"):
                best = child
        self.__population.remove(self.worstIndividual())
        self.__population.append(best)

    # def reduceIndividualsElite(self):
    #     randomPos = []
    #     pop = []
    #     pop.append(self.bestIndividual())
    #     while len(randomPos) != self.__populationSize:
    #         pos = randint(0, self.__populationSize - 1)
    #         if pos not in randomPos:
    #             randomPos.append(pos)
    #     for i in range(self.__populationSize):
    #         pop.append(self.__population[randomPos[i]])
    #     self.setPopulation(pop)
    #
    # def evolveElite(self):
    #     self.crossovers()
    #     self.reduceIndividualsElite()
