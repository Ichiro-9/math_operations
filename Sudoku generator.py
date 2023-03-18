import random
sudoku = [];rows = {}; columns ={}
numbers = list(range(1,10))
def randomsudoku():
    global sudoku,rows,columns
    sudoku = []
    for x in range(3):
        sub = []
        for x in range(3):
            sub2 = []
            while True:
                a = random.randint(1,9)

                if a not in sub2 :sub2.append(a)
                if len(sub2)==9:break
            sub.append(sub2)
        sudoku.append(sub)
    rows = {'row1':sudoku[0],'row2':sudoku[1],'row3':sudoku[2]}
    columns = {}
    for x in range(0,9):
        ele=[]
        for a in range(0,3):
            for b in range(0,3):ele.append(sudoku[a][b][x])
        columns[f'col{x+1}'] = ele
def left(list1):
    for num in range[1,9]:
        if num not in list1:
            return num

def alltrue(vert):
    randomsudoku()
    nottrue = []
    for x in range(0,9):
        if len(columns[f'col{x+1}']) != len(set(columns[f'col{x+1}'])):
            nottrue.append(f'col{x+1}')
    for key in nottrue:
        for x in numbers:
            duplicate = columns[key].count(x)


alltrue(4)