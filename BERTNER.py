from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import os

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "My name is Wolfgang and I live in Berlin"


dir="/Users/prochetasen/Documents/Research/LegalIR/Supreme_court_texts/"
writeDir="/Users/prochetasen/Documents/Research/LegalIR/BERTNER/"

directory = os.fsencode(dir)
word="word"
entity="entity"
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	filePath=os.path.join(dir, filename)
	print("Processing File: ",filePath)
	writeFile=writeDir+filename.split(".txt")[0]+".ann"
	ann_dict={}
	ann_context={}
	ann_mention={}
	with open(filePath,"r") as f:
		for line in f:
			st=line.strip()
			anns=nlp(st)
			#print(anns)
			try:
				for ann in anns:
					count=0
					mentions=[]
					contexts=[]
					if ann[word] in ann_dict.keys():
						count=ann_dict[ann[word]]
						mentions=ann_mention[ann[word]]
						contexts=ann_context[ann[word]]
					if len(ann[word]) <=2 or ann[word].startswith("#"):
						continue	
					ann_dict[ann[word]]=count+1
					mentions.append(ann[entity])
					contexts.append(st)
					ann_context[ann[word]]=contexts
					ann_mention[ann[word]]=mentions
                                        #print(ann.mention)
			except Exception as e:
				print("exception", e)
	with open(writeFile,"w") as f1:
		f1.write("Annotation\tStat\tContext\tType\n")
		for key in ann_dict.keys():
			f1.write(key)
			f1.write("\t")
			f1.write(str(ann_dict[key]))
			f1.write("\t")
			contexts=ann_context[key]
			for ct in contexts:
				f1.write(ct)
				f1.write("##")
			f1.write("\t")
			mentions=ann_mention[key]
			for mention in mentions:
				f1.write(mention)
				f1.write(",")
			f1.write("\n")
	f1.close()
	break



