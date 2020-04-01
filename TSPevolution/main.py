from Generation import Generation


f = open("hard_02_52.txt", "r")
#f = open("medium.txt", "r")
nrCities = int(f.readline())
weight = []
for i in range(nrCities):
    line = f.readline()
    numbers = [int(n) for n in line.split(",")]
    weight.append(numbers)
# sourceCity = int(f.readline())
# destinationCity = int(f.readline())
f.close()



def simulate():
    populationSize = 150

    ga = Generation(populationSize, weight, nrCities)
    ga.initializePopulation()
    print('________________generation 1______________')
    sol = ga.bestIndividual()
    print('Best fitness this generation: ' + str(sol.__getattribute__("fitness")))
    print('Best fitness: ' + str(sol.__getattribute__("fitness")))
    bestFitnessEver = sol.__getattribute__("fitness")
    bestFor = 1
    genNo = 2
    while bestFor != 100:
        ga.evolveElite()
        sol = ga.bestIndividual()
        if sol.__getattribute__("fitness") < bestFitnessEver:
            bestFitnessEver = sol.__getattribute__("fitness")
            bestFor = 1
        else:
            bestFor += 1
        print('________________generation '+str(genNo+1)+'______________')
        print('Best fitness this generation: ' + str(sol.__getattribute__("fitness")))
        print('Best fitness: ' + str(bestFitnessEver))
        genNo += 1

    print(nrCities)
    solution = sol.__getattribute__("repres")
    for i in range(len(solution)):
        print(solution[i]+1, end=' ')
    print()
    print(str(sol.__getattribute__("fitness")))

simulate()
