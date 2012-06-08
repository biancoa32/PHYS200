from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob

#def square(t,l):
#	for i in range(4):
#		fd(t,l)
#		lt(t)
	
#square(bob,60)

def polygon(t,l,n):
	for i in range(n):
		fd(t,l)
		lt(t,360.0/n)
		
#polygon(bob,100,3)

def circle(t,r):
	c = 2*pi*r
	n = l/c
	polygon(t,l,n)
	
circle(bob,2)