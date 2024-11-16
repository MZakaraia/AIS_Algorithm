# Clonal selection algorithm
try:
    np  
except:
    import numpy as np

def AIS(MaxItr = 100, cloneNum = 20, popSize = 100, Fn = None, LB = -10, UB = 10, dim = 100):
    population = np.random.uniform(LB, UB, (popSize, dim))
    Evalution = np.array([Fn(i) for i in population])
    BestEval = np.min(Evalution)
    BestSol = population[np.argmin(Evalution)]
    for Itr in range(MaxItr):
        # The cloning process
        for i in range(popSize):
            for _ in range(cloneNum):
                population[i] = population[i] + np.random.uniform() *(BestSol - population[i])
                Evalution[i] = Fn(population[i])
                if Evalution[i]<=BestEval:
                    BestEval = Evalution[i]
                    BestSol = population[i]
        population = np.random.uniform(LB, UB, (popSize, dim))