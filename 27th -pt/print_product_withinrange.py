l=list(map(int,input("").split()))
x=[]
a,b=(map(int,input("").split()))
x.append(l[a:b])
print(x)
mul=1
for i in x[0]:
        mul=i*mul
print(mul)