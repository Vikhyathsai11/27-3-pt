l=list(map(int,input("").split()))
l1=[]
l2=[]
for i in l:
    if((i%2)==0):
        l1.append(i)
    else:
        l2.append(i)
l1.sort()
print(l1)
l2.sort(reverse=True)
print(l2)
l3=l1+l2
print(l3)