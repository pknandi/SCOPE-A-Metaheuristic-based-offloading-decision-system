import random
import math
import numpy as np

drop = 0
passed = 0

for loop in range(0, 100):
    class offerSet:
        def __init__(self, i, j, k, c, t, b, u, e):
            self.i = i  # ith subtask
            self.j = j  # jth server
            self.K = k  # kth offer from jth server
            self.C = c  # cost of this offer
            self.T = t  # time to run this offer
            self.B = b  # bandwidth for this offer
            self.U = u  # utility of this offer
            self.E = e


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
    NumOfServer = 6
    # Time_Deadline, Energy Deadline, Budget
    TD = random.uniform(0.60, 1.4)
    ED = random.uniform(0.45, 1.2)
    budget = random.randint(46, 65)

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
    SubtaskSize = [75, 70, 50, 85, 63, 57]
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

    # print(len(Offer))
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
        # print(*vectorSolution)


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

        if completion_time > TD: return 0
        if completion_energy > ED: return 0
        if completion_cost > budget: return 0
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
        local_energy = (sz * CPU_per_bitCycle) * .5 / (10 ** 9)
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

    # SubtaskSize = [70, 100, 110, 105, 120, 95]
    # Adj_List = [[-1], [0], [1], [2], [3], [4]]

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
    if num_of_agent > len(plan):
        print("Drop")
        drop = drop + 1
        continue

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

    # print("Time deadline -> " + str(TD))
    # print("Energy deadline ->" + str(ED))
    # print("Budget ->" + str(budget))

    if Valid(optimal_plan) == 0:
        print(str(loop) + "-->Task drop")
        drop = drop + 1
        # print("Optimal Time->" + str(optimal_time))
        # print("Optimal Energy->" + str(optimal_energy))
        # print("Optimal Cost->" + str(optimal_cost))
        # print("Optimal Utility->" + str(optimal_utility))
    else:
        # print(optimal_plan)
        # print(library_Utility)
        print(str(loop) + "-->Task passed")
        passed = passed + 1
        # optimal_time, optimal_energy, optimal_cost = optimalTimeEnergyCost(optimal_plan)
        # print("Optimal Time->" + str(optimal_time))
        # print("Optimal Energy->" + str(optimal_energy))
        # print("Optimal Cost->" + str(optimal_cost))
        # print("Optimal Utility->" + str(optimal_utility))

print("Drop ---->" + str(drop))
print("Passed---->" + str(passed))
