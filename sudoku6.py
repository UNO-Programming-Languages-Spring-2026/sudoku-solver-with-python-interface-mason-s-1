import sys
import clingo
#new import from sudoku_board here
from sudoku_board import Sudoku

class Context:
    def __init__(self, board: Sudoku):
        # YOUR CODE HERE
        self.board = board
    def initial(self) -> list[clingo.symbol.Symbol]:
        # YOUR CODE HERE
        facts = []

        for (a,b), c in self.board.sudoku.items():
            facts.append(
                clingo.Tuple_(
                    (clingo.Number(a),clingo.Number(b),clingo.Number(c))
                )
            )
        return facts




class SudokuApp(clingo.Application):
    program_name = "sudoku"
    def main(self, contr, file):
        #load the encoding and input
        contr.load("sudoku.lp")
        #added this bridging to load
        contr.load("sudoku_py.lp")

        with open(file[0], "r") as f:
             board = Sudoku.from_str(f.read())

        #make into an ojb
        context = Context(board)
        #ground it with python cont and solve with basic clingo
        contr.ground([("base", [])], context=context)
        contr.solve()
    def print_model(self, model, printer):
        #\/\/\/\/\/\/\/\/new stuff here, everything else same as sudoku1\/\/\/\/\/\/\\
        sudoku = Sudoku.from_model(model)
        print(sudoku)

if __name__ == "__main__":
#run
    clingo.clingo_main(SudokuApp(), sys.argv[1:])