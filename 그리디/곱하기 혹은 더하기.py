n = list(map(int, input()))
sum = 1
n.sort(reverse=True)
for i in n:
    if i >= 1:
        sum *= i
    elif i == 0:
        sum += i
print(sum)
