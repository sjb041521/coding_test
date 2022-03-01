# 받은 금액
n = 1260

# 거스름돈 동전 개수
won_count = []

# 동전 값
won_type = [500, 100, 50, 10]

# 계산식
for i in won_type:
    won_count.append(n // i)
    n %= i

# 출력
print("500원 : {}개 , 100원 : {}개 , 50원 : {}개 , 10원 : {}개 ".format(
    won_count[0], won_count[1], won_count[2], won_count[3]))
