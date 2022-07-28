def solution(mylist):
    return [abs(mylist[x]-mylist[x+1]) for x in range(len(mylist)-1)]