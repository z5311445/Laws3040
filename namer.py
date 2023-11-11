import sys
import string
import random
from names_generator import generate_name

#assumed argv is int indicating number of names to be generated 
def main(argv):
	#customerNamer(argv)
	employeeNamer(argv)

# Creates a text file of customers, n=argv (n assumed int)
def customerNamer(argv):
	with open('CustomersV2-.txt', 'w') as f:
		i = 1
		while i <= int(argv):
			f.write("(" + str(i) + ", ")
			firstName = firstNamer()
			lastName = lastNamer()
			f.write("'" + firstName + "', ")
			f.write("'" + lastName + "', ")
			f.write("'" + usernamer(i, firstName, lastName) + "', ")
			f.write("'" + basicPassworder(6) + "'),\n")
			i += 1

# Creates a text file of employees, n=argv (n assumed int)
def employeeNamer(argv):
	with open('EmployeesV2.txt', 'w') as f:
		i = 1
		while i <= int(argv):
			f.write("(" + str(i) + ", ")
			firstName = firstNamer()
			lastName = lastNamer()
			f.write("'" + firstName + "', ")
			f.write("'" + lastName + "', ")
			f.write("'" + usernamer(i, firstName, lastName) + "', ")
			f.write("'" + basicPassworder(6) + "', ")
			if random.randint(1,10) > 8:
				f.write("'" + str(True) + "'),\n")
			else:
				f.write("'" + str(False) + "'),\n")
			i += 1

# First name is three letter string with vowel in the middle
def firstNamer():
	ret_string = ''
	ret_string += random.choice(string.ascii_letters).upper()
	ret_string += random.choice('aeiou')
	ret_string += random.choice(string.ascii_letters).lower()

	return ret_string


def lastNamer():
	ret_string = ''
	ret_string += generate_name()
	ret_string = ret_string.replace(ret_string[0],ret_string[0].upper(),1)
	return ret_string
	
# Returns username, which is concat of id, firstName and lastName
def usernamer(id, firstName, lastName):
	return str(id) + firstName + lastName

def basicPassworder(len):
	return ''.join(random.choice(string.ascii_letters) for i in range(len))

if __name__ == "__main__":
	main(sys.argv[1])
