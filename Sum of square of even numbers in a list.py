a=[]
s=0
n=1
while n!=0:
    n=int(input())
    a.append(n)
for i in a:
    if i%2==0:
        s=s+i**2
print(s)
