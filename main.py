# Import Modules
import json
from difflib import get_close_matches

# Load in the JSON date
data = json.load(open("dictionary.json"))

# Main function
def main():
    print(getData())

# Function for getting data
def getData():
    while True:
        userInput = input("Input a word to define: ")
        if userInput in data:
            return data[userInput]
        elif userInput.title() in data:
            return data[userInput.title()]
        elif userInput.upper() in data:
            return data[userInput.upper()]
        elif len(get_close_matches(userInput, data.keys())) > 0:
            return ("Did you mean %s instead" % get_close_matches(userInput, data.keys())[0])
        else:
            print("That word is not available, please check the word is spelled correctly.")
            print()
            continue

if __name__ == '__main__':
    main()