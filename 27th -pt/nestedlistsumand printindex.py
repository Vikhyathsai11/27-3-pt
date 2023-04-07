n=int(input())
l1=[]
sum1=[]
for i in range(1,n+1):
    l=list(map(int,input("").split()))
    l1.append(l)   
for i in l1:
        sum1.append(sum(i))
print(sum1.index(max(sum1)))