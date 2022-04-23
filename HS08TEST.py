a= input().split(" ")
withdraw = float(a[0])
total = float(a[1])
del a 
if withdraw%5!=0 or withdraw >total-0.5:
    print(total)
elif(withdraw%5==0 and withdraw<total):
    print("{:.2f}".format(total-withdraw-0.5))
else:
    print(total)
