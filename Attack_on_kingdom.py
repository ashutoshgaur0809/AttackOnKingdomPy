T = int(input("Enter no. of texst case ="))
n = int(input("Enter no. of days = "))
l = []
for i in range(n):
    t = int(input("Enter temp = "))
    l.append(t)
print(l)
l.sort()
print(l)
print(l[1])
