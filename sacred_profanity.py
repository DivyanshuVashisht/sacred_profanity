from better_profanity import profanity
import argparse
import re
import csv

def load_censor_word_file(censor_words_file):
    profanity.load_censor_words_from_file(censor_words_file)

def add_censor_word_file(censor_words_file):
    censor_words = []
    file = open(censor_words_file, 'r')
    lines = file.readlines()
    for line in lines:
        censor_words.append(line.strip())

    profanity.add_censor_words(censor_words)


def load_text_file(filename):
    file = open(filename, 'r')
    return file

def tokenize(text):
    return re.findall(r'\w+', text.lower())

def profanity_degree(sentence):
    tokens = tokenize(sentence)
    if len(tokens) == 0:
        return
    degree_of_profanity = sum(1 for t in tokens if profanity.contains_profanity(t)) / len(tokens)
    return sentence.strip(), profanity.censor(sentence).strip(), "%.2f" %  degree_of_profanity

def initialize_output_file(filename):
    file = open(filename, 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(["sentence", "censored sentence", "degree of profanity"])
    return writer

def write_to_file(writer, line):
    if line:
        writer.writerow(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="text file that contains strings, default=test.txt", default="./test.txt")
    parser.add_argument("-cwf", "--censor_word_file", help="censor word file that contains bad words, leave empty if none")
    parser.add_argument("-o", "--output_file", help="name of output file .csv (extension required)", default="output.csv")
    parser.add_argument("-j", "--join", help="if you wish to use the default bad words library put 0, if you wish to use only your own profane words library put 1, if you wish to use both the libraries put 2, default=0", default=0)

    args = parser.parse_args()
    output = initialize_output_file(args.output_file)
    
    if args.censor_word_file and args.join == "1":
        load_censor_word_file(args.censor_word_file)
    elif args.censor_word_file and args.join == "2":
        add_censor_word_file(args.censor_word_file)
    else:
        profanity.load_censor_words()

    file = load_text_file(args.filename)
    lines = file.readlines()
    for line in lines:
        result = profanity_degree(line)
        if result:
            write_to_file(output, list(result))

