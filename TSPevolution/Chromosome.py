from random import randint


def getNum(v):
    # Size of the vector
    n = len(v)

    # Generate a random number within
    # the index range
    index = randint(0, n - 1)

    # Get random number from the vector
    num = v[index]

    # Remove the number from the vector
    v[index], v[n - 1] = v[n - 1], v[index]
    v.pop()

    # Return the removed number
    return num


# Function to generate n non-repeating
# random numbers
def generateRandom(n):
    v = [0] * n
    # Fill the vector with the values
    # 1, 2, 3, ..., n
    for i in range(n):
        v[i] = i
    perm = [0] * n
    i = 0
    while (len(v)):
        perm[i] = getNum(v)
        i += 1
    return perm


# permutation-based representation
class Chromosome:
    def __init__(self, nrCities):  # problParam has to store the number of nodes/cities
        self.__nrCities = nrCities
        self.__repres = generateRandom(nrCities)
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit):
        self.__fitness = fit

    def crossover(self, c):
        newrepres = [-1] * self.__nrCities
        pos1 = randint(-1, self.__nrCities - 1)
        pos2 = randint(-1, self.__nrCities - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        k = 0
        for i in range(pos1, pos2 + 1):
            newrepres[i] = self.__repres[i]
        unused = []
        for el in c.__repres:
            if el not in newrepres:
                    unused.append(el)
        for i in range(self.__nrCities):
            if newrepres[i] == -1:
                newrepres[i] = unused[0]
                unused.remove(unused[0])
        offspring = Chromosome(self.__nrCities)
        offspring.__setattr__("repres", newrepres)
        return offspring

    def mutation(self):
        # swap mutation
        pos1 = randint(0, self.__nrCities - 1)
        pos2 = randint(0, self.__nrCities - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        el = self.__repres[pos2]
        self.__repres[pos2] = self.__repres[pos1]
        self.__repres[pos1] = el

    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
