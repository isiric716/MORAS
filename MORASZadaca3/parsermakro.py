# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:23:02 2025

@author: Ivona
"""

def _parse_macros(self):
	self._iter_lines(self._parse_macro)


def _mv(self, A, B):
	lines = ["@" + A, "D=M", "@" + B, "M=D"]
	return lines

def _swp(self, A, B):
	lines = ["@temp", "M=0", "@" + A, "D=M", "@temp", "M=D", "@" + B, "D=M", "@" + A, "M=D", "@temp", "D=M", "@" + B, "M=D"]
	return lines

def _add(self, A, B, D):
	lines = ["@" + A, "D=M", "@" + B, "D=D+M", "@" + D, "M=D"]
	return lines

def _while(self, A):
	self._nest += 1
	lines = ["(WHILE" + str(self._nest) + ")", "@" + A, "D=M", "@END" + str(self._nest), "D;JEQ"] # otvara petlju i stavlja zaustavni uvjet while RAM[A] != 0
	return lines
	
def _parse_macro(self, line, o, p):
	if line[0] == "$":
		command = line[1:].split("(")
		macro = command[0]
		
		if len(command) > 1:
			args = command[1]
			args_list = args.replace(")", "").split(",")
		
			if macro == "MV":
				lines = self._mv(args_list[0], args_list[1])
				return lines
			
			elif macro == "SWP":
				lines = self._swp(args_list[0], args_list[1])
				return lines
			
			elif macro == "ADD":
				lines = self._add(args_list[0], args_list[1], args_list[2])
				return lines

			elif macro =