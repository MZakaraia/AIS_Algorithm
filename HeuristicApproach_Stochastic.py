try:
    np
except:
    import numpy as np
try:
    pd
except:
    import pandas as pd
try:
    stat
except:
    import scipy.stats as stat
def GenerateProblems(NumberOfProblems = 10, MinTransCost = 30, MaxTransCost = 80, MinFixedCost = 70, MaxFixedCost = 120\
                     , NumberOFDistCenter = 10, NumberOfPlants = 5, MinDemand = 20,  MaxDemand = 50):
    for i in range(NumberOfProblems):
        ProblemName = 'ProblemStochastic ' + str(NumberOFDistCenter)+ 'X'+ str(NumberOfPlants) + '_' + f"{i+1:02}" + '.xlsx'
        pd.DataFrame(np.random.randint(MinTransCost, MaxTransCost,(NumberOFDistCenter, NumberOfPlants)),\
                        columns=['Plant ' + str(j+1) for j in range(NumberOfPlants)],\
                        index=['Center ' + str(j+1) for j in range(NumberOFDistCenter)]).to_excel\
                            (ProblemName, sheet_name='Transportation Costs')
        with pd.ExcelWriter(ProblemName, engine='openpyxl', mode='a') as writer:
            pd.DataFrame(np.random.randint(MinFixedCost, MaxFixedCost, NumberOFDistCenter), columns=['Fixed Costs']\
                            , index=['Center '+ str(j+1) for j in range(NumberOFDistCenter)]).to_excel(writer, sheet_name='Fixd Costs')
            ExpectedDemand = np.random.randint(MinDemand, MaxDemand, NumberOfPlants)
            DemandsStd = ExpectedDemand * np.random.uniform(0.1, 0.3)
            DemandsData = np.array([ExpectedDemand, DemandsStd])
            pd.DataFrame(DemandsData.T, columns=['Expected Demand', 'Demand Std'], index=['Plant ' + str(j+1) for j in range(NumberOfPlants)])\
                .to_excel(writer, sheet_name='Demands')
            
            MeanDemand = ExpectedDemand.sum() / NumberOFDistCenter
            Capacities = np.random.randint(MeanDemand, MeanDemand + 100, NumberOFDistCenter)
            pd.DataFrame(Capacities, columns=['Capacity'], index=['Center '+str(j+1) \
                for j in range(NumberOFDistCenter)]).to_excel(writer, sheet_name='Capacities')

##########################################################################
def BubbleSortProcedure(x, y):
    y_length = len(y)
    j = 0
    test = 1
    while(test == 1):
        test = 0
        for i in range(y_length - j - 1):
            if y[i] < y[i+1]:
                temp = y[i]
                temp2 = x[i]
                y[i] = y[i+1]
                x[i] = x[i+1]
                y[i+1] = temp
                x[i+1] = temp2
                test = 1
        j += 1

##########################################################################
def GenerateDemands(Demands, ChanceProbability):
    ZValue = stat.norm.ppf(ChanceProbability)
    return Demands.apply(lambda x: int(x.iloc[0] + ZValue * x.iloc[1]), axis = True).to_numpy()

##########################################################################
def ReadProblem(fileName):
    Capacities = np.array(pd.read_excel(fileName + ".xlsx", sheet_name='Capacities').iloc[:,1])
    Demands = pd.read_excel(fileName + ".xlsx", sheet_name='Demands').iloc[:,1:]
    FixedCosts = np.array(pd.read_excel(fileName + ".xlsx", sheet_name='Fixd Costs').iloc[:,1])
    TransPortationCosts = np.array(pd.read_excel(fileName + ".xlsx", sheet_name='Transportation Costs').iloc[:,1:])
    return Capacities, Demands, FixedCosts, TransPortationCosts

