import sys
import psycopg2
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas

def main():
	plotGraph();


def simulate():

	# Connect to SAP database
	conn = psycopg2.connect("dbname="+"sap")
	cur = conn.cursor()

	# Ensure only one employee is infected to begin with
	cur.execute("update employees set isInfected=False")
	cur.execute("update employees set isInfected=True where id=1")
	
	#Change variables
	infectionChanceVal = 0.19
	cur.execute("update employees set infectionChance = {};".format(infectionChanceVal))
	interactionsPerDayVal = 46
	cur.execute("update employees set interactionsPerDay = {};".format(interactionsPerDayVal))
	
	# results file to write simulation results to
	tf = open('results.txt', 'a')

	dayCount = 0
	#Loop to simulate days passing
	while dayCount < 100:
		#print("------day is " + str(dayCount))
		
		# for each employee choose (#interactionsPerDay) random employees 
		# if one of those random employees is infected, then that employee is now infected 
		
		# If all employees are infected write to file
		cur.execute('select id from employees where isInfected=False')
		if cur.fetchone() is None:
			tf.write(str(infectionChanceVal) + ', ' + str(interactionsPerDayVal) + ', ' + str(dayCount) +'\n')
			break
				
		cur.execute('select id, "nameFirst", isInfected, infectionChance, interactionsPerDay from employees;')

		#print("Employees not infected: ")
		
		for employee in cur.fetchall():
			id, nameFirst, isInfected, infectionChance, interactionsPerDay = employee

			if isInfected is True:
				# If already infected, pass
				continue
			else:
				empCount = 0
				while empCount < interactionsPerDay:
					# Loop through employees to simulate interaction 
					cur.execute("select id,isInfected from employees order by random() limit 1")
					curEmpId, curEmpInfected = cur.fetchone()

					if curEmpInfected is True:
						if random.random() < infectionChance:
							cur.execute("update employees set isInfected=True where id = {};".format(id))
					empCount += 1

					
			#print(employee)
		dayCount += 1
	conn.close()
	tf.close()
	
def plotGraph():
	points = pandas.read_csv('resultsAvg.csv')

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	x = points['x'].values
	y = points['y'].values
	z = points['z'].values

	ax.scatter(x, y, z, c='r', marker='o')
	plt.show()

def averageResults():
    i = 0
    ic = ''
    ipd = ''
    dc = 0
    sum = 0
    
    with open('results.txt') as f:
        tf = open('resultsAvg.csv', 'w')
        tf.write('avg results')
        for line in f:
            arr = line.split(',')
            if i == 4:
                tf.write(ic + ', ' + ipd + ', '+ str(sum/5) + '\n')
                i =0
                sum = 0
                
            ic = arr[0]
            ipd = arr[1]
            dc = int(arr[2])
            
            sum += dc
            i += 1
    


#MAIN
if __name__ == "__main__":
	main()
