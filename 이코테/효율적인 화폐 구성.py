n, m = map(int, input().split())

d = [10001]*(m+1)

coins = []

for i in range(n):
    coins.append(int(input()))

d[0] = 0

# for i in range(m+1):
#     for coin in coins:
#         min[]

for coin in coins:
    for i in range(m+1):
        d[i] = min(d[i-coin]+1, d[i])

print(d[m])
