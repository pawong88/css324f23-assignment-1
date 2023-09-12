def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s
    list = []
    if x > 0:
        if y < 5:
            cost = min(5-y, x)
            list.append([(x-cost, y+cost, z),cost])
        if z < 3:
            cost = min(3-z, x)
            list.append([(x-cost, y, z+cost),cost])
    if y > 0:
        if x < 8:
            cost = min(8-x, y)
            list.append([(x+cost, y-cost, z),cost])
        if z < 3:
            cost = min(3-z, y)
            list.append([(x, y-cost, z+cost),cost])
    if z > 0:
        if x < 8:
            cost = min(8-x, z)
            list.append([(x+cost, y, z-cost),cost])
        if y < 5:
            cost = min(5-y, z)
            list.append([(x, y+cost, z-cost),cost])
    return list
