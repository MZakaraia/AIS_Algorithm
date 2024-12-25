# from HeuristicApproach_Stochastic import *
# import copy

# def AISforFLDCP(MaxItr = 50, cloneNum = 10, popSize = 10, ProblemName = None):
#     # Read problem
#     Capacities, Demands, FixedCosts, TransPortationCosts = ReadProblem(ProblemName)
#     # Generate a population of T-cells (Solutions)
#     population = [solStucture(Demands, Capacities) for _ in range(popSize)]
#     # Matching procedure (Evaluation)
#     Evalution = np.array([i.Evaluate(TransPortationCosts, FixedCosts) for i in population])
#     # Keep an elitism that saves the best T-cell (best solution) 
#     BestEval = np.min(Evalution)
#     BestSol = population[np.argmin(Evalution)]
#     # T-cells migration process from thymus and bone marrow
#     for Itr in range(MaxItr):
#         for i in range(popSize):
#             # The cloning process
#             for j in range(cloneNum):
#                 alpha = 1 - j/cloneNum
#                 # Affinity maturation
#                 # population[i] = population[i] + np.random.uniform() *(BestSol - population[i])
#                 population[i].DistCenterArray = population[i].DistCenterArray + alpha * \
#                 (BestSol.DistCenterArray - population[i].DistCenterArray)
#                 population[i].PlantArray = population[i].PlantArray + alpha * \
#                 (BestSol.PlantArray - population[i].PlantArray)
#                 Evalution[i] = population[i].Evaluate(TransPortationCosts, FixedCosts)
#                 if Evalution[i]<=BestEval:
#                     BestEval = Evalution[i]
#                     BestSol = copy.deepcopy(population[i])
#         population = [solStucture(Demands, Capacities) for _ in range(popSize)]
#         Evalution = np.array([i.Evaluate(TransPortationCosts, FixedCosts) for i in population])

#     return BestEval, BestSol

# import numpy as np
# import copy
# from HeuristicApproach_Stochastic import ReadProblem, solStucture
# dist = lambda x,y:np.sqrt((x-y)**2).sum()

# def AISforFLDCP(MaxItr=50, cloneNum=10, popSize=10, ProblemName=None, ChanceProbability = 0.6):
#     # Read problem data
#     Capacities, Demands, FixedCosts, TransPortationCosts = ReadProblem(ProblemName)

#     # Generate initial population
#     population = [solStucture(Demands, Capacities, ChanceProbability) for _ in range(popSize)]
#     evaluations = np.array([ind.Evaluate(TransPortationCosts, FixedCosts) for ind in population])

#     # Elitism: Track best solution
#     best_eval = np.min(evaluations)
#     best_sol = copy.deepcopy(population[np.argmin(evaluations)])
#     ConvergenceCurve = np.array([best_eval])
#     ConvergenceCurve0 = np.array([best_eval])
#     labels = ['0_0']
#     # Main AIS loop
#     for itr in range(MaxItr):
#         alpha = itr / MaxItr
#         # Clone and mature each solution
#         for i, individual in enumerate(population):
#             cloned_ind = copy.deepcopy(individual)
#             for j in range(cloneNum):
                
#                 # Generate mutated clones
                
#                 cloned_ind.DistCenterArray += alpha * (best_sol.DistCenterArray - population[i].DistCenterArray)
#                 cloned_ind.PlantArray += alpha * (best_sol.PlantArray - population[i].PlantArray)
#                 cloned_eval = cloned_ind.Evaluate(TransPortationCosts, FixedCosts)
                
#                 # Update if clone is better
#                 if cloned_eval < evaluations[i]:
#                     population[i] = copy.deepcopy(cloned_ind)
#                     evaluations[i] = cloned_eval
                
#                 # Update global best
#                 if cloned_eval < best_eval:
#                     best_eval = cloned_eval
#                     best_sol = copy.deepcopy(cloned_ind)
#                     ConvergenceCurve = np.append(ConvergenceCurve, best_eval)
#                     labels.append(str(itr)+'_'+ str(i) +'_'+ str(j))        
#         # Replace weakest solutions to maintain diversity
#         # new_population = [solStucture(Demands, Capacities) for _ in range(popSize)]
#         # weak_indices = np.argsort(evaluations)[-popSize:]
#         # for idx in weak_indices:
#         #     population[idx] = new_population.pop(0)
#         #     evaluations[idx] = population[idx].Evaluate(TransPortationCosts, FixedCosts)
#     ConvergenceCurve0 = np.append(ConvergenceCurve0, best_eval)
#     population = [solStucture(Demands, Capacities, ChanceProbability) for _ in range(popSize)]
#     evaluations = np.array([ind.Evaluate(TransPortationCosts, FixedCosts) for ind in population])

    # return best_eval, best_sol, ConvergenceCurve, labels, # from HeuristicApproach_Stochastic import *
