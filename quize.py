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





