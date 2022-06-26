import os
import nltk
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords


nltk.download('stopwords')
from gensim.utils import tokenize
stop_words = set(stopwords.words('english'))





dir="/Users/prochetasen/Documents/Research/LegalIR/Supreme_court_texts/"



dest_dir="/Users/prochetasen/Documents/Research/LegalIR/Clean/"

files=os.listdir(dir)





def tokenize(train_texts):
    filtered_tokens = []
    train_texts=train_texts.replace("#","")
    train_texts=train_texts.replace("\n"," ")
    #tokens = [word for sent in nltk.sent_tokenize(train_texts) for word in nltk.word_tokenize(sent)]
    tokens=train_texts.split(" ")
    #print(len(tokens))
    filtered_text=""
    for token in tokens:
        #if re.search('[a-zA-Z]',token):
        if (('http' not in token) and ('@' not in token) and ('<*?>' not in token) and (not token in stop_words) and (len(token) <=16)):
            filtered_text=filtered_text+" "+token
                #print("Token",token)
    filtered_text=filtered_text.replace("|"," ")
    filtered_text=filtered_text.replace(". ."," ")
    return filtered_text







for f in files:
	fileName=f.split(".txt")[0]+".pp.txt"
	with open(dest_dir+fileName,"w") as f1:
		flag=0
		print(f)
		st = ""
		with open(dir+f,"r") as f2:
			for line in f2:
				if line=="* * *\n" or line=="HEADNOTE\n":
					flag =1
				if flag ==1:
					if line!="\n":
						line=line.lower()
						st=st+line
		
		l1=sent_tokenize(st)
		for l in l1:
			l=tokenize(l)
			l=l+"\n"
			if l=="\n":	
				continue
			l=l.replace("*","")
			f1.write(l)
	f1.close()

