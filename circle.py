import math
x1=int(input())
y1=int(input())
r1=int(input())
x2=int(input())
y2=int(input())
r2=int(input())
x3=(x1-x2)*(x1-x2)
y3=(y1-y2)*(y1-y2)
c1c2=math.sqrt(x3+y3)
if c1c2 == r1+r2:
    print("The circles are tangential")
elif c1c2 < r1+r2:
    print("The circles overlap")
else:
    print("The circles do not overlap")
