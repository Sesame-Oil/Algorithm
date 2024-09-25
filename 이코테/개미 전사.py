n = int(input())
klist = list(map(int, input().split()))
d = [0] * 100

d[0] = klist[0]
d[1] = max(klist[0], klist[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+klist[i])

print(d[n-1])
