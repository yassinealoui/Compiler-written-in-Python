from lex import *
from emit import *
from parse import *
import sys

def main():
    print("Compy Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument"
                 "( write this: "
                 "python compy.py \"nom de fichier a compiler\".txt)")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()

    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(input)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser.
    emitter.writeFile() # Write the output to file.
    print("Compiling completed.")
	
main()

