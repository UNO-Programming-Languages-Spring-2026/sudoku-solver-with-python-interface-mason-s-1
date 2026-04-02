from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
        for i in range(1,10):
                rows = []
                #grab values for all columns in row
                for a in range(1,10):
                        rows.append(str(self.sudoku[(i,a)]))
                #format it all
                s += " ".join(rows[0:3]) + "  " + " ".join(rows[3:6]) + "  " + " ".join(rows[6:9])
                #this part below and above (using += to append it) is like the example you gave at the start of the semester
                #I think you said it was an accident of the author, cool to use it haha.
                #newline for each row (not last)
                if i != 9:
                        s += "\n"
                #extra line every 3 rows (match a sudoku board)
                if i in [3,6]:
                        s += "\n"
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        which_row=1
        #.splitlines() is pretty cool, automatically takes a string with mutiple lines and makes a list including each line
        lines=s.splitlines()
        #increment through each line in lines, skip all blank lines
        for i in lines:
                if i.strip()=="":
                        continue
                which_column = 1
                split_lines = i.split()
                #go through and ignore each empty cell
                for a in split_lines:
                        if a != "-":
                                sudoku[(which_row, which_column)]=int(a)
                        #increments to change the rows and columns we are in
                        which_column +=1
                which_row += 1
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        for i in model.symbols(shown=True):
                sudoku[(i.arguments[0].number, i.arguments[1].number)] = i.arguments[2].number
        return cls(sudoku)
