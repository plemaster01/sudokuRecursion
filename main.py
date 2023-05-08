import numpy

puzzle = [[0, 0, 0, 0, 0, 0, 0, 2, 8],
           [0, 6, 0, 0, 0, 0, 0, 0, 7],
           [0, 0, 0, 4, 0, 1, 0, 0, 0],
           [5, 0, 0, 9, 7, 0, 3, 0, 0],
           [2, 0, 4, 0, 0, 8, 0, 0, 0],
           [3, 0, 0, 0, 0, 4, 5, 0, 0],
           [1, 3, 0, 0, 9, 0, 0, 0, 0],
           [0, 5, 7, 0, 0, 0, 0, 9, 0],
           [0, 0, 8, 3, 1, 7, 0, 0, 0]]

puzzle2 = [[0, 0, 0, 4, 0, 1, 0, 0, 6],
          [0, 0, 3, 0, 0, 8, 0, 9, 0],
          [0, 7, 0, 0, 6, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 6, 0, 0, 0],
          [0, 0, 9, 0, 0, 0, 0, 4, 0],
          [3, 4, 0, 2, 0, 0, 6, 0, 5],
          [0, 0, 0, 0, 0, 5, 0, 8, 0],
          [0, 9, 0, 0, 1, 0, 7, 0, 0],
          [4, 0, 0, 0, 0, 7, 0, 0, 3]]


def valid(row, col, value):
    # check row, column, then 3xx3 block
    global puzzle
    for i in range(0, 9):
        if puzzle[row][i] == value:
            return False
    for i in range(0, 9):
        if puzzle[i][col] == value:
            return False
    x_start = (col // 3) * 3
    y_start = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if puzzle[y_start + i][x_start + j] == value:
                return False
    return True


def iterate():
    global puzzle
    for i in range(0, 9):
        for j in range(0, 9):
            if puzzle[i][j] == 0:
                for num in range(1, 10):
                    if valid(i, j, num):
                        puzzle[i][j] = num
                        iterate()
                        puzzle[i][j] = 0

                return

    print(numpy.matrix(puzzle))


iterate()
