# Import Modules
import json
from difflib import get_close_matches

# Load in the JSON data
data = json.load(open("dictionary.json"))

# Main function
def main():
    output = getDefinition()

    # An iterator to display multiple definitions for a single word
    if type(output) == list:
        for item in output:
            print("-", item)
    # Prints words with a single definition
    else:
        print("-", output)

# Function for getting the definition
def getDefinition():
    while True:
        userInput = input("Input a word to define: ")

        # A conditional checking for the word in the dictionary
        if userInput in data:
            return data[userInput]
            break
        elif userInput.title() in data:
            return data[userInput.title()]
            break
        elif userInput.upper() in data:
            return data[userInput.upper()]
            break
        # If the users word is a close match to a different word this line executes
        elif len(get_close_matches(userInput, data.keys())) > 0:
            action = input("Did you mean %s instead? {y or n]: " % get_close_matches(userInput, data.keys())[0])
            # User is given the choice to select if they meant a certain word or not
            if (action == "y"):
                return data[get_close_matches(userInput, data.keys())[0]]
            elif (action == "n"):
                addWord = input("The word doesn't exist, yet. Would you like to add it? [y or n]: ")
                if (addWord == "y"):
                    definition = input("Enter the definition for %s: " % userInput)
                    newWord = {userInput: definition}
                    insert = data.dumps(newWord)
                    print("%s has been added" % userInput)
                elif (addWord == "n"):
                    print("OK, thanks for using the dictionary!")
                else:
                    print("Invalid entry. Please enter 'y' or 'n'")
            else:
                return ("Invalid entry. Please enter 'y' or 'n'")
        # If word isn't in the dictionary the while loop resets and they can input another word
        else:
            print("That word is not available, please check the word is spelled correctly and try again.")
            print()
            continue

if __name__ == '__main__':
    main()