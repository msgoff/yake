import yake
from sys import argv

with open(argv[1],'r') as f:
    text =f.read()

#### assuming default parameters
kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(text)

for kw in keywords:
	print(kw)
