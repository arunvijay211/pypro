a=raw_input()
if((int(a)%4)==0 and (int(a)%100)!=0):
    print("leap year")
elif((int(a)%4)==0 and (int(a)%100)==0 and (int(a)%400)==0):
    print("leap year")
else: 
    print(" not a leap year")
