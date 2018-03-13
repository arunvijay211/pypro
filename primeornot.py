N = input()
print("Input:")
print(N)
print("Output:")
if N<1000:
   for i in range(2,N):
       if (N % i) == 0:
           print("no")
           break
   else:
       print("yes")
