N=int(input())
a=[]
i=1
while i<=N:
   a.append(i)
   i=i+1
print("Array of N integers is:")  
print(a)
max=a[0]
for i in range(1,int(N)):
   if(max<a[i]):
      max=a[i]
print("Max number is:")
print(max)
