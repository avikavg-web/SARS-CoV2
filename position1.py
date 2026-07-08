import re

f=open("/share/SARS-class/SARS-2020.fasta")

lines = f.readlines()
for i in range(len(lines)):
   lines[i] = lines[i].rstrip('\n')

string = ""

for i in range(len(lines)):
   string += lines[i]

codon = ""

for i in range (0, len(string), 3):
   codon = string [i: i+3]
   print (codon)
