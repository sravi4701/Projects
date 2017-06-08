'''
Problem : 
Find PI to the Nth Digit - 
	Enter a number and have the program generate PI up to that many decimal places.
	Keep a limit to how far the program will go.

'''

import math

def pitonthdigit(digit):
	print '%.*f' % (digit, math.pi)

if __name__ == "__main__":
	
	d = 0
	while(True):
		f = True
		try:
			d = int(raw_input('How many digits ? '))
		except Exception:
			f = False
			print("Please Enter only integer value")
		if(d < 50 and f):
			break
		else:
			if(not f):
				print("Please Enter a no. less than 50")

	pitonthdigit(d)