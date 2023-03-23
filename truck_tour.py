def truckTour(petrolpumps):
    tank = 0
    index = 0
    i = 0
    while i < len(petrolpumps):
        tank += petrolpumps[i][0] - petrolpumps[i][1]
        if tank < 0:
            index = i + 1
            i = index
            tank = 0
        else:
            i = i + 1
    return index
