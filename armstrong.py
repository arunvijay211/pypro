n=int(input())
print("Input: Enter any number:")
print(n)
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
print("Output:")
if(sum(b)==n):
    print("yes")
else:
    print("no")
   
   
