from HeuristicApproach_Stochastic import *
import copy

def AISforFLDCP(MaxItr = 50, cloneNum = 10, popSize = 10, ProblemName = None):
    # Read problem
    Capacities, Demands, FixedCosts, TransPortationCosts = ReadProblem(ProblemName)
    # Generate a population of T-cells (Solutions)
    population = [solStucture(Demands, Capacities) for _ in range(popSize)]
    # Matching procedure (Evaluation)
    Evalution = np.array([i.Evaluate(TransPortationCosts, FixedCosts) for i in population])
    # Keep an elitism that saves the best T-cell (best solution) 
    BestEval = np.min(Evalution)
    BestSol = population[np.argmin(Evalution)]
    # T-cells migration process from thymus and bone marrow
    for Itr in range(MaxItr):
        for i in range(popSize):
            # The cloning process
            for _ in range(cloneNum):
                # Affinity maturation
                # population[i] = population[i] + np.random.uniform() *(BestSol - population[i])
                population[i].DistCenterArray = population[i].DistCenterArray + np.random.uniform() * \
                (BestSol.DistCenterArray - population[i].DistCenterArray)
                population[i].PlantArray = population[i].PlantArray + np.random.uniform() * \
                (BestSol.PlantArray - population[i].PlantArray)
                Evalution[i] = population[i].Evaluate(TransPortationCosts, FixedCosts)
                if Evalution[i]<=BestEval:
                    BestEval = Evalution[i]
                    BestSol = copy.deepcopy(population[i])
        population = [solStucture(Demands, Capacities) for _ in range(popSize)]
    return BestEval, BestSol
