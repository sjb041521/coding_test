
# 초기 값
# N = 배열의 크기 , M = 숫자가 더해지는 횟수 , K 연속으로 더할 수 있는 수
N, M, K = map(int, input().split())
n_list = list(map(int, input().split()))
n_num = []

# 정렬
n_list.sort()

# 계산식
n_num.append((n_list[-1]*K)*(M % K))
n_num.append(n_list[-2]*(M//K))

# 출력
print(n_num[0]+n_num[1])
