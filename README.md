# sacred_profanity
A python program that detects, censors and indicates the degree of profanity for sentences in a file.

Ideal for twitter tweets or youtube/steam/medium reviews as each sentence/review is on a different line. 

Easy to customize, as you can use a wordlist with your own bad words that you'd like to censor.

## Requirements
- run the requirements.txt file
`pip install -r requirements.txt`

- A single line is treated as a single statement and hence the program gives a single degree of profanity to it. Refer test.txt for structure of the file.
- The file with profane words list should contain words in different lines. Refer profane_words_list.txt for structure of wordlist file.

## Running the Code
> Use the help command to see usage
`$ python3 sacred_profanity.py --help`
`usage: sacred_profanity.py [-h] [-f FILENAME]
                           [-cwf CENSOR_WORD_FILE]
                           [-o OUTPUT_FILE]
                           [-j JOIN]`

## Simple Execution (no custom profane wordlist provided)
> `$ python3 sacred_profanity.py -f test.txt`
The output contains the sentences, their censored version and the degree of profanity. The output is saved in output.csv file.

## Execution with profane words list
> `$ python3 sacred_profanity.py -f test.txt -cwf profane_words_list.txt -j 1 `
You can replace 1 with 0 if you want to use better_profanity's default wordlist, 1 is to use only your own wordlist and 2 is to use your own wordlist in conjunction with the default wordlist.

>>Note: You can also define the name of the output file using the `-o` flag.

