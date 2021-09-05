a = [[1, 1], [2, 5], [7, -3]]
Hasil = [[0,0,0], [0,0,0]]
for b in range(len(a)):
    for c in range(len(a[0])):
        Hasil[c][b] = a[b][c]
print ("Result transpos matrix is")

for r in Hasil:
    print(r)
