#  N : 행의 개수 , M : 열의 개수
n, m = map(int, input().split())
# 행의 가장 작은 값
min_num = []
# 행의 가장 작은 값들 중 가장 큰 값
max_num = 0

# 계산 식
for i in range(n):
    data = list(map(int, input().split()))
    min_num.append(min(data))
    max_num = max(min_num)

print(max_num)
