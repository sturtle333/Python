mat33 = [0,0,0,0,0,0,0,0,0]
mat22 = [0,0,0,0]

for a in range(0, 9):
    mat33[a] = int(input())

def calcMat22 ():
    return (mat22[0]*mat22[3])-(mat22[1]*mat22[2])

def calcMat33():
    result = 0
    for a in range(0,3):
        temp = 0
        for b in range(0,3):
            if a!=b:
                mat22[temp]=mat33[b+3]
                mat22[temp+2]=mat33[b+(3*2)]
                temp += 1
        if a%2==0:
            result+=mat33[a]*calcMat22()
        else :
            result-=mat33[a]*calcMat22()
    return result

print(calcMat33())


"""
import numpy as np
A = np.matrix(input("input a: 1 1 1; 2 2 2; 3 3 3\n))

print(A)
print('det A = ', round(np.linealg.det(A),3))
"""
