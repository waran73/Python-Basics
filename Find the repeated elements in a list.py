a = []
n = int(input())
for i in range(n):
    x = int(input())
    a.append(x)
print(a)
for x in set(a):
    count=a.count(x)
    if(count>1):
        print(x)
