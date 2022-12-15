from typing import List

grid_1 = [[2, 4, 4, 2], [4, 3, 5, 6], [4, 6, 8, 6], [2, 7, 2, 3]]
grid_2 = [[2, 4, 3], [4, 4, 4], [3, 4, 1]]
grid_3 = [[4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4]]

def find_matches(grid: List[List[int]]) -> int:
    '''
    Функция, которая считает кол-во строк, которые равны столбцам.
    :param grid: матрица (список строк)
    :return: кол-во строчек, которые равны столбцам
    '''

    result = 0
    size_matrix = len(grid) - 1
    for item in grid:

        st = 0
        col = 0
        count = 0

        while True:
            if item[col] == grid[col][st] :
                count += 1
            else:
                if st == size_matrix:
                    break
                st += 1
                col = 0
                continue

            if st == size_matrix and col == size_matrix:
                break

            if col == size_matrix:
                st += 1
                col = 0
            else:
                col += 1

        result += count // (size_matrix + 1)

    return result

print(find_matches(grid_1))
print(find_matches(grid_2))
print(find_matches(grid_3))