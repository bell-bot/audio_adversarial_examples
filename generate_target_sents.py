 # Get all paragraphs from the nltk inaugural speech corpus and save them to a list of strings
 # and merge texts into one list
import nltk
nltk.download("inaugural")
nltk.download("punkt")
from nltk.corpus import inaugural
import random


def get_inaugural_sentences():
    # Get the fileids for all speeches
    fileids = inaugural.fileids()

    # Initialize paragraphs to be an empty list
    paras = []

    for id in fileids:
        p = inaugural.paras(id)
        for paragraph in p:
            sents = [" ".join(w for w in sent if valid_word(w)) for sent in paragraph]
            joined_sents = " ".join(sents)

            paras.append(joined_sents)

    random.shuffle(paras)
    return paras
   
def valid_word(word):

    # Only allow the following tokens
    toks = " abcdefghijklmnopqrstuvwxyz'-"

    for i in word:
        if not(i in toks):
            return False

    return True
