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
    if len(argv) > 0 and len(argv) < 3:
        if argv[0].split('.')[-1] != 'asm':
            print 'Wrong input file extension!'
        else:
            input_file = argv[0]
        if len(argv) < 2:
            output_file = argv[0].split('asm')[0] + 'hack'
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
    # First run: symbol recognition
    symbols = symbol_table.SymbolTable()
    symbol_parser = parser.Parser(input_file)
    line = 0
    while symbol_parser.hasMoreCommands():
        symbol_parser.advance()
        if symbol_parser.commandType() == 'A':
            line += 1
        elif symbol_parser.commandType() == 'L':
            symbol = symbol_parser.symbol()
            if not symbols.contains(symbol):
                symbols.addEntry(symbol, line)
        elif symbol_parser.commandType() == 'C':
            line += 1
    symbol_parser.destroy()
    # Second run: the assemblage 
    code_parser = parser.Parser(input_file)
    coder = code.Code()
    output = open(output_file, 'w')
    while code_parser.hasMoreCommands():
        code_parser.advance()
        if code_parser.commandType() == 'A':
            address = code_parser.address()
            if not address.isdigit():
                if symbols.contains(address):
                    address = symbols.GetAddress(address)
                else:
                    symbols.addEntry(address, symbols.getFreeRAM())
                    address = symbols.getFreeRAM()
                    symbols.incFreeRAM()
            binary = coder.symbol(address)
            output.write(binary+'\n')
        elif code_parser.commandType() == 'C':
            binary = coder.c_cmd()+coder.comp(code_parser.comp())+coder.dest(code_parser.dest())+coder.jump(code_parser.jump())
            output.write(binary+'\n')
    output.close()
    code_parser.destroy()
    return 0
    
    
def main(argv):
    """
    Main function to control the cmd arguments.
    """
    if len(argv) < 1 or len(argv) > 2:
        print 'Usage: ./hack_assembler.py </PATH_TO/input_file.asm> [</PATH_TO/output_file.hack>]'
        

if __name__ == '__main__':
    main(sys.argv[1:])
    assembler(sys.argv[1:])