# import copy

# def AISforFLDCP(MaxItr = 50, cloneNum = 10, popSize = 10, ProblemName = None):
#     # Read problem
#     Capacities, Demands, FixedCosts, TransPortationCosts = ReadProblem(ProblemName)
#     # Generate a population of T-cells (Solutions)
#     population = [solStucture(Demands, Capacities) for _ in range(popSize)]
#     # Matching procedure (Evaluation)
#     Evalution = np.array([i.Evaluate(TransPortationCosts, FixedCosts) for i in population])
#     # Keep an elitism that saves the best T-cell (best solution) 
#     BestEval = np.min(Evalution)
#     BestSol = population[np.argmin(Evalution)]
#     # T-cells migration process from thymus and bone marrow
#     for Itr in range(MaxItr):
#         for i in range(popSize):
#             # The cloning process
#             for j in range(cloneNum):
#                 alpha = 1 - j/cloneNum
#                 # Affinity maturation
#                 # population[i] = population[i] + np.random.uniform() *(BestSol - population[i])
#                 population[i].DistCenterArray = population[i].DistCenterArray + alpha * \
#                 (BestSol.DistCenterArray - population[i].DistCenterArray)
#                 population[i].PlantArray = population[i].PlantArray + alpha * \
#                 (BestSol.PlantArray - population[i].PlantArray)
#                 Evalution[i] = population[i].Evaluate(TransPortationCosts, FixedCosts)
#                 if Evalution[i]<=BestEval:
#                     BestEval = Evalution[i]
#                     BestSol = copy.deepcopy(population[i])
#         population = [solStucture(Demands, Capacities) for _ in range(popSize)]
#         Evalution = np.array([i.Evaluate(TransPortationCosts, FixedCosts) for i in population])

#     return BestEval, BestSol

import numpy as np
import copy
from HeuristicApproach_Stochastic import ReadProblem, solStucture
dist = lambda x,y:np.sqrt((x-y)**2).sum()

def AISforFLDCP(MaxItr=50, cloneNum=10, popSize=10, ProblemName=None, ChanceProbability = 0.6):
    # Read problem data
    Capacities, Demands, FixedCosts, TransPortationCosts = ReadProblem(ProblemName)

    # Generate initial population
    population = [solStucture(Demands, Capacities, ChanceProbability) for _ in range(popSize)]
    evaluations = np.array([ind.Evaluate(TransPortationCosts, FixedCosts) for ind in population])

    # Elitism: Track best solution
    best_eval = np.min(evaluations)
    best_sol = copy.deepcopy(population[np.argmin(evaluations)])
    ConvergenceCurve = np.array([best_eval])
    # ConvergenceCurve0 = np.array([best_eval])
    labels = [[0, 0, 0]]
    # Main AIS loop
    for itr in range(MaxItr):
        alpha = itr / MaxItr
        # Clone and mature each solution
        for i, individual in enumerate(population):
            cloned_ind = copy.deepcopy(individual)
            for j in range(cloneNum):
                
                # Generate mutated clones
                
                cloned_ind.DistCenterArray += alpha * (best_sol.DistCenterArray - population[i].DistCenterArray)
                cloned_ind.PlantArray += alpha * (best_sol.PlantArray - population[i].PlantArray)
                cloned_eval = cloned_ind.Evaluate(TransPortationCosts, FixedCosts)
                
                # Update if clone is better
                if cloned_eval < evaluations[i]:
                    population[i] = copy.deepcopy(cloned_ind)
                    evaluations[i] = cloned_eval
                
                # Update global best
                if cloned_eval < best_eval:
                    best_eval = cloned_eval
                    best_sol = copy.deepcopy(cloned_ind)
                    # ConvergenceCurve = np.append(ConvergenceCurve, best_eval)
                    if itr > labels[0][0] or i > labels[0][1] or j > labels[0][2]:
                        labels= [[itr+1, i+1 , j+1]]
        # Replace weakest solutions to maintain diversity
        # new_population = [solStucture(Demands, Capacities) for _ in range(popSize)]
        # weak_indices = np.argsort(evaluations)[-popSize:]
        # for idx in weak_indices:
        #     population[idx] = new_population.pop(0)
        #     evaluations[idx] = population[idx].Evaluate(TransPortationCosts, FixedCosts)
        ConvergenceCurve = np.append(ConvergenceCurve, best_eval)
        population = [solStucture(Demands, Capacities, ChanceProbability) for _ in range(popSize)]
        evaluations = np.array([ind.Evaluate(TransPortationCosts, FixedCosts) for ind in population])

    return best_eval, best_sol, labels, ConvergenceCurve

