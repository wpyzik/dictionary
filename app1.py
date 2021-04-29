import json
import difflib

from difflib import get_close_matches

data=  json.load(open("data.json"))
word= input( "Enter word: ")
translation= get_close_matches(word, data.keys(), 5, 0.75) [0] 

def translate (word):
    word= word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif translation != None:
        yn = input ("Did you mean {} ? Enter Y for yes, and N for no.".format(translation))
        yn = yn.upper()
        if yn == "Y":
            return data[translation]
        if yn == "N":
            return "The word doesn't exist. Please double check the word."
        else:
            return "We didn't understand your entry. Sorry! "
    else:
        return "The word doesn't exist. Please double check the word."

output = translate(word)

if type(output) == list:
    for item in output:
        print (item)
else:
    print (output)

