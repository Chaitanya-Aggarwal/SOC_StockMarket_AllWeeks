#Program to solve 9x9 Sudoko

def input_lst():
    "Function to input the sudoko table"
    fix_lst=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    for i in range(9):
        for j in range(9):
            fix_lst[i][j]=int(input("Enter digit (0 if blank)"))
    return fix_lst

def validity_check (lst,i,j):
    "Function to check validity of newly added number"
    ok = 1 
    row = [0,1,2,3,4,5,6,7,8]
    row.remove(i)
    column = [0,1,2,3,4,5,6,7,8]
    column.remove(j)
    for k in row:
        if lst[k][j] == lst[i][j]:
            ok = 0
    for k in column:
        if lst[i][k] == lst[i][j]:
            ok = 0
    return ok

def backtrack(sudoko,i,j):
    sudoko_copy = sudoko
    if sudoko_copy[i][j] != 0:
        if i==8 and j==8:
            print(sudoko_copy)
        else:
            if j==8:
                backtrack(sudoko_copy,i+1,0)
            else:
                backtrack(sudoko_copy,i,j+1)
    else:
        if i==8 and j==8:
            for k in [1,2,3,4,5,6,7,8,9]:
                sudoko_copy[8][8] = k
                if validity_check(sudoko_copy,i,j):
                    print (sudoko_copy)
            sudoko_copy[8][8] = 0
        else:
            for k in [1,2,3,4,5,6,7,8,9]:
                sudoko_copy[i][j] = k
                if validity_check(sudoko_copy,i,j):
                    if j==8:
                        backtrack(sudoko_copy,i+1,0)
                    else:
                        backtrack(sudoko_copy,i,j+1)
                sudoko_copy[i][j]=0        

k = backtrack( [ [0,1,5,0,0,2,8,0,9] , [0,0,0,0,0,1,6,0,7] , [0,7,0,0,0,8,4,0,0] , [0,0,6,0,1,7,0,4,5] , [0,5,3,0,0,4,7,0,0] , [8,4,0,0,9,5,0,6,2] , [0,0,4,1,7,0,0,8,6] , [7,6,0,5,2,0,9,1,0] , [5,9,1,0,8,6,0,0,0]  ], 0 ,0 )


