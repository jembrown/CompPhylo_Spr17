# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


testDnaSeq="aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg"

#### Question 1 ###############################################################################################################################
print("Question 1")
print (len(testDnaSeq)) # len is a inbulit function in python which gives the length of a given string or a list
###############################################################################################################################################

print('\n')
#### Question 2 ###############################################################################################################################
print("Question 2")
testRnaSeq=testDnaSeq.replace("t","u") # replace function can take two arguments old character and character to replace with, and this returns a new string
print(testRnaSeq)                     # this converts the DNA string to RNA

print('\n')
#### Question 3 ###############################################################################################################################
print("Question 3")
revDna=testDnaSeq[::-1] # this operation uses slicing, starts form the end of the string returns charactrs
#print(revDna)          # this is used to get the reverse of the sequence
#d="atgcctgca"
def complment(dna):     # 
    """
    This function takes a string of dna as a input and outputs a string of complmented dna sequence
    
    """
    complement=[] # define a empty list to hold complementry DNA sequence
    dnaStr=dna
    for idx,nt in enumerate(dnaStr):
        if nt=="a":
        
            complement.append("t")   # check each nuclotide and add complmentary base into complment list
        if nt=="t":
        
            complement.append("a")  # check each nuclotide and add complmentary base into complment list
        if nt=="g":
       
            complement.append("c")  # check each nuclotide and add complmentary base into complment list
        if nt=="c":
        
            complement.append("g")  # check each nuclotide and add complmentary base into complment list
    comStr = ''.join(complement)
    return comStr       
            
c=complment(revDna)
print (c)
print('\n')
#### Question 4 ########################################################################################################################
print("Question 4")
def extractCodons(codon,sequence):
     """
     this function takes a codon value and DNA sequence and outputs the nucleotides in specified codon
     """
     c=codon-1 # adjuest for python zero based index
     codonEx1=sequence[c*3:c*3+3] # takes the index and slice input sequence to regions between start and end of the codon
     return (codonEx1)
codon_13=extractCodons(13,testDnaSeq)
codon_14=extractCodons(14,testDnaSeq)

print(codon_13)
print(codon_14)   
print('\n')  
###########################################################################################################################################


#### Question 5 ##########################################################################################################################
print("Question 5")
aa=list("FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG")
Starts=list("--------------------------------MMMM---------------M------------")
Base1=list("TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG")
Base2=list("TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG")
Base3=list("TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG")

startCodons_dict={'ATC':'m','ATA':'m','ATG':'m','ACT':'m','GCT':'m'} # defining start codons in as key value pairs 
terminateCodons_dict={'TCG':'*','TAT':"*",'AAG':'*','AGT':'*'}
other_aa_codon_dict={}

for idx_,amino_acid in enumerate(aa):  # this for loop defines other amino acids as key value pairs in a dictionary 
    amino_acid
    codon=str(Base1[idx_]+Base2[idx_]+Base3[idx_])
    other_aa_codon_dict[codon]=amino_acid

#print(other_aa_codon_dict)
ttt="ATGatgacctTAGTTCACGATGaaaCGATAGCTTATA"
def ntTranslation(nt_sequence, start_codons,terminate_codons,other_codons):
    """
    This function takes a sense dna strand and output the longest protein defined within start and end codons
    four arguments
    nucleotide sequence to translate, should be the sense strand
    dictionary with start codon to amino acid mapping
    dictionary with terminater codon to amino acid mappin
    dictionary with other codons for their respective amino acid mapping
    """
    startDict=start_codons               #user inputs are assigned to variables 
    terDict=terminate_codons             #user inputs are assigned to variables 
    otrDict=other_codons                 #user inputs are assigned to variables 
    
    #print(x)
    start_positions=[]                   # define a empty list to hold the positions of start codons
    terminate_pos=[]                     # define a empty list to hold the positions of end codons
    nn=nt_sequence.upper()               #user supplied nucleotide sequence is converted to upper case
    #print(nn)
    x=len(nt_sequence)%3                 # modulous opertater is used check whether length of nt sequences is divisible by 3
    if x==2:
        number_of_codons=(len(nn)-2)/3   # if not respective number of nt are removed from the end of the list to get the number of codons         
    elif x==1:
       number_of_codons=(len(nn)-1)/3
    elif x==0:
       number_of_codons=(len(nn))/3
    nc=(int(number_of_codons))            # convert the number of codons to intigers
   # print(nc)
    amino_acid_chin=[]                    # define a empty list for amino acid sequence
    for i in range(nc):                   # iterate through all codon positions
        codon1=nn[i*3:i*3+3]              # get the three nt bases of the respective codon
        if codon1 in startDict.keys():    # use the 3nt of the codon to search the start codon dictionary  
           # print ("true")
            start_positions.append(i+1)   #if codon is found in start codon dictionary. store the codon position in start_positions
            amino_acid_chin.append("M")   #and put M in the amino acid chain
            continue
        if codon1 in terDict.keys():      # use the 3nt of the codon to search the stop codon dictionary  
           # print ("true")               #if codon is found in start codon dictionary. store the codon position in terminate_pos
            #print ("true")               #and put * in the amino acid chain
            terminate_pos.append(i+1)
            amino_acid_chin.append("*")
            continue
        if codon1 in otrDict.keys():        # use the 3nt of the codon to search the other codon dictionary  
            aa_=other_aa_codon_dict[codon1] #if codon is found in other_codons dictionary. 
            amino_acid_chin.append(aa_)     #put in the amino acid of the respective codon in amino acid chain list
            continue
        else :
            amino_acid_chin.("_")
            
            
    #print(start_positions)
    #print(terminate_pos)
    print(len(amino_acid_chin))
    long_aa=[]                             #define the list to hold longest amino acid
    for t_pos in terminate_pos:            # iterate through terminator position list
        for st_pos in start_positions:     # iterate through start position list
         if st_pos<t_pos:                  # if start pos is less than ter pos
           protein=[]                      # define a list for putative protein start and end
           #print(str(st_pos)+" "+str(t_pos))
           protein.append(st_pos)
           protein.append(t_pos)
           long_aa.append(protein)
           #break
   
    sorted_protein_coor=sorted(long_aa,key=lambda x: (x[0],x[1])) # sort the coordinates of the 2d list list to find out minimum start and end posions, longest contunous AA chain without stop codon in middle
    #print (sorted_protein_coor)
    protein_start=sorted_protein_coor[0][0]  # assign minimum value to start pos
    protein_end=sorted_protein_coor[0][1]    # assign minimum value to stop pos
    longest_protein=amino_acid_chin[protein_start-1:protein_end]
    longest_protein

    protein_str = ''.join(longest_protein)
    return protein_str
  
       
transpated_dna=ntTranslation(testDnaSeq,startCodons_dict,terminateCodons_dict,other_aa_codon_dict)
print(transpated_dna)   
 
