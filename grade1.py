r=int(input())
c=int(input())
n=int(input())
if n<=r*c:
    if n<=c or n%c==0 or n%c==1:
        print("Yes")
    else:
        print("No")
