import sys
import string


#assumed fromFileName is in same directory and that toFileName is valid file name, toTableName is the name of the 
def main(fromFileName, toFileName, toTableName):
	# Format the statute so can be inserted to table
	formatter(fromFileName, toFileName, toTableName)



def formatter(fromFileName, toFileName, toTableName):
	with open(fromFileName) as ff:
		tf = open(toFileName, 'w')
		tf.write('insert into \n	' + toTableName + '\nvalues\n')
	
		
		# boolean to check if is the first line
		first = True
		# bodystr needs to be assigned here 
		bodyStr = ''
		
		for line in ff:
			# Check if the first char of line is an int (if at new section)
			if line[0] in '1234567890':
				if first is False:
					# Write to file values before going to next section
					tf.write('("' + secStr +'", "' + titleStr + '", "' + bodyStr + '" ),\n')
				else:
					# Only first time round don't write to file
					first = False
				
				
				# values (resets on each section)
				secStr = ''
				titleStr = ''
				bodyStr = ''
			
				# get section number (can be int or int + char, e.g. 50 or 51B)
				curChar = line[0]
				titleStartIndex = 0
				for char in line:
					if char != ' ':
						secStr += char
					else:
						titleStart = line.index(char)
						titleStr = line[titleStart:]
						break
			else:
				bodyStr += line
		tf.write(';')



if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2], sys.argv[3])

