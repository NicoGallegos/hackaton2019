import json
import re
import spacy
import operator

from bs4 import BeautifulSoup
from pathlib import Path
from collections import OrderedDict


replaceTags = re.compile(r'<[^>]+>')
replaceMultipleSpaces = re.compile(r'\s{2,}')

#Limpio los tags del texto, y luego los espacios multiples
def clean_text(text):
    textosintags = BeautifulSoup(replaceTags.sub(' ', text), "html.parser")
    return replaceMultipleSpaces.sub(' ', textosintags.text)


nlp = spacy.load('es_core_news_md')

query = u'instrumentos derecho internacional'
#Reemplazar token por query
tokens = nlp(query)

data = {}
#Busco los archivos,
for jsonFile in Path('doctrina-Civil/').glob('*.json'):
    try:
        document = json.load(open(jsonFile))
        fullText = nlp(clean_text(document['fulltext']))
        title = nlp(clean_text(document['titleSuggestion']))
        for token in tokens: #Veo similitud entre texto y titulo
            scores = [fullText.similarity(token)]
            #scores = [ fullText.similarity(token), "titleScore:" + title.similarity(token)]
            data[document['guid']] = scores
        #print(document['guid'], "--", scores)
    except:
        print("error con doc")





print(json.dumps(OrderedDict(sorted(data.items(), key=lambda t: t[1], reverse=True))))
