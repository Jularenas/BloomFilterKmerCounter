import pyhash

#hashFunctions
fnv=pyhash.fnv1a_32()
mur=pyhash.murmur3_32()
lookup=pyhash.lookup3()
super=pyhash.super_fast_hash()
city=pyhash.city_64()
spooky=pyhash.spooky_32()
farm=pyhash.farm_32()
metro=pyhash.metro_64()
mum=pyhash.mum_64()
xx=pyhash.xx_32()
#10 hash functions
hashfuncs=[fnv,mur,lookup,super,city,spooky,farm,metro,mum,xx]

bit_vector=[]

def createFilterCountTable(bloomFilterSize, kmers, hashCount):
	global bit_vector
	bit_vector=[0]*bloomFilterSize
	hashT={}
	
	for kmer in kmers:
		xrep=''
		revK=reverse_complement(kmer)
		if(kmer<revK):
			xrep=kmer
		else:
			xrep=revK
		if(lookFilter(xrep,hashCount)):
			if(xrep not in hashT):
				hashT[xrep]=0
			else:
				insertBloom(xrep,hashCount)
	for kmer in kmers:
		xrep=''
		revK=reverse_complement(kmer)
		if(kmer<revK):
			xrep=kmer
		else:
			xrep=revK
		if(xrep in hashT):
			hashT[xrep]=hashT[xrep]+1
	for key in hashT:
		if(hashT[key]==1):
			del hashT[key]
		
	#print(hashT)
	return hashT


def insertBloom(kmer,hashCount):
	global bit_vector
	index=0
	for hs in hashfuncs:
		if(bit_vector[hs(kmer)]==0):
			index2=0
			for hs2 in hashFunctions:
				bit_vector[hs2(kmer)]=1
				if(index2>=hashCount):
					break
				index2+=1
		elif(index>=hashCount):
			break
		index+=1
def lookFilter(kmer,hashCount):
	global bit_vector
	index=0
	for hs in hashfuncs:
		if(bit_vector[hs(kmer)]==1):
			return True
		if(index>=hashCount):
			break
		index+=1
	return False



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