import math
import numpy as np
import random


class offerSet:
    def __init__(self, i, j, k, c, t, b, u, e):
        self.i = i  # ith subtask
        self.j = j  # jth server
        self.K = k  # kth offer from jth server
        self.C = c  # cost of this offer
        self.T = t  # time to run this offer
        self.B = b  # bandwidth for this offer
        self.U = u  # utility of this offer
        self.E = e  # energy consumption


def getTwoRandom():
    temp = []
    temp.append(random.randint(0, len(library) - 1))
    while True:
        cur = random.randint(0, len(library) - 1)
        if cur != temp[0]:
            temp.append(cur)
            return temp


def getMax(a, b):
    cura = float(a)
    curb = float(b)
    cur = cura - curb
    if (cur > 0):
        return a
    else:
        return b


# parameter: array of time of each subtask, subtask no
def CompletionTime(x, n):
    # root
    if Adj_List[n][0] == -1:
        return float(x[n])
    cur = 0.0
    for i in Adj_List[n]:
        ret = CompletionTime(x, i)
        cur = getMax(cur, ret)
    return float(x[n]) + float(cur)


def CompletionEnergyCost(x):
    curEnergy = 0
    curCost = 0
    for i in range(0, len(x)):
        if (x[i] == '1') or (x[i] == 1):
            curEnergy += float(offer[i].E)
            curCost += float(offer[i].C)
    return curEnergy, curCost


def Valid(x):
    visit = [0] * numOfSubtask
    time = [0] * numOfSubtask
    energy = [0] * numOfSubtask

    for i in range(0, len(x)):
        if (x[i] == '1') or (x[i] == 1):
            if visit[int(offer[i].i)] == 1: return 0
            time[int(offer[i].i)] = offer[i].T
            visit[int(offer[i].i)] = 1

    # rest of the subtask, not allocated in any server will be executed locally
    sz = 0.0
    for i in range(0, numOfSubtask):
        if time[i] == 0:
            sz += ToBit(SubtaskSize[i])

    # time for local execution
    local_time = (sz * CPU_per_bitCycle) / frequency
    kappa = 1e-11
    local_energy = (kappa) * (frequency ** 2) * (sz * CPU_per_bitCycle)
    local_energy = (sz * CPU_per_bitCycle) * (.5) / (10 ** 9)

    # so total time = time to execute remotely + time to execute locally
    completion_time = CompletionTime(time, numOfSubtask - 1) + local_time
    completion_energy, completion_cost = CompletionEnergyCost(x)
    completion_energy += local_energy

    if (completion_time > TD): return 0
    if (completion_energy > ED): return 0
    if (completion_cost > budget): return 0
    return 1


def getUtility(x):
    visit = [0] * numOfSubtask
    remote_utility = 0.0
    cost = 0.0
    for i in range(0, len(x)):
        if (x[i] == '1') or (x[i] == 1):
            remote_utility = remote_utility + float(offer[i].U)
            visit[int(offer[i].i)] = 1
            cost += float(offer[i].C)

    # utility to execute rest of the task locally
    sz = 0
    for i in range(0, numOfSubtask):
        if visit[i] == 0:
            sz += SubtaskSize[i]

    # time for local execution
    sz = ToBit(sz)
    local_time = (sz * CPU_per_bitCycle) / frequency
    # kappa = 1e-11
    # local_energy = kappa * (frequency ** 2) * (sz * CPU_per_bitCycle)
    local_energy = (sz * CPU_per_bitCycle) * (.5) / (10 ** 9)
    tau, eps, sigma = .01, .01, 1

    # now normalized time and energy
    norm_t = 0.0
    if local_time <= TD:
        norm_t += tau + (1 - tau) * (1 - np.exp(sigma * (local_time - TD)))

    norm_e = 0.0
    if local_energy <= ED:
        norm_e += eps + (1 - eps) * (1 - np.exp(sigma * (local_energy - ED)))

    beta = .5
    alpha = .7

    local_utility = beta * norm_t + (1 - beta) * norm_e
    Utility_Energy_Latency = local_utility + remote_utility

    # incorporate cost
    cost = 0.0
    for i in range(0, len(x)):
        if x[i] == '1' or x[i] == 1:
            cost += float(offer[i].C)
    cost /= budget

    UTILITY = alpha * Utility_Energy_Latency - (1 - alpha) * cost
    return UTILITY


def action(x1, x2):
    # print(len(x1),"----",len(x2))
    x3 = []
    for i in range(0, len(x1)):
        p, q = int(x1[i]), int(x2[i])
        r = 0
        temp = p + 2 * random.random() * (q - p)
        if temp < 0.5:
            r = 0
        else:
            r = 1

        x3.append(r)
    # print(x3)
    if Valid(x3) == 0: x3 = []

    return x3


def p_library():
    for i in library:
        cur = ""
        for j in i: cur += j
    return


def ToBit(KB):
    return KB * 1024 * 8


def call(ag):
    Random = getTwoRandom()
    point = Random[1]
    if library_Utility[Random[0]] > library_Utility[point]:
        point = Random[0]
    central = library[point]
    ref = library[ag]
    # point, having smaller utility should be assigned to ref point
    if library_Utility[point] < library_Utility[ag]:
        # swap them
        ref, central = central, ref

    x3 = action(ref, central)
    # print(x3)
    return x3


