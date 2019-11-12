#
#Kmer counter with bloom filters
#

import sys

def main(argv):
	#Command type
	command=argv[0]
	#file input
	fileName=argv[1]
	#Kmer size input
	k=int(argv[2])
	#Bloom filter size
	blommFilterSize=int(argv[3])
	
	

def readFileReturnStringFasta(filename){
	dnaAnswer=''
	
	index=0
	with open(fileName,'r')as f:
		for l in f:
			if(index==0):
				index+=1
			else:
				dnaAnswer+=l
	
	return dnaAnswer
}

def readFileReturnReadsFastQ(filename){
	dnaAnswer=[]
	
	index=4
	with open(fileName,'r')as f:
		for l in f:
			if(index%4==1):
				index+=1
				dnaAnswer.append(l)
			else:
				index+=1
	
	return dnaAnswer
}





#Utility functions
def reverse(seq):
    """Returns a reversed string"""
    return seq[::-1]
  
def complement(seq):
    """Returns a complement DNA sequence"""
    complement_dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    seq_list = list(seq)
    # I can think of 3 ways to do this but first is faster I think ???
    # first list comprehension
    seq_list = [complement_dict[base] for base in seq_list]
    # second complicated lambda
    # seq_list = list(map(lambda base: complement_dict[base], seq_list))
    # third easy for loop
    # for i in range(len(seq_list)):
    #    seq_list[i] = complement_dict[seq_list[i]]
    return ''.join(seq_list)
def reverse_complement(seq):
    """"Returns a reverse complement DNA sequence"""
    seq = reverse(seq)
    seq = complement(seq)
    return seq

	


# main function
if __name__ == "__main__":
   main(sys.argv[1:])

