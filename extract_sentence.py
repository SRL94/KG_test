import os
import re
import click

script_dir = os.path.dirname(__file__) # absolute dir the script is in
rel_path = "data/data.txt"
abs_file_path = os.path.join(script_dir, rel_path)


def extract_sentence(content_path):
    filehandle = open(content_path)
    return filehandle.read()

def co_reference():

    

@click.command()
@click.option('--min-words', default=6, help='Minimum length of a sentence.')
@click.option('--max-words', default=20, help='Maximum length of a sentece.')
def main(min_words, max_words):
    content = extract_sentence(abs_file_path)
    all_sentences = re.split(r'\.\s+', content) #sentence split based on full stop
    for sent in all_sentences:
        snt_tokens = sent.split()
        if min_words < len(snt_tokens) < max_words:
                # and any(token in snt_tokens for token in tokens):
            print(sent)




if __name__ == '__main__':
    main()
