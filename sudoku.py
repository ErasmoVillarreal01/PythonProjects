def check_sudoku(grid):
if len(grid) == 9:
    numsinrow = 0
    for i in range(9):
        if len(grid[i]) == 9:
            numsinrow += 1
    if numsinrow == 9:
        for i in range(9):
            rowoccurence = [0,0,0,0,0,0,0,0,0,0]
            for j in range(9):
                rowoccurence[grid[i][j]] += 1
                temprow = rowoccurence[1:10]
                if temprow == [1,1,1,1,1,1,1,1,1]:
                    return True
                else:
                    return False
    else:
        return False



print(check_sudoku())