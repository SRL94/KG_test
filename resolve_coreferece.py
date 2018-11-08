

from stanfordcorenlp import StanfordCoreNLP
# import logging
import json
import os
import re

class StanfordNLP:
    def __init__(self, host='http://localhost', port=9000):
        self.nlp = StanfordCoreNLP(host, port=port,
                                   timeout=30000)  # , quiet=False, logging_level=logging.DEBUG)
        self.props = {
            'annotators':  'tokenize,ssplit,pos,lemma,ner,parse,coref,quote',
            'pipelineLanguage': 'en'
        }

    # def word_tokenize(self, sentence):
    #     return self.nlp.word_tokenize(sentence)
    #
    # def pos(self, sentence):
    #     return self.nlp.pos_tag(sentence)

    def ner(self, sentence):
        return self.nlp.ner(sentence)

    # def parse(self, sentence):
    #     return self.nlp.parse(sentence)
    #
    # def dependency_parse(self, sentence):
    #     return self.nlp.dependency_parse(sentence)
    #
    def annotate(self, sentence):
        return json.loads(self.nlp.annotate(sentence, properties=self.props))

    # load corpus
    def load_corpus(self, content_path):
        filehandle = open(content_path)
        return filehandle.read()

    # write file based on file name
    def write_file(self, file_path, word, tag):
        f = open(file_path, "a")
        f.write(word + ": " + tag + "\n")
        f.close()


    # @staticmethod
    # def tokens_to_dict(_tokens):
    #     tokens = defaultdict(dict)
    #     for token in _tokens:
    #         tokens[int(token['index'])] = {
    #             #'word': token['word'],
    #             #'lemma': token['lemma'],
    #             #'pos': token['pos'],
    #             'ner': token['ner']
    #         }
    #     return tokens

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__) # absolute dir the script is in
    rel_path = "data/chesterton_brown.txt"
    ner_path = "data/ner.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    ner_file_path = os.path.join(script_dir, ner_path)
    os.remove(ner_file_path)
    ner_words = list()
    sNLP = StanfordNLP()
    text = sNLP.load_corpus(abs_file_path)
    ners = sNLP.ner(text)
    #
    # record all ners
    for (word, tag) in ners:
        if not re.match(r'^O[a-z|A-Z|0-9]*',tag) and \
            word not in ner_words:
            sNLP.write_file(ner_file_path, word, tag)
            ner_words.append(word)

    # coreference resolution
    result = sNLP.annotate(text)
    print(result['corefs'])
    # for (index, info) in result['corefs']:
    #     print(info)
    #print(result['corefs'])
    # print(text)
    # print ("Annotate:", sNLP.annotate(text))
    # print ("POS:", sNLP.pos(text))
    # print ("Tokens:", sNLP.word_tokenize(text))
    # print ("Parse:", sNLP.parse(text))
    # print ("Dep Parse:", sNLP.dependency_parse(text))

    # nlp = StanfordCoreNLP(r'/home/sl33548948/Desktop/Codes/stanford-corenlp-full-2018-10-05')
    # print(nlp.annotate(text))
