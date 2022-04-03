import os
import lexnlp.nlp.en.tokens
import lexnlp.nlp.en.segments.sentences
import lexnlp.extract.en.amounts
import lexnlp.extract.en.citations
import lexnlp.extract.en.courts
import lexnlp.extract.en.dates
import lexnlp.extract.en.definitions
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')

dir="/Users/prochetasen/Documents/Research/LegalIR/Supreme_court_texts/"
writeFile="/Users/prochetasen/Documents/Research/LegalIR/res.txt"
dateFile="/Users/prochetasen/Documents/Research/LegalIR/date.txt"
citationFile="/Users/prochetasen/Documents/Research/LegalIR/citations.txt"
defFile="/Users/prochetasen/Documents/Research/LegalIR/definitions.txt"
directory = os.fsencode(dir)
    
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	filePath=os.path.join(dir, filename)
	print("Processing File: ",filePath)
	with open(filePath,"r") as f:
		for line in f:
			line=line.strip()
			sentences=lexnlp.nlp.en.segments.sentences.get_sentence_list(line)
			if len(sentences) >0:
				for sen in sentences:
					#amounts=list(lexnlp.extract.en.amounts.get_amounts(sen))
					#if len(amounts)>0:
						#f1.write(sen)
						#f1.write("\tamount\t")
						#f1.write(str(amounts))
						#f1.write("\n")
					citations=list(lexnlp.extract.en.citations.get_citations(sen))
					if len(citations) > 0:
						with open(citationFile,"a") as f2:
							f2.write(filename)
							f2.write("\t")
							f2.write(sen)
							f2.write("\tcitation\t")
							f2.write(str(citations))
							f2.write("\n")
						f2.close()
					dates=list(lexnlp.extract.en.dates.get_dates(sen))
					if len(dates) > 0:
						with open(dateFile,"a") as f3:
							f3.write(filename)
							f3.write("\t")
                                                        f3.write(sen)
                                                        f3.write("\tdate\t")
                                                        f3.write(str(dates))
                                                        f3.write("\n")
						f3.close()
						
					defs=list(lexnlp.extract.en.definitions.get_definitions(sen))
					if len(defs) > 0:
						with open(defFile,"a") as f4:
							f4.write(filename)
							f4.write("\t")
                                                        f4.write(sen)
                                                        f4.write("\tdefinition\t")
                                                        f4.write(str(defs))
                                                        f4.write("\n")
						f4.close()
					tokens=lexnlp.nlp.en.tokens.get_nouns(sen)
				
					#for token in tokens:
						#print(token)
