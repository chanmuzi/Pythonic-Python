num, base = map(int, input().strip().split(' '))
answer = 0
for idx, number in enumerate(num[::-1]):
    answer += int(number) * (base ** idx)