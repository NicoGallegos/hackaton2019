import json
import re
import spacy
from bs4 import BeautifulSoup
from pathlib import Path
from collections import OrderedDict
import operator


class Classifier:

    def __init__(self):
        self.nlp = spacy.load('es_core_news_md')

    # Limpio los tags del texto, y luego los espacios multiples
    def clean_text(self, text):
        replaceTags = re.compile(r'<[^>]+>')
        replaceMultipleSpaces = re.compile(r'\s{2,}')
        textosintags = BeautifulSoup(replaceTags.sub(' ', text), "html.parser")
        return replaceMultipleSpaces.sub(' ', textosintags.text)

    def classify(self, query):

        data = {}

        # query = instrumentos derecho internacional'
        # Reemplazar token por query
        tokens = self.nlp(query)

        # Busco los archivos
        for jsonFile in Path('doctrina-Civil/').glob('*.json'):
            try:
                document = json.load(open(jsonFile))
                fullText = self.nlp(self.clean_text(document['fulltext']))
                #title = self.nlp(self.clean_text(document['titleSuggestion']))

                for token in tokens:  # Veo similitud entre texto y token
                    scores = [fullText.similarity(token)]

                    #scores = [fullText.similarity(token), title.similarity(token)]
                    data[document['guid']] = scores
            except:
                print("error con doc")
        return (json.dumps(OrderedDict(sorted(data.items(), key=lambda t: t[1], reverse=True))))
