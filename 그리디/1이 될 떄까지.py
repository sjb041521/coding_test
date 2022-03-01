# n%k를 위한 입력 값
n, k = map(int, input().split())
count = 1

while n > k:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1
print(count)
