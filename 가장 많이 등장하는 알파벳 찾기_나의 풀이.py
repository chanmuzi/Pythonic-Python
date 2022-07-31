from collections import Counter

my_str = input().strip()

str_dict = Counter(my_str).most_common()
answer = ''
max_count = str_dict[0][1]

for i in sorted(str_dict):
    if i[1] == max_count:
        answer += i[0]

print(answer)