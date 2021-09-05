a = [[3, 4], [2, 1]]
b = [[1, 5], [3, 7]]
c = []
for x in range(0, len(a)):
    row = []
    for y in range(0, len(a[0])):
        total = 0
        for z in range(0, len(a)):
            total = total + (a[x][y] * b[z][y])
        row.append(total)
    c.append(row)

for h in range(0, len(c)):
    for R in range(0, len(c[0])):
        print (c[x][y], end=' ')
    print()
