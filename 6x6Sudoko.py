#Program to solve 6x6 Sudoko

def input_lst():
    "Function to input the sudoko table"
    fix_lst=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    for i in range(6):
        for j in range(6):
            fix_lst[i][j]=int(input("Enter digit (0 if blank)"))
    return fix_lst

def validity_check (lst,i,j):
    "Function to check validity of newly added number"
    ok = 1 
    row = [0,1,2,3,4,5]
    row.remove(i)
    column = [0,1,2,3,4,5]
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
        if i==5 and j==5:
            print(sudoko_copy)
        else:
            if j==5:
                backtrack(sudoko_copy,i+1,0)
            else:
                backtrack(sudoko_copy,i,j+1)
    else:
        if i==5 and j==5:
            for k in [1,2,3,4,5,6]:
                sudoko_copy[5][5] = k
                if validity_check(sudoko_copy,i,j):
                    print (sudoko_copy)
            sudoko_copy[5][5] = 0
        else:
            for k in [1,2,3,4,5,6]:
                sudoko_copy[i][j] = k
                if validity_check(sudoko_copy,i,j):
                    if j==5:
                        backtrack(sudoko_copy,i+1,0)
                    else:
                        backtrack(sudoko_copy,i,j+1)
                sudoko_copy[i][j]=0        

k = backtrack([[0,0,0,5,0,6],[0,0,5,0,0,0],[0,0,0,0,3,0],[2,3,4,0,0,0],[0,4,2,0,0,1],[3,5,1,2,0,0]],0,0)
s = backtrack([[0,0,3,0,1,0],[5,6,0,3,2,0],[0,5,4,2,0,3],[2,0,6,4,5,0],[0,1,2,0,4,5],[0,4,0,1,0,0]],0,0)
r = backtrack(  [ [2,0,0,3,4,5] , [5,0,0,1,0,6] ,  [3,0,0,0,5,2]  ,  [0,2,0,0,3,0]  , [0,5,3,2,6,0]  ,  [4,6,0,0,0,3] ] , 0 , 0 )


