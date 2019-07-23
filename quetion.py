import math

temp=input().split(" ")

a = int(temp[0])
b = int(temp[1])
c = int(temp[2])
d = (b*b)-(4*a*c)


if d>0:
    x1 = (-b + math.sqrt((b*b)-(4*a*c)))/(2*a)
    x2 = (-b - math.sqrt((b*b)-(4*a*c)))/(2*a)
    print(x1," ",x2)
    
elif d==0:
    x1 = (-b + math.sqrt((b*b)-(4*a*c)))/(2*a)
    print(x1)
    
elif d<0:
    print('complex')
