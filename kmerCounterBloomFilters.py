#
#Kmer counter with bloom filters
#

import sys
import bloomFilterDefs

def main(argv):
	#Command type
	command=argv[0]
	#file input
	fileName=argv[1]
	#Kmer size input
	k=int(argv[2])
	#Bloom filter size
	blommFilterSize=int(argv[3])
	#Hash functions to use
	hashCount=int(argv[4])
	
	#FileDistinction
	dnaToProcess=''
	if(fileName.endsWith(".fa")):
		dnaToProcess=readFileReturnStringFasta(fileName)
	elif(fileName.endsWith(".fastq")):
		dnaToProcess=readFileReturnReadsFastQ(fileName)
		
	myKmers=getKmers(dnaToProcess)
	hashTableKmerCount=bloomFilterDefs.createFilterCountTable(blommFilterSize,myKmers,hashCount)
	
	vals=list(hashTableKmerCount.values())
	maxVal=max(vals)

	#print(max)
	frecuencies=[0]*(maxVal+1)
	for val in vals:
		valKFr=frecuencies[val]
		frecuencies[val]=valKFr+1
	print("somethings")
	if(command=='frecs'):
		print(frecuencies)
	else:
		print(hashTableKmerCount[command])
	#print(frecuencies)
	#print(frecuencies[1])
	

def readFileReturnStringFasta(filename):
	dnaAnswer=''
	index=0
	with open(fileName,'r')as f:
		for l in f:
			if(index==0):
				index+=1
			else:
				dnaAnswer+=l
	
	return dnaAnswer

def readFileReturnStringFastQ(filename):
	dnaAnswer=''
	index=4
	with open(fileName,'r')as f:
		for l in f:
			if(index%4==1):
				index+=1
				dnaAnswer+=l
			else:
				index+=1	
	
	return dnaAnswer

def getKmers(dnaString,k):
	kmers=[]
	i=1
	dnaLen=len(dnaString)
	while(dnaLen-i>=k):
		kmers.append(dnaString[i:i+k])
		i+=1
	return kmers

# main function
if __name__ == "__main__":
   main(sys.argv[1:])

