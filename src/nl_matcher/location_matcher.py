import spacy
from spacy.tokens import Span
from spacy.matcher import Matcher
from pathlib import Path
import re


def LocationMatcher():
    # Exclude all but essencial pipelines to improve performance.
    exclude = [
        # 'ner',
        # 'morphologizer',
        # 'tok2vec',
        'tagger',
        'parser',
        'entity_linker',
        'entity_ruler',
        'textcat',
        'textcat_multilabel',
        'lemmatizer',
        'trainable_lemmatizer',
        'attribute_ruler',
        'senter',
        'sentencizer',
        'transformer',
    ]

    nlp = spacy.load('nl_core_news_lg', exclude=exclude)
    ruler = nlp.add_pipe('entity_ruler', before='ner')
    ruler.from_disk((Path(__file__).parent / "./rules").resolve())

    patterns = [
        [
            {"TEXT": "oversteekplaats"},
            {"TEXT": "tussen"},
            {"TEXT": "de"},
            {"ENT_TYPE": {"IN": ["GPE", "FAC", "LOC", "ORG"]}, "OP": "+"},
            {
                "POS": {"IN": ["ADP", "DET", "NOUN", "CCONJ"]},
                "TEXT": {"NOT_IN": ["naar"]},
                "OP": "+"
            },
            {"ENT_TYPE": {"IN": ["GPE", "FAC", "LOC"]}}
        ],

        # ---

        [
            {"TEXT": "in"},
            {"TEXT": "de"},
            {"ENT_TYPE": {"IN": ["GPE", "FAC", "LOC", "ORG"]}, "OP": "+"},
        ],

        # --

        # Example: 'Barn in de Meadow' in Benschop
        [
            {"IS_PUNCT": True},
            {
                "POS": {"IN": ["PROPN", "ADP", "DET"]},
                "OP": "+"
            },
            {"IS_PUNCT": True},
            {
                "POS": {"IN": ["ADP", "DET", "NOUN"]},
                "TEXT": {"NOT_IN": ["naar"]},
                "OP": "+"
            },
            {"ENT_TYPE": {"IN": ["GPE", "FAC", "LOC"]}}
        ],


        # Examples: 'Fluitekamp in Hoogland', 'Maarssense wijk Zwanenkamp'
        [
            {
                "ENT_TYPE": {"IN": ["GPE", "FAC", "LOC", "ORG"]},
                "OP": "+"
            },
            {
                "POS": {"IN": ["ADP", "DET", "NOUN"]},
                "TEXT": {"NOT_IN": ["naar"]},
                "OP": "+"
            },
            {"ENT_TYPE": {"IN": ["GPE", "FAC", "LOC"]}}
        ],

        # ---

        # Pattern that starts with person names and ends with a location.
        # Example: 'Marco Pololaan in de Utrechtse wijk Kanaleneiland'
        [
            {"ENT_TYPE": "PERSON", "OP": "+"},
            {"POS": {"IN": ['ADP', "DET"]},  "OP": "+"},
            {"ENT_TYPE": "NORP"},
            {"POS": "NOUN"},
            {"POS": "PROPN"},
        ],

        # ---

        # At last catch simple locations.
        [{
            "ENT_TYPE": {"IN": ["LOC", "GPE"]},
            "LOWER": {"NOT_IN": ["zondagavond"]},
            "OP": "+"
        }],
    ]

    matcher = Matcher(nlp.vocab)

    for index, pattern in enumerate(patterns):
        matcher.add(f"pattern_{index}", [pattern], greedy="LONGEST")

    def location_matcher(text: str) -> list[Span]:
        # Remove newlines and extra spaces.
        # This is done to improve the performance of the matcher by
        # elminiating the effect of newlines and extra spaces on the
        # text.
        text = text.strip()
        text = text.replace('\n', ' ')
        text = re.sub(r'\s+', ' ', text)

        doc = nlp(text)
        matches = matcher(doc, as_spans=True)
        matches = list(matches)

        return matches

    return location_matcher
