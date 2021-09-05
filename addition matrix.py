a = [[2, 4], [6, -8]]
b = [[3, 0], [10, -6]]
print("Result addition Matrix is")
for x in range(0, len(a)):
    for y in range(0, len(a[0])):
        print(a[x][y] + b[x][y], end=' '),
    print
