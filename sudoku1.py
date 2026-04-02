import sys
import clingo
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
        #extract symbols
        symbols = model.symbols(shown=True)
        #sort the symbols extracted
        symbols = sorted(symbols, key=str)
        #print them all as a line
        print(" ".join(map(str, symbols)))

if __name__ == "__main__":
#run
    clingo.clingo_main(SudokuApp(), sys.argv[1:])