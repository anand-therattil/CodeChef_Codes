def add(n):
    if(n==1):
        return 1
    elif(n==2):
        return 4
    else:
        return (n*n +add(n-2))

    
for testcase in range(int(input())):                        # NO_OF_TESTCASE 
  n= int(input())
  count =0
  while(n>0):
      if(n==1):
          count =count +1
      elif(n==2):
          count= count +4
      else:
          count = count +n*n
      n=n-2
    
  print(count)