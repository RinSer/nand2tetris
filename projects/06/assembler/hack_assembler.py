#!/usr/bin/env python
"""
Assembler for the hack computer.
nand2tetris course assignment implementation.

created by RinSer
"""

import sys
import code
import parser
import symbol_table


def assembler(argv):
    """
    Function to proceed the assemblage.
    """
    input_file = None
    output_file = None
    # Get the cmd arguments
    if len(argv) > 0 and len(argv) < 2:
        if argv[0].split('.')[-1] != 'asm':
            print 'Wrong input file extension!'
        else:
            input_file = argv[0]
        if len(argv) < 2:
            output_file = argv[0].split('.')[0] + '.hack'
        else:
            if argv[1].split('.')[-1] != 'hack':
                print 'Wrong output file extension!'
            else:
                output_file = argv[1]
    # Check the files
    if input_file == None or output_file == None:
        print 'Invalid input or output file!'
        return 1
    # Initialize the assemblage
    new_parser = parser.Parser(input_file)
    line = 0
    while new_parser.hasMoreCommands():
        new_parser.advance()
        if new_parser.commandType() == 'A':
            print line, new_parser.address()
            line += 1
        elif new_parser.commandType() == 'L':
            print line, new_parser.symbol()
            line+= 1
        elif new_parser.commandType() == 'C':
            print line, new_parser.comp(), new_parser.dest(), new_parser.jump()
            line += 1
    
    

def main(argv):
    """
    Main function to control the cmd arguments.
    """
    if len(argv) < 1 or len(argv) > 2:
        print 'Usage: ./hack_assembler.py </PATH_TO/input_file.asm> [</PATH_TO/output_file.hack>]'
        

if __name__ == '__main__':
    main(sys.argv[1:])
    assembler(sys.argv[1:])

