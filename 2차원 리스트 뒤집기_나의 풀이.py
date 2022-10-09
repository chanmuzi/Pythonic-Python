def solution(mylist):
    length = len(mylist)
    answer = []

    for i in range(length):
        # 2차원 배열 만들기
        answer.append([])
        # 길이만큼 2중 for문 만들기
        for j in range(length):
            # 행과 열을 반대로 추가
            answer[i].append(mylist[j][i])
 
    return answer #정답 반환
