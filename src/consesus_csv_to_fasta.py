import pandas as pd
import textwrap
import sys
# main
df = pd.read_csv(sys.argv[1],header=None)
# concatenate nucleotides in the 1st row of the dataframe
seq = df.iloc[0].str.cat(sep="")
# wrap fasta sequence by x characters per line
wrapped_seq = textwrap.fill(seq, width=int(sys.argv[2]))
# export to fasta
with open(sys.argv[3], "w") as f:
    f.write(f'>consesus_seq\n{wrapped_seq}\n')
