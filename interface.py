
import matrixfunctions

def enterMatrix():
    matrix = []
    columnsize = int(input("Enter no. of columns of matrix (integers only): "))
    while True:
        print("Please enter a row, with all numbers seperated by commas. Enter 'end' once the matrix is finished.")
        unrefinedRow = input("")
        listedRow = unrefinedRow.strip().split(",")
        if unrefinedRow.strip() == 'end':
            matrixfunctions.printMatrix(matrix)
            return matrix
            break
        elif all(is_number(x) for x in listedRow):
            listedRow = [float(x) for x in listedRow]
            if len(listedRow) == columnsize:
                matrix.append(listedRow)
                matrixfunctions.printMatrix(matrix)
            else:
                print("Incorrect no. of columns, please try again.")
            continue
        else:
            print("Invalid input")

def is_number(string_to_check):
    try:
        float(string_to_check)
        return True
    except ValueError:
        return False
    

def main():
    
    print("Welcome to the MatrixCalculator.")
    print("Enter '+' to add, '-' to subtract, 'REF' to get echelon form, and 'RREF' to get reduced row echelon form.")
    print("Enter 'AB' to solve a matrix equation of the form Ax=B.")
    operation = input("Enter operation symbol: ")
    if operation.strip() == '+':
        matrixAddList = []
        print("Enter 'cont' to input another matrix after the first 2. Enter 'end' to perform the addition operation.")
        matrix1 = enterMatrix()
        matrix2 = enterMatrix()
        while True:
            check = input("")
            matrixAddList.append(matrix1)
            matrixAddList.append(matrix2)
            if check.strip() == 'cont':
                newMatrix = enterMatrix()
                matrixAddList.append(newMatrix)
            elif check.strip() == 'end':
                matrixfunctions.printMatrix(matrixfunctions.matrixAddition(*matrixAddList))
                break
            else:
                print("Invalid input, please try again.")
                continue
    elif operation.strip() == '-':
        matrixSubtractList = []
        print("Enter 'cont' to input another matrix after the first 2. Enter 'end' to perform the subtraction operation.")
        matrix1 = enterMatrix()
        matrix2 = enterMatrix()
        while True:
            check = input("")
            matrixAddList.append(matrix1)
            matrixAddList.append(matrix2)
            if check.strip() == 'cont':
                newMatrix = enterMatrix()
                matrixAddList.append(newMatrix)
            elif check.strip() == 'end':
                matrixfunctions.printMatrix(matrixfunctions.matrixSubtraction(*matrixSubtractList))
                break
            else:
                print("Invalid input, please try again.")
                continue
    elif operation.strip().lower() == "ref":
        matrix = enterMatrix()
        matrixfunctions.createEchelonForm(matrix)
        matrixfunctions.printMatrix(matrix)
    elif operation.strip().lower() == "rref":
        matrix = enterMatrix()
        matrixfunctions.createRREF(matrix)
        matrixfunctions.printMatrix(matrix)
    elif operation.strip().lower() == "ab":
        print("Please enter A and B in order.")
        a = enterMatrix()
        b = enterMatrix()
        matrixfunctions.solveMatrixEquation(a, b)

main()

            
