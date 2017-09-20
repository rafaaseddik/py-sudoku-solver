# -------py-Sudoku-Solver V 0.1
# -------Developped by : Seddik Mohamed Rafaa
# -------------------------------------------


# The inital Grid :
# put 0 for an empty cell
initial_matrix = [
    [8, 0, 1, 0, 2, 4, 6, 0, 3],  # 1
    [0, 0, 0, 0, 6, 8, 0, 9, 0],  # 2
    [6, 0, 0, 9, 0, 0, 4, 0, 7],  # 3

    [0, 0, 7, 0, 3, 0, 0, 0, 9],  # 4
    [0, 4, 9, 0, 0, 0, 3, 6, 0],  # 5
    [1, 0, 0, 0, 9, 0, 2, 0, 0],  # 6

    [4, 0, 2, 0, 0, 9, 0, 0, 6],  # 7
    [0, 7, 0, 3, 5, 0, 0, 0, 0],  # 8
    [3, 0, 8, 6, 4, 0, 9, 0, 5]  # 9
]
# The solution for the given example
solution = [
    [8, 9, 1, 7, 2, 4, 6, 5, 3],
    [7, 3, 4, 5, 6, 8, 1, 9, 2],
    [6, 2, 5, 9, 1, 3, 4, 8, 7],

    [2, 8, 7, 4, 3, 6, 5, 1, 9],
    [5, 4, 9, 2, 7, 1, 3, 6, 8],
    [1, 6, 3, 8, 9, 5, 2, 7, 4],

    [4, 5, 2, 1, 8, 9, 7, 3, 6],
    [9, 7, 6, 3, 5, 2, 8, 4, 1],
    [3, 1, 8, 6, 4, 7, 9, 2, 5]
]


# prints every line separately
def print_matrix(matrix):
    for line in matrix:
        print(line)


# adds value to matrix
def add(matrix, row, col, value):
    matrix[row][col] = value


# transforms every empty cell with a list from 1 to 9 : possibilities
def initialize_lists(matrix):
    result = list(matrix)
    for row in result:
        for col in range(len(row)):
            if (row[col] == 0):
                row[col] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return result


# makes 'value' not in 'row' possibilities
def clear_line(matrix, row, value):
    changes = 0
    for col in range(9):
        if (isinstance(matrix[row][col], list) and value in matrix[row][col]):
            matrix[row][col].remove(value)
            changes += 1
    return changes


# makes 'value' not in 'col' possibilities
def clear_col(matrix, col, value):
    changes = 0
    for row in range(9):
        if (isinstance(matrix[row][col], list) and value in matrix[row][col]):
            matrix[row][col].remove(value);
            changes += 1
    return changes


# makes 'value' not in box containing '' possibilities
def clear_box(matrix, row, col, value):
    changes = 0
    start_box_x = (col // 3) * 3
    start_box_y = (row // 3) * 3
    for i in range(3):
        for j in range(3):
            if (isinstance(matrix[start_box_y + i][start_box_x + j], list) and value in matrix[start_box_y + i][
                    start_box_x + j]):
                matrix[start_box_y + i][start_box_x + j].remove(value)
                changes += 1
    return changes


# transforms single-valued possibilities' list into a valid cell
def refresh(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if (isinstance(matrix[row][col], list) and len(matrix[row][col]) == 1):
                matrix[row][col] = matrix[row][col][0]


def check_solved(matrix):
    for row in matrix:
        for col in row:
            if isinstance(col, list):
                return False
    return True


# This application uses many algorithms to solve the matrix , each algorithm has a level

# LEVEL 1 Algorithm : remove values from possibilities based on row-col-box intersections
def level_1_filter(matrix):
    while not check_solved(matrix):
        refresh(matrix)
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if (isinstance(matrix[row][col], int)):
                    clear_line(matrix, row, matrix[row][col])
                    clear_col(matrix, col, matrix[row][col])
                    clear_box(matrix, row, col, matrix[row][col])


result_matrix = initialize_lists(initial_matrix)
level_1_filter(result_matrix)
print("Result Matrix : ")
print_matrix(result_matrix)
if (solution == result_matrix):
    print("OK")
else:
    print("Not OKs")
