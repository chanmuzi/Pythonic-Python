num, base = map(int, input().strip().split(' '))
print(sum([base**x*int(str(num)[len(str(num))-x-1]) for x in range(len(str(num)))]))