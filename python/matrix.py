matrix = []
def printMatrix (*arr):
    tempMatrix = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    count = 0
    for element in  arr:
        matrix[count] = element
    print("|",matrix[0],',',matrix[1],',',martix[2],'|')
    print("|",matrix[3],',',matrix[4],',',martix[5],'|')
    print("|",matrix[6],',',matrix[7],',',martix[8],'|')
    return
    
def inputMatrix ():
    count=0
    for a in range(0, 8):
        printMatrix(matrix)
        print("Input : ")
    return

inputMatrix()
