from itertools import permutations

def solution(mylist):
    case = permutations(mylist)
    return sorted([list(x) for x in case])