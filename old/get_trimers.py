import gzip
import os
with open('bednamesG.txt','r') as infile:
    lines = infile.readlines()
    files =[str(e.strip()) for e in lines]
infile.close()

for bed in files:
    outfile = gzip.open(str(bed) + '.trimer.bed.gz','wb')
    with gzip.open(str(bed) + '.fix.bed.gz','rb') as f:
        lines = f.readlines()
        for line in lines:
            chrom = line.split('\t')[0]
            start=int(line.split('\t')[1])
            end = int(line.split('\t')[2])
            n = line.split('\t')[3]
            name = n.strip()
            newstart=start-1
            outfile.write(str(chrom) + '\t' +  str(newstart) + '\t' + str(end) + '\t'+ str(name) + '\n')
    outfile.close()
    f.close()
    os.remove(str(bed) + '.fix.bed.gz')