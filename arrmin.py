N=int(input())
a=[]
i=1
while i<=N:
   a.append(i)
   i=i+1
print("Array of N integers is:")  
print(a)
min=a[0]
for i in range(1,int(N)):
   if(min>a[i]):
      min=a[i]
print("Min number is:")
print(min)
