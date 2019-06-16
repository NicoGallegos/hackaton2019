import json
import re
import spacy
from bs4 import BeautifulSoup
from pathlib import Path


replaceTags = re.compile(r'<[^>]+>')
replaceMultipleSpaces = re.compile(r'\s{2,}')

#Limpio los tags del texto, y luego los espacios multiples
def clean_text(text):
    textosintags = BeautifulSoup(replaceTags.sub(' ', text), "html.parser")
    return replaceMultipleSpaces.sub(' ', textosintags.text)


nlp = spacy.load('es_core_news_md')

#Reemplazar token por query
tokens = nlp(u'instrumentos derecho internacional')

#Busco los archivos,
for jsonFile in Path('C:/Users/nicol/Desktop/doctrina-Civil/').glob('*.json'):
    try:
        document = json.load(open(jsonFile))
        fullText = nlp(clean_text(document['fulltext']))
        title = nlp(clean_text(document['titleSuggestion']))
        for token in tokens: #Veo similitud entre texto y titulo
            scores = [fullText.similarity(token), title.similarity(token)]

        print(document['guid'], "--", scores)
    except:
        print("error con doc")





