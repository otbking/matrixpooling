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
def makematrix(prevalence, matrixsize):
	samples = matrixsize ** 2
	m = [0] * samples
	for a in range(samples):
		if random.random() < prevalence:
			m[a] = 1
	return m

def horizontal(inputmatrix, matrixsize):
	hoz = []
	for a in range(matrixsize):
		hoz.append(inputmatrix[(a * matrixsize):((a+1) * matrixsize)])
	return hoz

def vertical(inputmatrix, matrixsize):
	vert = []
	for a in range(matrixsize):
		vert.append([])
		for b in range(matrixsize):
			vert[a].append(inputmatrix[a + (b * matrixsize)])
	return vert

def reducepools(inputpools):
	reduced = [0] * len(inputpools)
	for a in range(len(inputpools)):
		for b in range(len(inputpools[a])):
			if inputpools[a][b] == 1:
				reduced[a] = 1
	return reduced

def matrixretests(reducedhoz, reducedvert, matrixsize):
	r = 0
	hozpositive = 0
	vertpositive = 0
	# assuming a square matrix
	for a in range(matrixsize):
		hozpositive += reducedhoz[a]
		vertpositive += reducedvert[a]
	if hozpositive > 1 and vertpositive > 1:
		r = hozpositive * vertpositive
	return r

def matrixpooling(prevalence, matrixsize):
	m = makematrix(prevalence, matrixsize)
	h = reducepools(horizontal(m, matrixsize))
	v = reducepools(vertical(m, matrixsize))
	p = retestsamples(h, v, matrixsize)
	"""
	print(m)
	print(h)
	print(v)
	printsamples(p)
	"""
	return matrixretests(h, v, matrixsize)

def retestsamples(reducedhoz, reducedvert, matrixsize):
	samples = []
	hozpospools = []
	vertpospools = []
	unequivocal = False
	if matrixretests(reducedhoz, reducedvert, matrixsize) == 0:
		unequivocal = True
	for a in range(matrixsize):
		if reducedhoz[a] == 1:
			hozpospools += [a]
		if reducedvert[a] == 1:
			vertpospools += [a]
	for a in range(len(hozpospools)):
		for b in range(len(vertpospools)):
			samples += [(matrixsize * hozpospools[a]) + vertpospools[b]]
	return [unequivocal, samples]

def printsamples(rsamples):
	if rsamples[0] == True:
		poscount = len(rsamples[1])
		if poscount > 1:
			print("No retests, " + str(poscount) + " positive samples detected: " + str(rsamples[1]))
		elif poscount == 1:
			print("No retests, 1 positive sample detected: " + str(rsamples[1]))
		else:
			print("No retests, no positive samples detected.")
	else:
		print(str(len(rsamples[1])) + " retests: " + str(rsamples[1]))

# this is not important right now
def generatetray(trayx, trayy):
	display = ""
	for i in range(trayy):
		for k in range (trayx):
			display += "[ ]"
		display += "\n"
	return display

def compare(samples, prevalence, tradsize, matrixsize):
	msamples = (matrixsize ** 2)
	core = msamples * tradsize
	slotmulti = (matrixsize * 2)/(msamples/tradsize)
	samples = core - (samples % core) + samples
	trials = int(samples/core)
	i = [0, 0]

	for a in range(trials):
		for b in range(msamples):
			i[0] += traditional(prevalence, tradsize)
		for b in range(tradsize):
			i[1] += matrixpooling(prevalence, matrixsize)
	#print(slotmulti)
	#print(i)
	i = i[0]/(slotmulti * i[1])
	return([prevalence, tradsize, matrixsize, samples, i])	

def matrixcompare(samples, prevalence, matrixsize1, matrixsize2):
	msamples1 = (matrixsize1 ** 2)
	msamples2 = (matrixsize2 ** 2)
	core = msamples1 * msamples2
	slotmulti = (matrixsize1 / 2) / (matrixsize2 / 2)
	samples = core - (samples % core) + samples
	trials = int(samples/core)
	i = [0, 0]

	for a in range(trials):
		for b in range(msamples2):
			i[0] += matrixpooling(prevalence, matrixsize1)
		for b in range(msamples1):
			i[1] += matrixpooling(prevalence, matrixsize2)
	print(i)
	print(slotmulti)
	i = i[0]/(i[1]*slotmulti)
	return([prevalence, matrixsize1, matrixsize2, samples, i])

def main():
	samples = 2400000
	print(matrixcompare(1000000,.33,4,3))
	print(compare(samples,.05,1,4))
	print(compare(samples,.05,1,3))
	"""
	print(compare(samples,.19,2,4))
	print(compare(samples,.16,3,4))
	print(compare(samples,.14,4,4))
	print(compare(samples,.25,2,3))
	print(compare(samples,.21,3,3))
	print(compare(samples,.19,4,3))
	print(compare(samples,.05,2,4))
	print(matrixcompare(samples,.05,4,3))

	i = [0, 0]
	for a in range(12000):
		for b in range(8):
			i[0] += traditional(0.19, 2)
		for b in range(1):
			i[1] += matrixpooling(0.19, 4)
	print(i)
	print(i[0]/i[1])
	i = [0, 0]
	for a in range(12000):
		for b in range(9):
			i[0] += traditional(0.25, 2)
		for b in range(2):
			i[1] += (4/3) * matrixpooling(0.25, 3)
	print(i[1]/i[0])

	# for a in range(1200000):
	i[0] *= 8 
	i[0] /= 100000
	i[1] /= 100000
	print(i)
	"""

main()

