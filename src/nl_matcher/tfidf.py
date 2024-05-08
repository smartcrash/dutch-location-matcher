import numpy as np


def Tfidf():
    def tf(word: str, text: str) -> float:
        return text.count(word) / len(text)

    def idf(word: str, corpus: list[str]) -> np.ndarray:
        count_of_documents = len(corpus) + 1
        count_of_documents_with_word = sum(
            [1 for doc in corpus if word in doc]) + 1
        idf = np.log10(count_of_documents/count_of_documents_with_word) + 1

        return idf

    def tf_idf(word: str, text: str, corpus: list[str]) -> float:
        if not len(text) or not len(corpus):
            return 0

        return tf(word, text) * idf(word, corpus)

    return tf_idf
