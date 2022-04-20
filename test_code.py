import NNP_extractor as npe
import re
import os
tag = 'HEADNOTE:'
tag2='* * *'

tag_found1= False 
tag_found2=True
i=1
while(i<=50):
    tag_found1= False 
    tag_found2=True
    filename="/home/subinay/Documents/data/1950.INSC."+str(i) + ".txt"
    filepath="/home/subinay/Legal/output/1950.INSC."+str(i) + ".txt"
    with open(filename, 'r', encoding="utf8") as in_file:
        print(filename)
        with open(filepath,'a',encoding="utf8") as out_file:
            print(filepath)
            for line in in_file:
                if not tag_found1 and line.strip() == tag:
                    tag_found1= True
                    continue
                if tag_found1:
                    if tag_found2 and line.strip()==tag2:
                        tag_found2=False
                        break
                    if tag_found2:
                        NNP_list = npe.start(line)
                        x='\n'.join(NNP_list)
                        out_file.write(x)
    #in_file.close()
    #out_file.close()
    i=i+1
    



























