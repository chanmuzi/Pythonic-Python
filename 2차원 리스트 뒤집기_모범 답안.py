def solution(mylist):
    length = len(mylist)
    answer = []

    for i in range(length):
        # 2차원 배열 만들기
        answer.append([])
        for j in range(length):
            # 행과 열을 반대로 추가
            answer[i].append(mylist[j][i])
 
    return answer