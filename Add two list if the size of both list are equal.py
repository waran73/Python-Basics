a=[1,10,100]
b=[1,10,100]
c=[]
if len(a)==len(b):
    for i in range(3):
        c.append(a[i]+b[i])
    print(c)
else:
    print('Invalid')
