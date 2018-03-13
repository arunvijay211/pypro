N=input()
K=input()
a=[]
i=1
while i<=N:
   a.append(i)
   i=i+1
print("Array of N integers is:")  
print(a)
sum=0
for i in range(0,int(K)):
   sum=sum+a[i]
print("sum of K integers is:")
print(sum)
