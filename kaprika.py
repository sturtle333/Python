num = int(input())
lst=[int(num/1000%10),int(num/100%10),int(num/10%10),int(num%10)]

minNum = maxNum = 0

lst.sort()
minNum = lst[0]*1000 + lst[1]*100 + lst[2]*10 + lst[3]
lst.reverse()
maxNum = lst[0]*1000 + lst[1]*100 + lst[2]*10 + lst[3]
count = 1
temp=maxNum-minNum

while temp != 6174:
    lst=[int(temp/1000%10),int(temp/100%10),int(temp/10%10),int(temp%10)]
    lst.sort()
    minNum = lst[0]*1000 + lst[1]*100 + lst[2]*10 + lst[3]
    lst.reverse()
    maxNum = lst[0]*1000 + lst[1]*100 + lst[2]*10 + lst[3]

    count += 1
    temp=maxNum-minNum
print(count)

