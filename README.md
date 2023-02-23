# sacred_profanity
A python program that detects, censors and indicates the degree of profanity for sentences in a file.\n

Ideal for twitter tweets or youtube/steam/medium reviews as each sentence/review is on a different line. \n

Easy to customize, as you can use a wordlist with your own bad words that you'd like to censor.\n

## Requirements
run the requirements.txt file\n
`pip install -r requirements.txt`

## Running the Code
> Use the help command to see usage
`$ python3 sacred_profanity.py --help
usage: sacred_profanity.py [-h] [-f FILENAME]
                           [-cwf CENSOR_WORD_FILE]
                           [-o OUTPUT_FILE]
                           [-j JOIN]

options:
  -h, --help            show this help message and
                        exit
  -f FILENAME, --filename FILENAME
                        text file that contains
                        strings, default=test.txt
  -cwf CENSOR_WORD_FILE, --censor_word_file CENSOR_WORD_FILE
                        censor word file that
                        contains bad words, leave
                        empty if none
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        name of output file .csv
                        (extension required)
  -j JOIN, --join JOIN  if you wish to use the
                        default bad words library
                        put 0, if you wish to use
                        only your own profane words
                        library put 1, if you wish
                        to use both the libraries
                        put 2, default=0
`

