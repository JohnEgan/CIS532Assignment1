
# part 1 stuff
def main():
    userInput = getInput()
    shiftedInput = circularShift(userInput)
    alphabetizedInput = alphabetize(shiftedInput)
    displayWords(alphabetizedInput)

# user input for part 1
def getInput():
    return input("Enter String \n").lower().split(' ')

# first circular shift
def circularShift(words):
    new_sentences = []
    for index in range(len(words)):
        new_sentences.append(words)
        words = words[1:] + [words[0]]
    return new_sentences

def alphabetize(words):
    words.sort()
    return words

# display for part 1
def displayWords(words):
    string = ""
    for i in range (len(words)):
        for j in range (len(words[i])):
            string+=(words[i][j] + " ")
        string+=("\n")
    print(string)

main()
