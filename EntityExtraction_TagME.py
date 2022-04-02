import tagme
import os

tagme.GCUBE_TOKEN="5cdbd99a-62b1-4f7e-aad1-45aa6676b3a2-843339462"
dir="/Users/prochetasen/Documents/Research/LegalIR/Supreme_court_texts/"
writeDir="/Users/prochetasen/Documents/Research/LegalIR/"

directory = os.fsencode(dir)
    
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	filePath=os.path.join(dir, filename)
	print("Processing File: ",filePath)
	writeFile=writeDir+filename.split(".txt")[0]+".ann"
	ann_dict={}
	ann_mention={}
	with open(filePath,"r") as f:
		for line in f:
			st=line.strip()
			anns=tagme.annotate(st)
			try:
				for ann in anns.get_annotations(0.5):
					count=0
					mentions=[]
					if ann.entity_title in ann_dict.keys():
						count=ann_dict[ann.entity_title]
						mentions=ann_mentions[ann.entity_title]
					ann_dict[ann.entity_title]=count+1
					mentions.append(ann.mention)
					ann_mention[ann.entity_title]=mentions
					#print(ann.mention)
			except:
				print("exception")
	with open(writeFile,"w") as f1:
		f1.write("Annotation\tStat\n")
		for key in ann_dict.keys():
			f1.write(key)
			f1.write("\t")
			f1.write(str(ann_dict[key]))
			f1.write("\t")
			mentions=ann_mention[key]
			for mention in mentions:
				f1.write(mention)
				f1.write(",")
			f1.write("\n")
	f1.close()
	

