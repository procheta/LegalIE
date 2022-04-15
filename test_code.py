import NNP_extractor as npe
import re
import os
tag = 'HEADNOTE:'
tag2='* * *'

tag_found1= False 
tag_found2=True

for path,dirs,files in os.walk("/home/subinay/Documents/data/"):
        for f1 in files:
            filename=os.path.join(path,f1)
            with open(filename, 'r', encoding="utf8") as in_file:
                with open('file.out','a',encoding="utf8") as out_file:
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
                                x='\t'.join(NNP_list)
                                out_file.write(x)




























