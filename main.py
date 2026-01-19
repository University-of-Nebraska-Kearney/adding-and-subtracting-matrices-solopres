def get_matrix()->list:
    row:int = int(input("Enter row size for the matrix: "))
    col:int = int(input("Enter col size for the matrix: "))
    if row > 1:
        matrix:list = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                matrix[i][j] = int(input(f"Enter value for position {i+1} {j+1}: "))
    else:
        matrix:list = [0 for _ in range(col)]
        for i in range(col):
            matrix[i] = int(input(f"Enter value for position 1 {i+1}: "))
    return matrix

def add_matrix(matrix1:list, matrix2:list)->list:
    matrix:list = []
    checkdimension1:bool = all(not isinstance(i, list) for i in matrix1)
    checkdimension2:bool = all(not isinstance(i, list) for i in matrix2)
    # Verify matrices
    if (len(matrix1) != len(matrix2) or (not checkdimension1 and checkdimension2)
            or (checkdimension1 and not checkdimension2)):
        print(f"These matrices are not the same dimensions!\nmatrix1: {matrix1}, matrix2: {matrix2}")
        return matrix
    # Matrix is multidimensional
    elif not checkdimension1 and not checkdimension2:
        for i,j in zip(matrix1,matrix2):
            if len(i) != len(j):
                print(f"These matrices are not the same dimensions!\nmatrix1: {matrix1}, matrix2: {matrix2}")
                return []
            temp:list = []
            for x,y in zip(i,j):
                temp.append(x + y)
            matrix.append(temp)
        return matrix
    # Matrix is not multidimensional
    else:
        for i,j in zip(matrix1, matrix2):
            matrix.append(i + j)
    return matrix

def main():
    matrix1:list = get_matrix()
    matrix2:list = get_matrix()
    print(matrix1)
    print(matrix2)
    print(add_matrix(matrix1,matrix2))

if __name__ == '__main__':
    main()
