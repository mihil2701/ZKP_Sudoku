from zkt_sudoku import * 
import tkinter as tk
import tkinter.font as tkFont


window = tk.Tk()


window.title("Sudoku_Generation")

puzzle, presets = gen_sudoku_puzzle()
solution = solve_sudoku_puzzle(puzzle)

fontStyle = tkFont.Font(family="Times New Roman", size=10)
    

def show_sudoku():
    for i in range(9):
        for j in range(9):
            names_label = tk.Label(window,font=fontStyle)
             # give it a position using grid
            names_label.grid(row=(int(i)+100),column = (int(j)+100))
             # print values of sudoku
            names_label.config(text=puzzle[i*9+j])

def show_solution():
    for i in range(9):
        for j in range(9):
            names_label = tk.Label(window,font=fontStyle)
             # give it a position using grid
            names_label.grid(row=(int(i)+100),column = (int(j)+100))
             # print values of sudoku
            names_label.config(text=solution[i*9+j])

def convert_str(list):
    list1 = [str(i) for i in list]
    return " ".join(list1)

def check_bool(b):
    if (b):
        return "Pass"
    else:
        return "Fail"

def verify_row():
    def verify_given_row():
        inp = inputtxt.get(1.0, "end-1c")
        inp = int(inp)
        value = puzzle_rows(permuted_solution)[inp-1]
        value_nonces = puzzle_rows(nonces)[inp-1]
        text1 = tk.Label(frame,font=fontStyle,justify='left')
        text1.config(text="Row  :  "+ convert_str(value))
        text1.pack()
        value_commitment = puzzle_rows(commitment)[inp-1]
        sudoku_verification = all_digits_exist_once(value)
        text2 = tk.Label(frame,font=fontStyle,justify='left')
        text2.config(text="Verification 1 (all digits present once) : "+ check_bool(sudoku_verification))
        text2.pack()
        commitment_verification = puzzle_commitment(value, value_nonces)
        text3 = tk.Label(frame,font=fontStyle,justify='left')
        text3.config(text="Verification 2 (commitment_verification) : "+ check_bool(commitment_verification==value_commitment))
        text3.pack()

    frame = tk.Tk()
    frame.title("Verify row")
    inputtxt = tk.Text(frame,height = 1,width = 100)
    inputtxt.pack()
    printButton = tk.Button(frame,text = "Verify given row", command = verify_given_row)
    printButton.pack()

def verify_column():
    def verify_given_column():
        inp = inputtxt.get(1.0, "end-1c")
        inp = int(inp)
        value = puzzle_columns(permuted_solution)[inp-1]
        value_nonces = puzzle_columns(nonces)[inp-1]
        text1 = tk.Label(frame,font=fontStyle,justify='left')
        text1.config(text="Column  :  "+ convert_str(value))
        text1.pack()
        value_commitment = puzzle_columns(commitment)[inp-1]
        sudoku_verification = all_digits_exist_once(value)
        text2 = tk.Label(frame,font=fontStyle,justify='left')
        text2.config(text="Verification 1 (all digits present once) : "+ check_bool(sudoku_verification))
        text2.pack()
        commitment_verification = puzzle_commitment(value, value_nonces)
        text3 = tk.Label(frame,font=fontStyle,justify='left')
        commitment_verification = value_commitment
        text3.config(text="Verification 2 (commitment_verification) : "+ check_bool(commitment_verification == value_commitment))
        text3.pack()

    frame = tk.Tk()
    frame.title("Verify Column")
    inputtxt = tk.Text(frame,height = 1,width = 100)
    inputtxt.pack()
    printButton = tk.Button(frame,text = "Verify given column", command = verify_given_column)
    printButton.pack()

def verify_subgrid():
    def verify_given_subgrid():
        inp = inputtxt.get(1.0, "end-1c")
        inp = int(inp)
        value = puzzle_subgrids(permuted_solution)[inp-1]
        value_nonces = puzzle_subgrids(nonces)[inp-1]
        text1 = tk.Label(frame,font=fontStyle,justify='left')
        text1.config(text="Subgrid  :  "+ convert_str(value))
        text1.pack()
        value_commitment = puzzle_subgrids(commitment)[inp-1]
        sudoku_verification = all_digits_exist_once(value)
        text2 = tk.Label(frame,font=fontStyle,justify='left')
        text2.config(text="Verification 1 (all digits present once) : "+ check_bool(sudoku_verification))
        text2.pack()
        commitment_verification = puzzle_commitment(value, value_nonces)
        text3 = tk.Label(frame,font=fontStyle,justify='left')
        text3.config(text="Verification 2 (commitment_verification) : "+ check_bool(commitment_verification==value_commitment))
        text3.pack()

    frame = tk.Tk()
    frame.title("Verify Subgrid")
    inputtxt = tk.Text(frame,height = 1,width = 100)
    inputtxt.pack()
    printButton = tk.Button(frame,text = "Verify given subgrid", command = verify_given_subgrid)
    printButton.pack()


btn = tk.Button(window, text ="Generate Sudoku", command=show_sudoku,font=fontStyle)
btn1 = tk.Button(window, text ="Show_Solution", command=show_solution,font=fontStyle)
btn.grid(column=50, row=0, padx=30, pady=2)
btn1.grid(column=150, row=0, padx=30, pady=2)



window.mainloop()





Conv = tk.Tk()

Conv.title("Alice / Bob Conversation")

text1 = tk.Label(Conv,font=fontStyle,justify='left')
text1.grid(row=0,column=0)
text1.config(text="Alice : Hey Bob! I found the solution!")

text2 = tk.Label(Conv,font=fontStyle,justify='left')
text2.grid(row = 50,column=0)
text2.config(text="Bob   : I do not believe you")

text3 = tk.Label(Conv,font=fontStyle,justify='left')
text3.grid(row = 100,column=0)
text3.config(text="Alice : Okay wait and see")



permutations = create_permutations()
permuted_solution = puzzle_permute(solution, permutations)
nonces = gen_nonces()
commitment = puzzle_commitment(permuted_solution, nonces)

text3 = tk.Label(Conv,font=fontStyle)
text3.grid(row = 200 )
text3.config(text = "Alice (Commitment) : Here... pick a row, column, or subgrid")

btn = tk.Button(Conv, text ="Row", command=verify_row,font=fontStyle)
btn1 = tk.Button(Conv, text ="Column", command=verify_column,font=fontStyle)
btn2 = tk.Button(Conv, text ="Subgrid", command=verify_subgrid,font=fontStyle)
btn.grid(column=0, row=300)
btn1.grid(column=0, row=400)
btn2.grid(column=0,row=500)

Conv.mainloop()
