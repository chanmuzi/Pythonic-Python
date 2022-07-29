def solution(mylist):
    answer = list()
    for i in mylist:
        for j in range(len(i)):
            answer.append(i[j])
    return(answer)