def updateLibrary(x):
    Random = getTwoRandom()
    Random.extend(getTwoRandom())
    Random.extend(getTwoRandom())
    Random = list(set(Random))

    mn = 20000
    # kick (pos)th index from the library = having minimum utility
    pos = -1
    for i in range(0, len(Random)):
        if library_Utility[Random[i]] < mn:
            mn = library_Utility[Random[i]]
            pos = Random[i]
    library[pos] = x
    cur = getUtility(x)
    # update the corresponding utility in the libray
    library_Utility[pos] = cur
    return


def optimalTimeEnergyCost(x):
    visit = [0] * numOfSubtask
    time = [0] * numOfSubtask
    energy = [0] * numOfSubtask

    for i in range(0, len(x)):
        if (x[i] == '1') or (x[i] == 1):
            if visit[int(offer[i].i)] == 1: return 0
            time[int(offer[i].i)] = offer[i].T
            # print(str(offer[i].i) + "th subtask:- time->  " + str(offer[i].T) + " cost->" + str(
            #     offer[i].C) + " server->" +
            #       str(offer[i].j) + " offer number->" + str(i) + " energy consumption->" + str(offer[i].E))
            visit[int(offer[i].i)] = 1

    # rest of the subtask, not allocated in any server will be executed locally
    sz = 0.0
    for i in range(0, numOfSubtask):
        if time[i] == 0:
            sz += SubtaskSize[i]

    print("Local execution size->" + str(sz) + " kb")
    sz = ToBit(sz)
    # time for local execution
    local_time = (sz * CPU_per_bitCycle) / frequency
    # print(local_time)
    # kappa = 1e-11
    # local_energy = kappa * (frequency ** 2) * (sz * CPU_per_bitCycle)
    local_energy = (sz * CPU_per_bitCycle) * .5 / (10 ** 9)
    print("Local execution latency->" + str(local_time) + " Local energy consumption->" + str(local_energy))

    # so total time = time to execute remotely + time to execute locally
    completion_time = CompletionTime(time, numOfSubtask - 1) + local_time
    completion_energy, completion_cost = CompletionEnergyCost(x)
    completion_energy += local_energy
    return completion_time, completion_energy, completion_cost


########################################
#
# All declaration is here
#

offer = []
# Time_Deadline, Energy Deadline, Budget


file = open("randomValue.txt", "r")
lines = file.readlines()
cur = lines[0].split()

TD = float(cur[0])
ED = float(cur[1])
budget = float(cur[2])

CPU_per_bitCycle = 600
frequency = 1e9

SubtaskSize = [70, 100, 110, 105, 120, 95]
Adj_List = [[-1], [0], [1], [2], [3], [4]]

num_of_agent = 5
plan = []
numOfSubtask = len(SubtaskSize)

########################################

file = open("offerset.txt", 'r')
lines = file.readlines()
for line in lines:
    cur = line.split()
    offer.append(offerSet(cur[0], cur[1], cur[2], cur[3], cur[4], cur[5], cur[6], cur[7]))
    # print(cur)
file.close()


# demo plan
# will change later
# plan.append([0,0,1,0,1,1])

file = open("plan.txt", 'r')
lines = file.readlines()
for line in lines:
    temp = []
    cur = line.split()
    for i in cur:
        temp.append(i)
    plan.append(temp)

library = plan

library_Utility = []
# update utility of library

for i in range(0, len(library)):
    total_utility = getUtility(library[i])
    library_Utility.append(total_utility)

# print(library_Utility)

# in each iteration, each agent will make a move.
# after ending of each iteration, all the agents will update the library
for it in range(0, 500):
    temp = []
    for agent in range(0, num_of_agent):
        x = call(agent)
        # print(x)
        if len(x) > 0:
            temp.append(x)
    for i in range(0, len(temp)):
        updateLibrary(temp[i])

# print the optimal result
mn = 100.0
pos = -1
for i in range(0, len(library_Utility)):
    if library_Utility[i] < mn:
        mn = library_Utility[i]
        pos = i

# print(pos)
optimal_plan = library[pos]
optimal_utility = getUtility(optimal_plan)
optimal_time, optimal_energy, optimal_cost = optimalTimeEnergyCost(optimal_plan)

print("Time deadline -> " + str(TD))
print("Energy deadline ->" + str(ED))
print("Budget ->" + str(budget))

if Valid(optimal_plan) == 0:
    print("Task drop")
    # print("Optimal Time->" + str(optimal_time))
    # print("Optimal Energy->" + str(optimal_energy))
    # print("Optimal Cost->" + str(optimal_cost))
    # print("Optimal Utility->" + str(optimal_utility))
else:
    print(optimal_plan)
    # print(library_Utility)
    print("Optimal Time->" + str(optimal_time))
    print("Optimal Energy->" + str(optimal_energy))
    print("Optimal Cost->" + str(optimal_cost))
    print("Optimal Utility->" + str(optimal_utility))
