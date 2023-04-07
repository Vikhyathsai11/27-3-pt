l=input().split()
l1=[]
for i in l:
    if((l.count(i)%2)!=0) and i not in l1:
        l1.append(i)

for i in l1:
    if(l1.count(i)>1):
        l1.remove(i)
print(l1)