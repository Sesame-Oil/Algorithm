N = int(input())

array = []

for _ in range(N):
    stu = input().split()

    array.append([stu[0], int(stu[1]), int(stu[2]), int(stu[3])])

array.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in array:
    print(i[0])
