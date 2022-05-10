import mmap
import  pandas as pd
import  numpy as np
def extract(vcf, if_data,output):
    #print(vcf)
    if if_data==False:
        f = open(vcf, "rt")
        out = open(output, "wt")
        for line in f:
            if line.startswith("#"):
                continue
            else:
                line=line.split("\n")[0].split("\t")
                i = line[7].split(";")[0].split("=")
                if i[0] == 'DP':
                    i = i[1]
                else:
                    i = 0
                format_list = line[8].split(":")
                if "AD" in format_list:
                    pos = format_list.index("AD")
                else:
                    pos = format_list.index("AO")
                if line[4] != "":
                    tmp_df = pd.DataFrame([[line[0], line[1], line[3], line[4], i,
