""" @Author(s): Andrea Failla
    @VersionID: 0.2
    @LastUpdated: 25 lug 2021, 19:20:06
"""
import argparse, sys
from collections import Counter
try:
    import nltk
    from nltk.corpus import stopwords
except ImportError: 
    raise RuntimeError('This script assumes that nltk is installed on your system\
                        \nPlease install nltk, e.g. $pip install --user -U nltk')


def lang_util(lang):
    if lang =='en':
        return 'english'
    elif lang == 'it':
        return 'italian'

   
def get_text(input):
    with open(input, encoding="utf-8") as f:
        text = f.read()
    return text

def tokenize_text(text, lang):
    sent_tokenizer = nltk.data.load('tokenizers/punkt/' + lang +'.pickle')  # loads tokenizer
    sents = sent_tokenizer.tokenize(text)
    tokensTOT = []
    for sent in sents:
        tokens = nltk.word_tokenize(sent)
        for token in tokens:
            tokensTOT.append(token)
    return sents, tokensTOT

def n_chars(tokensTOT):
    nchars = 0
    for token in tokensTOT:
        nchars += len(token)
    return nchars
        
def content_words(tokensTOT, lang):
    sw = stopwords.words(lang)
    content = [word.lower() for word in tokensTOT if not (word.lower() in sw) and word.isalpha()]
    funct = [word.lower() for word in tokensTOT if word.lower() in sw]
    return content, funct 

def PoS_dist(tokensTOT, lang):
    if lang not in ['russian', 'english']:
        dummy = {'x':0}
        return dummy
    postags = nltk.pos_tag(tokensTOT, tagset='universal', lang=lang[:3])
    counts = Counter([j for i,j in postags])
    return dict(counts)

def printall(lang, text, sents, tokensTOT, nchars, vocab, content, funct, PoScounts):
    if lang=='english':
        print('Sentences:', len(sents), '\nTokens:', len(tokensTOT))
        print('Token/Sent ratio:', round(len(tokensTOT)/float(len(sents)), 3))
        print('Number of characters (whitespaces included):', len(text))
        print('Number of characters (whitespaces excluded):', nchars)
        print()
        print('Type words:', len(vocab), '\nType/Token ratio:', round(len(vocab)/float(len(tokensTOT)), 3))
        print('Content Words:', len(content), '\nFunction Words:', len(funct))
        print()
        for tag, v in dict(PoScounts).items():
            print("N. of",tag + ":", v)
            print('Avg n. of', tag, 'per sentence:', round(v/float(len(sents)), 3))
        print()
    
    elif lang=='italian':
        print('Frasi:', len(sents), '\nToken:', len(tokensTOT))
        print('Token per frase', round(len(tokensTOT)/float(len(sents)), 3))
        print('Numero di caratteri (spazi esclusi):', nchars)
        print('Numero di caratteri (spazi inclusi):', len(text))
        print()
        print('Vocabolario:', len(vocab), '\nType/Token ratio:', round(len(vocab)/float(len(tokensTOT)), 3))
        print('Parole contenuto:', len(content), '\nParole funzionali:', len(funct))
        print()
        print('Il PoS tagging in NLTK supporta solo inglese e russo :(')
        print()
    
   

def text_stats(input, lang):
    # converts langstring
    lang = lang_util(lang)
    # fetches text
    text = get_text(input) 

    # gets list of sentences and tokens
    sents, tokensTOT = tokenize_text(text, lang)
    # gets number of characters (whitespaces excluded)
    nchars = n_chars(tokensTOT)
    # gets list of type words
    vocab = list(set(tokensTOT))
    # gets list of content and function words
    content, funct = content_words(tokensTOT, lang)
    # gets dict -> {PoS:count}
    PoScounts = PoS_dist(tokensTOT, lang)
    # print to screen
    printall(lang, text, sents, tokensTOT, nchars, vocab, content, funct, PoScounts)


def main(argv):
    parser = argparse.ArgumentParser(description="Quick Text Stats extractor")
    parser.add_argument("lang", choices=('it', 'en'), help="language option")
    parser.add_argument("input", help="your text file")
    args = parser.parse_args()

    text_stats(args.input, args.lang)


if __name__ == "__main__":
    main(sys.argv)
