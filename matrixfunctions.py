def matrixAddition(*matrices):
    row_counts = {len(matrix) for matrix in matrices}
    col_counts = {len(row) for matrix in matrices for row in matrix}
    if len(row_counts) <= 1 and  len(col_counts) <= 1:
        matrix = [[0 for j in range(len(matrices[0][0]))] for i in range(len(matrices[0]))]
        for i in range(len(matrices[0])):
            for a in range(len(matrices[0][i])):
                positionSum = sum(m[i][a] for m in matrices)
                matrix[i][a] = positionSum
        return matrix
    else:
        print("Invalid matrices. Matrices must be of the same dimensions.")

def matrixSubtraction(*matrices):
    row_counts = {len(matrix) for matrix in matrices}
    col_counts = {len(row) for matrix in matrices for row in matrix}
    if len(row_counts) <= 1 and  len(col_counts) <= 1:
        matrix = [[0 for j in range(len(matrices[0][0]))] for i in range(len(matrices[0]))]
        for i in range(len(matrices[0])):
            for a in range(len(matrices[0][i])):
                positionSum = sum(m[i][a] for m in matrices[1:])
                positionDifference = matrices[0][i][a] - positionSum
                matrix[i][a] = positionDifference
        return matrix
    else:
        print("Invalid matrices. Matrices must be of the same dimensions.")

def matrixSubtraction(matrix1, matrix2):
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):  
        matrix3 = [[0] for i in range(len(matrix1))]
        for i in range(len(matrix1)):
            for a in range(len(matrix1[i])):
                matrix3[i].append(matrix1[i][a] - matrix2[i][a])
        return matrix3
    else:
        print("Invalid matrices. Matrices must be of the same dimensions.")

#Elementary row operations: Replace, + kx, kx

def createEchelonForm(matrix):
    pivotColList = []
    column = 0
    pivotRows = 0
    while pivotRows < len(matrix) and column < len(matrix[0]):
        truthVar = scanColumn(matrix, pivotRows, column)[0]
        if truthVar or truthVar == 0:
            placeholder1 = matrix[truthVar]
            placeholder2 = matrix[pivotRows]
            matrix[truthVar] = placeholder2
            matrix[pivotRows] = placeholder1
            eliminatBelowRows(matrix, pivotRows, column)
            pivotColList.append(((pivotRows, column)))
            pivotRows += 1
        column+=1
        continue
    return pivotColList

def createRREF(matrix):
    pivotColList = createEchelonForm(matrix)
    for (row, column) in pivotColList:
        scalePivotRow(matrix, row, column)
        eliminateAboveRows(matrix, row, column)
    return matrix, pivotColList
    

def eliminatBelowRows(matrix, pivotRows, column):
    p = matrix[pivotRows][column]
    for someRow in range(pivotRows + 1, len(matrix)):
        v = matrix[someRow][column]
        if v == 0:
           continue
        else:
            k = v/p
            for col in range(len(matrix[0])):
                matrix[someRow][col] = matrix[someRow][col] - k * matrix[pivotRows][col]
                matrix[someRow][col] = round(matrix[someRow][col], 10)

def eliminateAboveRows(matrix, pivotRows, column):
    for someRow in range(pivotRows):
        v = matrix[someRow][column]
        if v == 0:
            continue
        else:
            for col in range(len(matrix[0])):
                matrix[someRow][col] = matrix[someRow][col] - v*matrix[pivotRows][col]
                matrix[someRow][col] = round(matrix[someRow][col], 10)

def scanColumn(matrix, row, column):
    if matrix[row][column] == 0 and row < len(matrix) - 1:
        return scanColumn(matrix, row+1, column)
    elif matrix[row][column] != 0:
        return (row, column)
    elif row == len(matrix) - 1:
        if matrix[row][column] != 0:
            return (row, column)
        else:
            return None, None

def scalePivotRow(matrix, pivotRows, column):
    p = matrix[pivotRows][column]
    for col in range(len(matrix[0])):
        matrix[pivotRows][col] = matrix[pivotRows][col] / p
        matrix[pivotRows][col] = round(matrix[pivotRows][col], 10)

def printMatrix(matrix):
    for row in matrix:
        print(row)

def concatenate(matrix1, matrix2):
    if len(matrix1)==len(matrix2):
        result = [[] for i in range(len(matrix1))]
        for i in range(len(matrix1)):
            result[i] = matrix1[i] + matrix2[i]
        return result
    else:
        print("Both matrices need the same number of rows, please try again.")

def solveMatrixEquation(A, B):
    augmented, pivotColList = createRREF(concatenate(A, B))
    identityMatrixCheck = all(x==y for (x,y) in pivotColList) and len(pivotColList)==len(A)
    solutionsDict = {}
    for col in range(len(A[0]), len(augmented[0])):
        noSolutionCheck = False
        for row in range(len(A)):
            if augmented[row][col] != 0 and all(x==0 for x in augmented[row][:len(A)]):
                    if len(B[0]) > 1:
                        print(f"No solution for A with column {col} of B.")
                    else:
                        print("No solution")
                    noSolutionCheck = True
                    solutionsDict[col-len(A[0])] = None
        if noSolutionCheck:
            continue
        if identityMatrixCheck:
            currentColSolution = [augmented[r][col] for r in range(len(A))]
            solutionsDict[col-len(A[0])] = currentColSolution
            if len(B[0]) > 1:
                print(f"The solution for A with column {col} of B is {currentColSolution}.")
            else:
                print(f"The solution is {currentColSolution}.")
            continue
        else:
            solutionsDict[col-len(A[0])] = "Infinite"
            if len(B[0])>1:
                print(f"Infinite solutions for A with column {col} of B.")
            else:
                print("Infinite solutions.")
            continue
    if len(B[0]) > 1:
        print("The following dictionary maps the solution of the columns of B with A.")
        print(solutionsDict)

