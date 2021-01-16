#!/usr/bin/python3

import sys

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

def main():
	hoz = []
	vert = []
	for i in sys.argv[1]:
		hoz.append(int(i))
	for i in sys.argv[2]:
		vert.append(int(i))
	size = int(sys.argv[3])
	printsamples(retestsamples(hoz,vert,size))

main()

