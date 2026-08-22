
import matrixfunctions
def fillRow(row):
            matrix = []
            while True:
                entry = input("Enter a number: ")
                if entry == "":
                    print("Nothing entered.")
                    continue
                elif entry.startswith("-"):
                    modentry = entry[1:]
                    a = entry[1:].split(".")
                else:
                    modentry = entry
                    a = entry.split(".")
                if modentry.isdigit() or (all(x.isdigit()
                                            for x in a) and len(a) == 2):
                    row.append(float(entry))
                elif entry.lower() == 'row':
                    if row == []:
                        print("Row cannot be empty. Please try again.")
                    elif len(matrix) >= 1 and len(row) == len(matrix[len(matrix)-1]):
                        matrix.append(row)
                    elif len(matrix) == 0:
                         matrix.append(row)
                    else:
                        print("Invalid row length. Please input your row again.")
                        continue
                    newRow = []
                    fillRow(newRow)
                elif entry.lower() == 'end':
                    matrix.append(row)
                    return matrix
                    break
                elif entry.lower() == 'end' and len(matrix[0]) == 0:
                    print("Invalid entry, empty matrix.")
                else:
                     print("Invalid entry, integers, floats or appropriate keywords only.")
                

def main():
    print("Welcome to the Matrix Calculator. In order to build your matrix, enter a number.")
    print("This will create a row in the matrice. Any number enterred after this one will be a part of this row, until you enter 'row' to create a new row" \
    "Enter 2 matrices for addition and substraction." \
    "Enter 1 matrice for row reduction."
    )
    print("Enter 'end' to finish your matrix.")
    matricesList = []
    matrix1 = fillRow([])
    matricesList.append(matrix1)
    while True:
         moreMatrices = input("Would you like to input another matrice? y/n: ")
         if moreMatrices.strip() == "y":
            matrix1 = fillRow([])
         elif moreMatrices.strip() == "n":
              while True:
                    if len(matricesList) == 2:
                        addOrSubstract = input("Enter 'add' to add 2 matrices. Enter 'substract' to substract a matrice from another.")
                        matrix1 = matricesList[0]
                        matrix2 = matricesList[1]
                        if addOrSubstract == 'add':
                            print(matrixfunctions.matrixAddition(matrix1, matrix2))
                        elif addOrSubstract == 'substract':
                            print(matrixfunctions.matrixSubstraction(matrix1, matrix2))
                        break
                    elif len(matricesList) == 1:
                        print(matrixfunctions.createEchelonForm(matricesList[0]))
                        break
         else:
              print("Invalid input. Please try again.")
main()

