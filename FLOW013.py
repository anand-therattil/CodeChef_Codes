for _ in range(int(input())):
    (A,B,C) = list(map(int,input().split(" ")))
    if(A+B+C==180):
        print('YES')
    else:
        print('NO')
