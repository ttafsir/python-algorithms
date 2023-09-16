"""
Write a function that will take 3 arguments:
bombs = list of bomb locations.
rows, columns

mine_sweeper([[0,0], [1,2]], 3, 4)

first bomb at (0,0)
second bomb at (1,2)

1 0 0 0
0 0 1 0
0 0 0 0

we should return a 3x4 array (-1) = bomb
"""
import typing as t


def draw_minefield(field: t.List[t.List[int]]):
    for row in field:
        print("|", end=" ")
        for col in row:
            print(f"{col:2d} |", end="")
        print()


def sweep(bombs: t.List[t.Tuple[int, int]], row_count: int, col_count: int):
    # initialize empty rows. different options
    # mine_field = [[0] * col_count for _ in range(row_count)]
    # mine_field = [[0 for _ in range(col_count)] for _ in range(row_count)]
    mine_field = [[0] * col_count for _ in range(row_count)]

    print("Mine field - Pre-sweep")
    draw_minefield(mine_field)

    # place the bombs
    for row, col in iter(bombs):
        mine_field[row][col] = -1

    print("\nMine field - Active")
    draw_minefield(mine_field)

    for row, col in iter(bombs):
        # we want to consider the surrounding cells
        # for the bomb at (0,0) we want to consider the cells
        # for bomb at (0,0): row_range = (-1, 2); col_range = (-1, 2)
        # for bomb at (1,2): row_range = (0, 3); col_range = (1, 4)
        row_range = range(row - 1, row + 2)
        col_range = range(col - 1, col + 2)

        for r in row_range:
            for c in col_range:
                if (0 <= r < row_count and 0 <= c < col_count) and mine_field[r][
                    c
                ] != -1:
                    mine_field[r][c] += 1

    print("\nMine field - Post-sweep")
    draw_minefield(mine_field)

    return mine_field


sweep(bombs=[(0, 0), (1, 2)], row_count=3, col_count=4)
