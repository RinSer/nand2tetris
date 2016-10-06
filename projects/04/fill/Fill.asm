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


(START)
	@KBD  // Load the keyboard value
        D=M

	@BLACKEN  // Black screen if any key is pressed
        D;JNE 

	@8192  // Pixel array index
	D=A

(WHITEN)
	D=D-1  // Decrement the array index

	@SCREEN  // Load the i-th 16 pixels with zeros
	A=A+D
	M=0

	@WHITEN  // Return to the current loop start if the index is not 0
	D;JNE

	@START  // Main loop iteration
	0;JMP

(BLACKEN)
	@8192  // Pixel array index
	D=A

(BLOOP)
	D=D-1  // Decrement the array index

	@SCREEN  // Load the i-th 16 pixels with ones
	A=A+D
        M=-1

	@BLOOP  // Return to the current loop start if the index is not 0
	D;JNE

	@START  // Main loop iteration
	0;JMP

