'''
	This program show basic string operations.
'''

if __name__ == '__main__':
	
	string = raw_input("Enter any string :")
	print "input string is :%s"%string
	print "length of string:%s"%len(string)
	print "reverse string  :%s"%string[::-1]
	print "capitalize string:%s"%string.capitalize()
	print "upper case string:%s"%string.upper()
	print "lower case string:%s"% string.lower()
	print "split string     :%s"% string.split() #default is space delimiter

	
	
