import random

# traditional pooling
def traditional(prevalence, poolsize):
	clear = 0
	for a in range(poolsize):
		if random.random() < prevalence:
			clear += 1
		if clear > 0:
			return poolsize
	return 0

# matrix pooling
def matrix(prevalence, matrixsize):
	retests = 0
	return retests

# this is not important right now
def generatetray(trayx, trayy):
	display = ""
	for i in range(trayy):
		for k in range (trayx):
			display += "[ ]"
		display += "\n"
	return display

def main():
	i = 0
	#for a in range(92):
	for a in range(9200000):
		i += traditional(0.05, 2)
	print(i)
	print(i/100000)

main()

