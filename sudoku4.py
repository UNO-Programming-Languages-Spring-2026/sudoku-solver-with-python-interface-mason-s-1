import sys
import clingo
#new import from sudoku_board here
from sudoku_board import Sudoku
class SudokuApp(clingo.Application):
    program_name = "sudoku"
    def main(self, contr, file):
        #load the encoding and input
        contr.load("sudoku.lp")
        for i in file:
            contr.load(i)
        #ground it and solve with basic clingo
        contr.ground([("base", [])])
        contr.solve()
    def print_model(self, model, printer):
        #\/\/\/\/\/\/\/\/new stuff here, everything else same as sudoku1\/\/\/\/\/\/\\
        sudoku = Sudoku.from_model(model)
        print(sudoku)

if __name__ == "__main__":
#run
    clingo.clingo_main(SudokuApp(), sys.argv[1:])