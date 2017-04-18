# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Print the length of the sequence to the screen along with text explaining the value
dnaseq = "aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg"
len(dnaseq)
print(len(dnaseq))

# Create and store the RNA equivalent of the sequence, then print to screen
dnaseq = "aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg"
print(dnaseq)
dnaseq1 = dnaseq.replace('t', 'u')
print(dnaseq1)

# complementry sequence from given DNA sequence
seq = "aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg"
comp = seq.replace('a', 'T')
print(comp)
comp1 = comp.replace('t', 'A')
print(comp1)
comp2 = comp1.replace('c', 'G')
print(comp2)
complementry_seq = comp2.replace('g', 'C')
print(complementry_seq)

# reverse_complementry sequence 
reverse_complementry_DNA = complementry_seq[::-1]
print(reverse_complementry_DNA)

# Extract the bases corresponding to the 13rd and 14th codons from the sequence, then print them to the screen
dnaseq = "aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg"
cod13 = (dnaseq[36:39])
print(cod13)
#Codon13 is aaa
cod14 = (dnaseq[36:39])
print(cod14)
# Codon 14 is aaa

# split sequence in triplets
myseq = "aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg"
triplate_codon = [myseq[i:i+3]for i in range(0,len(myseq),3)]
for codon in triplate_codon:
    print(codon)
    print(triplate_codon)
    
# Translate the sequence

myseq = "aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg"
def translate_sequence(myseq):
    triplate_codon = [myseq[i:i+3]for i in range(0,len(myseq),3)]
    for codon in triplate_codon:
        if codon in ['ttt','ttc']:
            print("Phe"), 
        elif codon in ['tta', 'ttg', 'ctt', 'cta', 'ctc', 'ctg']:
            print ("Leu"),
        elif codon in ['att', 'atc']:
            print ("Ile"),
        elif codon in ['ata', 'atg']:
            print ("Met"),
        elif codon in ['gtt','gtc', 'gta', 'gtg']:
            print ("Val"),
        elif codon in ['tct', 'tcc', 'tca', 'tcg']:
            print ("Ser"),
        elif codon in ['cct', 'ccc', 'cca', 'ccg']:
            print ("Pro"),
        elif codon in ['act' , 'acc', 'aca' , 'acg']:
            print ("Thr"),
        elif codon in ['gct' , 'gcc', 'gca' , 'gcg']:
            print ("Ala"),
        elif codon in ['tat' , 'tac']:
            print ("Tyr"),
        elif codon in ['taa' , 'tag']:
            print ("Ter"),
        elif codon in ['cat' , 'cac']:
            print ("His"),
        elif codon in ['caa' , 'cag']:
            print ("Gln"),
        elif codon in ['aat' , 'aac']:
            print ("Asn"),
        elif codon in ['aaa' , 'aag']:
            print ("Lys"),
        elif codon in ['gat' , 'gac']:
            print ("Asp"),
        elif codon in ['gaa' , 'gag']:
            print ("Glu"),
        elif codon in ['tgt' , 'tgc']:
            print ("Cys"),
        elif codon in ['tga' , 'tgg']:
            print ("Trp"),
        elif codon in ['cgt' , 'cgc' , 'cga' , 'cgg']:
            print ("Arg"),
        elif codon in ['agt' , 'agc']:
            print ("Ser"),
        elif codon in ['aga' , 'agg']:
            print ("Ter"),
        elif codon in ['ggt' , 'ggc' , 'gga' , 'ggg']:
            print ("Gly"),
        else:
           print("stop")
          
translate_sequence(myseq)         
    







        
