// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(START)
	@KBD  // Load the keyboard value
        D=M

	@WHITEN  // Do nothing if no key is pressed
        D;JEQ 

	@8192   // Array index kept in reg D
	D=A

(BLACKEN)
	D=D-1   // Decrement the array index

	@SCREEN
	A=A+D   // Load the ith 16 pixels
        M=-1

	@BLACKEN // Return to the loop start if index is not 0
	D;JNE

	@END   // Skip the whiten loop
	0;JMP

(WHITEN)
	@8192
	D=A  // Array index

(LOOP)
	D=D-1 // Decrement the array index

	@SCREEN
	A=A+D  // Load the ith 16 pixels
	M=-1

	@LOOP // Return to the loop start if index is not 0
	D;JNE

(END)
	@START
        0;JMP // Infinit loop
	
