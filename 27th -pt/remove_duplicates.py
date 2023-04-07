l1=input().split()
for i in l1:
    if(l1.count(i)>1):
        l1.remove(i)
print(l1)