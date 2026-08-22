def matrixAddition(matrix1, matrix2):
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):  
        matrix3 = [[] for i in range(len(matrix1))]
        for i in range(len(matrix1)):
            for a in range(len(matrix1[i])):
                matrix3[i].append(matrix1[i][a] + matrix2[i][a])
        return matrix3
    else:
        print("Invalid matrices. Matrices must be of the same dimensions.")

def matrixSubstraction(matrix1, matrix2):
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):  
        matrix3 = [[] for i in range(len(matrix1))]
        for i in range(len(matrix1)):
            for a in range(len(matrix1[i])):
                matrix3[i].append(matrix1[i][a] - matrix2[i][a])
        return matrix3
    else:
        print("Invalid matrices. Matrices must be of the same dimensions.")

#Elementary row operations: Replace, + kx, kx

def createEchelonForm(matrix):
    column = 0
    pivotRows = 0
    while pivotRows < len(matrix):
        while column < len(matrix[0]):
            truthVar = scanColumn(matrix, pivotRows, column)
            if truthVar or truthVar == 0:
                pivotRows += 1
                placeholder1 = matrix[truthVar]
                placeholder2 = matrix[pivotRows]
                matrix[truthVar] = placeholder2
                matrix[pivotRows] = placeholder1
            column+=1
        continue
            

def scanColumn(matrix, row, column):
    if matrix[row][column] == 0 and row < len(matrix) - 1:
        return scanColumn(matrix, row+1, column)
    elif matrix[row][column] != 0:
        return row
    elif row == len(matrix) - 1:
        if matrix[row][column] != 0:
            return row
        else:
            return None




test1 = [[1.0,2.0,3.0], [0.0,2.0,3.0], [1.0,2.0,3.0]]
test2 = [[2.0,3.0,4.0], [5.0,6.0,7.0], [8.0,9.0,10.0]]
zeroMatrix = [[0 for j in range(len(test1[0]))] for i in range(len(test1))]

print(zeroMatrix)