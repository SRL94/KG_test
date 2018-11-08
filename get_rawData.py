import nltk
import os
# nltk.download()

raw_data = nltk.corpus.gutenberg.raw('chesterton-brown.txt')
script_dir = os.path.dirname(__file__) # absolute dir the script is in
rel_path = "data/chesterton_brown.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def main():
    f = open(rel_path, "w")
    f.write(raw_data)
    f.close()

if __name__ == '__main__':
    main()
