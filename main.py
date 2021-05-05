import random
import math
import numpy as np


class offerSet:
    def __init__(self, i, j, k, c, t, b, u, e):
        self.i = i  # ith subtask
        self.j = j  # jth server
        self.K = k  # kth offer from jth server
        self.C = c  # cost of this offer
        self.T = t  # time to run this offer
        self.B = b  # bandwidth for this offer
        self.U = u  # utility of this offer
        self.E = e  # energy required for this offer


def GetVmLevel(NumOfServer, k):
    VM = []
    for i in range(0, NumOfServer):
        level = random.randint(1, k)
        VM.append(level)
    return VM


# return the number of VM in each unit
def GetVmLevelUnit(VmLevel):
    Unit = []
    for i in VmLevel:
        temp = []
        start = random.randint(4, 10)
        step = random.randint(2, 5)
        for j in range(0, i):
            temp.append(start)
            start = start + step
        Unit.append(temp)
    return Unit


def GetPerUnitVmCost(NumOfServer):
    temp = []
    for i in range(0, NumOfServer):
        perUnitVmCost = random.random() + 1
        temp.append(perUnitVmCost)
    return temp


def getBandwidth(NumOfServer):
    temp = []
    for i in range(0, NumOfServer):
        temp.append(random.randint(3, 6))
    return temp


def ToBit(KB):
    return KB * 1024 * 8


# return the normalised latency of an offer
def NormalizedTime(i, b, T):
    t = SubtaskSize[i] / (b * 1024)
    ret = 0
    tau, sigma = .01, 1
    TotalTime = (2 * t) + T
    if TotalTime <= TD:
        ret = tau + (1 - tau) * (1 - np.exp(sigma * (TotalTime - TD)))
    else:
        ret = 0
    return ret


def NormalizedEnergy(i, b):
    t = SubtaskSize[i] / (b * 1024)

    # transmission Energy
    T_E = T_P * t
    ret = 0
    eps, sigma = .01, 1
    if T_E <= ED:
        ret = eps + (1 - eps) * (1 - np.exp(sigma * (T_E - ED)))
    else:
        ret = 0
    return ret


# get the utility of an offer
# utility = beta * time + (1-beta)* energy
def Utility(i, b, T):
    beta = .5
    N_time = NormalizedTime(i, b, T)
    N_Energy = NormalizedEnergy(i, b)
    U = beta * N_time + (1 - beta) * N_Energy
    return U


# parameter: array of time of each subtask, subtask no
def CompletionTime(x, n):
    # root
    if Adj_List[n][0] == -1:
        return x[n]
    cur = 0
    for i in Adj_List[n]:
        cur = max(cur, CompletionTime(x, i))
    return x[n] + cur


def CompletionEnergyCost(x):
    curEnergy = 0
    curCost = 0
    for i in range(0, len(x)):
        if x[i] == 1:
            curEnergy += Offer[i].E
            curCost += Offer[i].C
    return curEnergy, curCost


# number of maximum offers, a server can submit
K = 5
NumOfServer = 3
# Time_Deadline, Energy Deadline, Budget
TD = random.uniform(0.4, 2.2)
ED = random.uniform(0.1, 1.5)
budget = random.randint(40, 70)

file = open("randomValue.txt", "w")
file.write(str(TD) + " " + str(ED) + " " + str(budget))

# VmLevel[i] = number of VmLevel in ith server
VmLevel = GetVmLevel(NumOfServer, K)
VmCost = GetPerUnitVmCost(NumOfServer)
# VmLevelUnit[i][j] = number of vm in jth level of ith server
VmLevelUnit = GetVmLevelUnit(VmLevel)
Bandwidth = getBandwidth(NumOfServer)

# 1.6e9 HZ
FrequencyOfEachVm = 1.6 * (10 ** 9)

# ith subtask size  in KB
SubtaskSize = [70, 100, 110, 105, 120, 95]
Adj_List = [[-1], [0], [1], [2], [3], [4]]

# parent list

# Adj_List=[[-1],[0],[0],[1,2]]

Subtask = len(SubtaskSize)
numOfSubtask = Subtask

CPU_per_bitCycle = 600
frequency = 1e9

# transmission power
T_P = .5

numberOfInitialSolution = 50

Offer = []

for i in range(0, Subtask):
    for j in range(0, NumOfServer):
        for k in range(0, VmLevel[j]):
            # size in bit
            Subtask_Size = ToBit(SubtaskSize[i])
            time = (Subtask_Size * CPU_per_bitCycle) / (VmLevelUnit[j][k] * FrequencyOfEachVm)
            cost = VmLevelUnit[j][k] * VmCost[j]
            bandwidth = Bandwidth[j]
            utility = Utility(i, bandwidth, time)
            t = SubtaskSize[i] / (bandwidth * 1024)
            # print(t)
            energy = T_P * t

            if random.random() < 0.65:
                Offer.append(offerSet(i, j, k, cost, (2 * t) + time, bandwidth, utility, energy))

# Algorithm 3 starts from here


# def Compare(offers):
#     return offers.U


# Offer.sort(key=Compare, reverse=True)
random.shuffle(Offer)
file = open("offerset.txt", "w")

for i in range(0, len(Offer)):
    temp = str(Offer[i].i) + " " + str(Offer[i].j) + " " + str(Offer[i].K) + " " + str(Offer[i].C) + " " + str(
        Offer[i].T) \
           + " " + str(Offer[i].B) + " " + str(Offer[i].U) + " " + str(Offer[i].E) + "\n"
    file.write(temp)
    # print("subtask:{}  server={}  offer no= {} Cost={} time={} Utility={}".format(Offer[i].i, Offer[i].j, Offer[i].K,
    #                                                                               Offer[i].C, Offer[i].T, Offer[i].U))

file.close()

initialSolutions = []
vectorized = [0] * len(Offer)
checkSubtask = [0] * len(SubtaskSize)
subTaskSet = []

curCost = 0
curTime = 0
curEnergy = 0

print(len(Offer))
for i in range(0, len(Offer), 2):
    # print("{} start from ----->", i)
    # if len(initialSolutions) > len(Offer)/2:
    #     break
    checkSubtask = [0] * len(SubtaskSize)
    curCost = 0
    curTime = 0
    curEnergy = 0
    vectorized = [0] * len(Offer)
    subTaskSet.clear()
    for j in range(i, i + len(Offer)):
        # print(j)
        j = j % len(Offer)
        t = SubtaskSize[Offer[j].i] / (Offer[j].B * 1024)
        energy = T_P * t
        if (curCost + Offer[j].C <= budget) and (curTime + Offer[i].T + t <= TD) and (curEnergy + energy <= ED) \
                and (checkSubtask[Offer[j].i] == 0):
            vectorized[j] = 1
            checkSubtask[Offer[j].i] = 1
            subTaskSet.append(Offer[j].i)
            curCost += Offer[j].C
            curTime += (Offer[i].T + t)
            curEnergy += energy
        else:
            vectorized[j] = 0
    initialSolutions.append(vectorized)

file = open("plan.txt", "w")

for vectorSolution in initialSolutions:
    # file.write(vectorSolution)
    temp = ""
    for j in vectorSolution:
        temp += str(j) + " "
    file.write(temp + "\n")
    print(*vectorSolution)
