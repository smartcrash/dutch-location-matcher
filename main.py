import spacy
# import re
# from nl_matcher import LocationMatcher
from nl_matcher import Tfidf

exclude = [
    'ner',
    'morphologizer',
    # 'tok2vec',
    # 'tagger',
    # 'parser',
    'entity_linker',
    'entity_ruler',
    'textcat',
    'textcat_multilabel',
    'lemmatizer',
    'trainable_lemmatizer',
    'attribute_ruler',
    'senter',
    # 'sentencizer',
    'transformer',
]

nlp = spacy.load('nl_core_news_sm', exclude=exclude)


text = """
De politie heeft op station Amersfoort een waarschuwingsschot gelost bij de aanhouding van een man. Hij zou in de trein een andere reiziger hebben bedreigd met een vuurwapen.
Even na 22.00 uur kreeg de politie een melding vanuit de trein. Daarop werd Amersfoort Centraal ontruimd. Toen de man niet op het waarschuwingsschot reageerde, hebben agenten hem getaserd en gearresteerd.
Het vermoedelijke vuurwapen is in beslag genomen. Niemand raakte bij het incident gewond.
"""

tdidf = Tfidf()

doc = nlp(text)
corpus = [sent.text for sent in doc.sents]

print("1:", tdidf("Amersfoort", text, corpus))
print("2:", tdidf("Amersfoort Centraal", text, corpus))
print("2:", tdidf("Zebra", text, corpus))

# text = """
# Was u getuige van de aanval in de Maarssense wijk Zwanenkamp op
# woensdag 1 februari? Bel dan met de tiplijn: 0800 - 6070 of bel
# Meld Misdaad Anoniem: 0800 - 7000. Beelden waarop de dader te
# zien is kunt u uploaden via politie.nl/upload
#
# Maarssense wijk Zwanenkamp
#
# Maarssense wijk Zwanenkamp
# """
#
# print(text.count("Maarssense wijk Zwanenkamp"))

# nlp = spacy.load('nl_core_news_lg')
#
# location_matcher = LocationMatcher()
#
# locations = location_matcher(text)
#
# for span in locations:
#     print(span.text)

# print("======")
#
# text = text.strip()
# text = text.replace('\n', ' ')
# text = re.sub(r'\s+', ' ', text)
#
# doc = nlp(text)
#
# for span in doc:
#     print(span.text, "|", span.pos_, "|", span.ent_type_)
