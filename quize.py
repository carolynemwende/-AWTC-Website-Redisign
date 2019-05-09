def smallest(a):
	return min(a)

def reminder(b):
	b=(x%3 for x in range(110,150))
	return b	  
    

def sorted(a,b,c):
	p= a+b+c
	p.sort()
	print (p)


def divisible_by_three(n):
	number= range(1,n+1)
	div=(number/3)
	print (div)


def flatlist(x):
	x= [[1,2],[3,4],[5,6]]
	flatlist=[]
	for sublist in x:
		for number in sublist:
			flatlist.append(number)
			print(flatlist)

def duplicate():
	a=set()
	print(a)


def school():
	student1 = {"age": 12, "name": "emma"}
	student2 = {"age": 19, "name": "vera"}
	student3 =  {"age": 31, "name": "caro"}
	student4 = {"age": 15, "name": "mwende"}

	students = [student1,student2,student3,student4]
	
	for student in students:
		year = 2019-student['age']
		print ("Hello {}, you were born in year {}.".format(student['name'],year))




