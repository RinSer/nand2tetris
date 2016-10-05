// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.

// Initialization start
	@R0 // load R0 value
	D=M

	@R3 // create index variable
	M=D

	@R2 // init the mult value to zero
	M=0

	@END
	D;JEQ // do not multiply if the first value is 0

// Initialization end
(WHILE)
	@R2 // load the mult value
        D=M

	@R1 // load the add value
        D=D+M

	@R2 // increase the mult value
        M=D

        @R3 // decrease the index
        M=M-1
	D=M
	@END
	D;JEQ // stop the while loop if the index is 0

	@WHILE
	0;JMP // jump to the loop beggining if index not 0

(END)
	@END
        0;JMP // Infinit loop
	
