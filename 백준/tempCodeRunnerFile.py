N = int(input())

array = []

for _ in range(N):
    stu = input().split()

    array.append([stu[0], int(stu[1]), int(stu[1]), int(stu[2])])

array.sort(key=lambda x: (-x[1], x[2], -x[3], x[0][0].lower(), x[0][1:]))

for i in array:
    print(i[0])
