M=input()
N=M
print("Input:")
print(M)
sum=0
while(M>0):
   mod=M%10
   M=M//10
   sum=sum*10+mod
print("Output:")
if sum==N:
    print("yes")
else:
    print("no") 
