n=int(input())
l1=[]
for i in range(1,n+1):
    l=input("").split()
    l1.append(l)
l1.sort(key=lambda l1:l1[1])
print(l1)