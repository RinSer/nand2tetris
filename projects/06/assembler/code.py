"""
Auxiliary module for the Hack Assembler.
Purposed to store translate Hack assembly language 
mnemonics into binary codes.

created by RinSer
"""

# C_COMMAND first 3 bits
C_CMD = '111'

# Dictionaries containing mnemonic translations
COMP = {'0':'0101010', '1':'0111111', '-1':'0111010', 'D':'0001100', 'A':'0110000', 
	'!D':'0001101', '!A':'0110001', '-D':'0001111', '-A':'0110001', 'D+1':'0011111', 
	'A+1':'0110111', 'D-1':'0001110', 'A-1':'0110010', 'D+A':'0000010', 'D-A':'0010011', 
	'A-D':'0000111', 'D&A':'0000000', 'D|A':'0010101', 'M':'1110000', '!M':'1110001', 
	'-M':'1110011', 'M+1':'1110111', 'M-1':'1110010', 'D+M':'1000010', 'D-M':'1010011', 
	'M-D':'1000111', 'D&M':'1000000', 'D|M':'1010101'}

DEST = {'M':'001', 'D':'010', 'MD':'011', 'A':'100', 'AM':'101', 'AD':'110', 'AMD':'111'}

JUMP = {'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100', 'JNE':'101', 'JLE':'110', 'JMP':'111'}


class Code:
    """
    Module to translate an assembly line 
    into binary code.
    """
    def __init__(self):
        self.compD = dict(COMP)
        self.destD = dict(DEST)
        self.jumpD = dict(JUMP)
        self.cmd = C_CMD

    def symbol(self, symbol):
        """
        Method to translate symbol value 
        into binary value.
        Returns the symbol binary string.
        """
        binary = bin(int(symbol))[2:]
        while len(binary) < 16:
            binary = '0'+binary
        return binary

    def comp(self, mnemonic):
        """
        Method to map comp mnemonic translations
        with binary values.
        Returns the comp binary.
        """
        return self.compD[mnemonic]

    def dest(self, mnemonic):
        """
        Method to map dest mnemonic translations 
        with binary values.
        Returns the dest binary.
        """
        if mnemonic == None:
            return '000'
        else:
            return self.destD[mnemonic]

    def jump(self, mnemonic):
        """
        Method to map jump mnemonic translations 
        with binary values.
        Returns the jump binary.
        """
        if mnemonic == None:
            return '000'
        else:
            return self.jumpD[mnemonic]

    def c_cmd(self):
        """
        Method to return the C_COMMAND first 3 bits.
        Returns the binary string.
        """
        return self.cmd


