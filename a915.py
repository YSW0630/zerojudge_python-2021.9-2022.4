l = []
n = int(input())
for i in range(n):
    l.append(list(map(int, input().split(" "))))
    
for i in l:
    print(i[0], i[1])