##########################################################################
# class solStucture:
#     def __init__(self, Demands, Capacities, ChanceProbability = 0.95):
#         self.NumberOFDistCenter = len(Capacities)
#         self.NumberOfPlants = len(Demands)
#         # Generate random priorities for both distribution centers and plants
#         self.DistCenterArray = np.random.uniform(0, 1, self.NumberOFDistCenter)
#         self.PlantArray = np.random.uniform(0, 1, self.NumberOfPlants)
#         self.ChanceProbability = ChanceProbability
#         # self.membershipvalue = np.round(np.random.uniform(), 2)

#         self.Demands = Demands
#         self.Capacities = Capacities
#         # self.solution = np.zeros((self.NumberOFDistCenter, self.NumberOfPlants), dtype=int)
    
#     def GenerateSolution(self):
#         self.solution = np.zeros((self.NumberOFDistCenter, self.NumberOfPlants), dtype=int)
#         D = GenerateDemands(self.Demands, self.ChanceProbability)
#         C = self.Capacities.copy()
#         self.D, self.C = D.copy(), C.copy()
#         Centers = list(range(self.NumberOFDistCenter))
#         plants = list(range(self.NumberOfPlants))
#         BubbleSortProcedure(Centers,  self.DistCenterArray.copy())
#         # print(Centers)
#         BubbleSortProcedure(plants,  self.PlantArray.copy())
#         # print(plants)
#         while(len(plants) != 0):
#             plant = plants[0]
#             while(plant in plants):
#                 if D[plant] < C[Centers[0]]:
#                     C[Centers[0]] = C[Centers[0]] - D[plant]
#                     self.solution[Centers[0], plant] = D[plant]
#                     np.delete(D, plant)
#                     del plants[0]
#                 elif D[plant] > C[Centers[0]]:
#                     D[plant] = D[plant] - C[Centers[0]]
#                     self.solution[Centers[0], plant] = C[Centers[0]]
#                     np.delete(C, Centers[0])
#                     del Centers[0]
#                 else:
#                     self.solution[Centers[0], plant] = D[plant]
#                     np.delete(C, Centers[0])
#                     del Centers[0]
#                     np.delete(D, plant)
#                     del plants[0]
                    
#     def Evaluate(self, TransCosts, FixedCosts):
#         self.GenerateSolution()
#         self.Eval = (self.solution * TransCosts).sum() + sum(np.clip(self.solution.sum(axis=1), 0, 1) *FixedCosts)
#         return self.Eval        




class solStucture:
    def __init__(self, Demands, Capacities, ChanceProbability=0.95):
        self.NumberOFDistCenter = len(Capacities)
        self.NumberOfPlants = len(Demands)
        
        # Use numpy for faster random generation
        self.DistCenterArray = np.random.rand(self.NumberOFDistCenter)
        self.PlantArray = np.random.rand(self.NumberOfPlants)
        self.ChanceProbability = ChanceProbability

        self.Demands = Demands
        self.Capacities = Capacities

    def GenerateSolution(self):
        self.solution = np.zeros((self.NumberOFDistCenter, self.NumberOfPlants), dtype=int)
        
        # Generate demands with chance probability
        D = GenerateDemands(self.Demands, self.ChanceProbability)
        C = self.Capacities.copy()

        # Sort centers and plants based on priority
        sorted_centers = np.argsort(self.DistCenterArray)
        sorted_plants = np.argsort(self.PlantArray)

        # Loop through plants and assign demands to centers
        for plant in sorted_plants:
            while D[plant] > 0 and sorted_centers.size > 0:
                center = sorted_centers[0]
                if D[plant] <= C[center]:
                    self.solution[center, plant] += D[plant]
                    C[center] -= D[plant]
                    D[plant] = 0
                else:
                    self.solution[center, plant] += C[center]
                    D[plant] -= C[center]
                    C[center] = 0
                    sorted_centers = sorted_centers[1:]  # Remove exhausted center

    def Evaluate(self, TransCosts, FixedCosts):
        self.GenerateSolution()
        # Evaluate transportation and fixed costs
        transport_cost = (self.solution * TransCosts).sum()
        fixed_cost = (self.solution.sum(axis=1) > 0).astype(int) @ FixedCosts
        self.Eval = transport_cost + fixed_cost
        return self.Eval
