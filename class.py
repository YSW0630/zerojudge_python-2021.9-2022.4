L = []
j_L = []
while 1:
    n = int(input())
    if n == 0:
        break
    else:
        L.append(n)
for i in L:
    for j in range(1, i):
        if j % 7 != 0:
            j_L.append(str(j))
    print(" ".join(j_L))
    j_L = []