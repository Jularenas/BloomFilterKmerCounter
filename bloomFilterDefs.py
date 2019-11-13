import pyhash
import sys
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

bloomFilterSize=10
bit_vector=[]


#hashFunctions
fnv=pyhash.fnv1a_32()
mur=pyhash.murmur3_32()
lookup=pyhash.lookup3()
super1=pyhash.super_fast_hash()
city=pyhash.city_64()
spooky=pyhash.spooky_32()
farm=pyhash.farm_32()
metro=pyhash.metro_64()
mum=pyhash.mum_64()
xx=pyhash.xx_32()
#10 hash functions
hashfuncs=[fnv,mur,lookup,super1,city,spooky,farm,metro,mum,xx]
#hash

def insertBloom(kmer, hashFuncCount):
    global bloomFilterSize
    global bit_vector
    index=0
    for hf in hashfuncs:
        if(index<=hashFuncCount):
            if(bit_vector[hf(kmer)%bloomFilterSize]==0):
                for hf2 in hashfuncs:
                    bit_vector[hf2(kmer)%bloomFilterSize]=1
            index+=1
        else:
            index+=1
            break
        #print("not avaliable")

def lookFilter(kmer,hashFuncCount):
    global bit_vector
    global bloomFilterSize
    index=0
    for hs in hashfuncs:
        if(bit_vector[hs(kmer)%bloomFilterSize]==1):
            return True
        if(index>=hashFuncCount):
            break
        index+=1
    return False
            
            

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





def main(argv):
    #Bloom filter size
    global bloomFilterSize
    global bit_vector
    bloomFilterSize=int(argv[0])
    
    #BloomFilter
    bit_vector=[0]*bloomFilterSize
        
    #HashTable
    hashT={}
    
    #KmerSize
    k=int(argv[1])
    
    #filename
    filename=argv[2]
    string = ''
    with open(filename,'r') as f:
        index = 0        
        for l in f:
            if (index == 0):
                index +=1
            else:
                string+=l.rstrip("\r\n")
    
    #HashFunctions to use
    hashFuncC=int(argv[3])

    #print("bit_vector_size",len(bit_vector))
    #print("fileReadSize",len(string))

    kmers=[]
    idx=0
    while(len(string)-idx>=k):
        kmers.append(string[idx:idx+k].rstrip("\r\n"))
        idx+=1

    #print("---kmers---")
    print(len(kmers))
    




    for kmer in kmers:
        xrep=''
        x=kmer
        xrep=x
        #xrev=reverse_complement(kmer)
        #if(xrev>x):
        #    xrep=x
        #else:
        #    xrep=xrev
        if(lookFilter(xrep,hashFuncC)):
            if(xrep not in hashT.keys()):
                hashT[xrep]=0
        else:
            insertBloom(xrep,hashFuncC)
    for kmer in kmers:
        xrep=''
        x=kmer
        xrep=x
        #xrev=reverse_complement(kmer)
        #if(xrev>x):
        #    xrep=x
        #else:
        #    xrep=xrev
        if(xrep in hashT.keys()):
            hashT[xrep]+=1

    definiteDict={}
    for key in hashT.keys():
        if(hashT[key]!=1):
            definiteDict[key]=hashT[key]

    print(max(definiteDict.values()))
    print(definiteDict["AAAC"])
    print(len(definiteDict.keys()))
    plt.hist(definiteDict.values(),bins=100,alpha=1)
    plt.savefig("hist.png")





# main function
if __name__ == "__main__":
   main(sys.argv[1:])
    
