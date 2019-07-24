number = str(input())
lst=[]
lst.append(number[0])
lst.append(number[1])
lst.append(number[2])
lst.append(number[3])

count = 0
lst.sort()
a=0
a+=1000*int(lst[0])
a+=100*int(lst[1])
a+=10*int(lst[2])
a+=int(lst[3])

lst.reverse()
b=0
b+=1000*int(lst[0])
b+=100*int(lst[1])
b+=10*int(lst[2])
b+=int(lst[3])


c=b-a
count+=1
while c != 6174:
    lst[0] = c/1000
    lst[1] = c/100%10
    lst[2] = c/10%10
    lst[3] = c%10

    lst.sort()
    a=0
    a+=1000*int(lst[0])
    a+=100*int(lst[1])
    a+=10*int(lst[2])
    a+=int(lst[3])

    lst.reverse()
    b=0
    b+=1000*int(lst[0])
    b+=100*int(lst[1])
    b+=10*int(lst[2])
    b+=int(lst[3])
    c = b-a
    count+=1
print(count)


