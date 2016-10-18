"""
Auxiliary module for the Hack Assembler.
Purposed to proceed the assembly command parsing.

created by RinSer
"""

# Command constants
A_COMMAND = 'A'
L_COMMAND = 'L'
C_COMMAND = 'C'


class Parser:
    """
    Module to read the assembly input 
    and parse it.
    """
    def __init__(self, file_path):
        self.asm_file = open(file_path, 'r')
        self.new_line = 'initial'
        
    def hasMoreCommands(self):
        """
        Method to check if the assemblage 
        file is not over.
        Returns boolean value.
        """
        return not(self.new_line == '')

    def advance(self):
        """
        Method to advance the file pointer.
        Returns nothing.
        """
        self.new_line = self.asm_file.readline()
        while self.new_line in ('\n', '\r\n'):
            self.new_line = self.asm_file.readline()
        line_split = self.new_line.split()
        if len(line_split) > 0:
            self.new_line = line_split[0]

    def commandType(self):
        """
        Method to check the current commant type.
        Returns the command type.
        """
        if len(self.new_line) > 1:
            if self.new_line[0] == '@':
                return A_COMMAND
            elif self.new_line[0] == '(':
                return L_COMMAND
            elif self.new_line != '//':
                return C_COMMAND

    def symbol(self):
        """
        Method to return the symbol from a given 
        L_COMMAND command.
        Returns the symbol as string.
        """
        return self.new_line[1:-1]

    def address(self):
        """
        Method to return the address from a given 
        A_COMMAND.
        Returns decimal integer.
        """
        return self.new_line[1:]

    def dest(self):
        """
        Method to return the destination from a given 
        C_COMMAND.
        Returns dest mnemonic as string.
        """
        command = self.new_line.split('=')
        if len(command) > 1:
            return command[0]
        else:
            return None

    def comp(self):
        """
        Method to return the computation from a given 
        C_COMMAND.
        Returns comp mnemonic as string.
        """
        command = self.new_line.split('=')
        if len(command) > 1:
            cmd = command[1].split(';')[0]
        else:
            cmd = command[0].split(';')[0]
        return cmd

    def jump(self):
        """
        Method to return the jump from a given 
        C_COMMAND.
        Returns jump mnemonic as string.
        """
        command = self.new_line.split(';')
        if len(command) > 1:
            return command[1]
        else:
            return None

    def destroy(self):
        """
        Method to uninitialize a parser.
        """
        self.asm_file.close()


