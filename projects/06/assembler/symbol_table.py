"""
Auxiliary module for the Hack Assembler.
Purposed to store the symbol data.

created by RinSer
"""

# Predefined Symbols Table
PREDEFINED_SYMBOLS = {'SP':0, 'LCL':1, 'ARG':2, 'THIS':3, 'THAT':4, 'R0':0, 'R1':1, 'R2':2, 'R3':3, 'R4':4, 'R5':5, 'R6':6, 'R7':7, 'R8':8, 'R9':9, 'R10':10, 'R11':11, 'R12':12,'R13':13, 'R14':14, 'R15':15, 'SCREEN':16384, 'KBD':24576}


class SymbolTable:
    """
    Module to store the Symbol Table.
    Contains a dictionary with symbol, address pairs
    """
    def __init__(self):
        self.table = dict(PREDEFINED_SYMBOLS)
        self.free_ram = 16

    def contains(self, symbol):
        """
        Method to check if a symbol is already 
        in the table.
        Returns boolean value.
        """
        if symbol in self.table:
            return True
        else:
            return False
        
    def addEntry(self, symbol, address):
        """
        Method to add entries into the table.
        Returns nothing.
        """
        if not self.contains(symbol):
            self.table[symbol] = address

    def GetAddress(self, symbol):
        """
        Method to retrieve address corresponding 
        to given symbol from the table.
        Returns the address value.
        """
        if self.contains(symbol):
            return self.table[symbol]

    def getFreeRAM(self):
        """
        Method to return the free RAM address.
        Returns the address as a string.
        """
        return self.free_ram

    def incFreeRAM(self):
        """
        Method to increment the free RAM address.
        Returns nothing.
        """
        self.free_ram += 1

    def __str__(self):
        return self.table

