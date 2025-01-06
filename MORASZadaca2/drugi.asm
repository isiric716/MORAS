
@0
M=0             // Postavi i = 0 (RAM[i])
@5
M=0             // Postavi RAM[5] = 0 (početna vrijednost)

// Početak glavne petlje
(LOOP_START)
    @i
    D=M         
    @4
    D=D-A       
    @LOOP_END
    D;JGT       

   
    @i
    A=M         
    D=M         

    
    @NOT_POS
    D;JLE       

   
    @5
    D=M         
    @UPDATE_MIN
    D;JEQ       
	
    
    @i
    A=M         
    D=M         
    @5
    D=D-M       
    @NOT_MIN
    D;JGE       

    
(UPDATE_MIN)
    @i
    A=M         
    D=M         
    @5
    M=D         

    
(NOT_POS)
(NOT_MIN)
    @i
    M=M+1       
    @LOOP_START 
    0;JMP


(LOOP_END)
(END)
    @END
    0;JMP       

	