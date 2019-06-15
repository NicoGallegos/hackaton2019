import html
import json
import re
from bs4 import BeautifulSoup

TAG_RE = re.compile(r'<[^>]+>')

def clean_text(text):
    return BeautifulSoup(TAG_RE.sub('', text))


#for jsonFile in glob('foo/*.json'):
jsonFile = "/home/nico/Desktop/doctrina-Civil/i0A10A3793AC7161A3F113AB6DF266BCB.json"
data = json.load(open(jsonFile))

print(clean_text(data['fulltext']))





# nlp = spacy.load('es_core_news_sm')


# Process whole documents
# text = ("Hola mi nombre es Nicolas, tengo 30 años, y estoy dando una desipcrión de mi persona")
# doc = nlp(text)

# Analyze syntax
# print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
# for entity in doc.ents:
#    print(entity.text, entity.label_)
