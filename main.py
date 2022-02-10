
# part 1 stuff
def main():
    userInput = getInput()
    circularShift(userInput)
    displayWords(userInput)

# user input for part 1
def getInput():
    return input("Enter String \n").split(' ')

# first circular shift
def circularShift(words):
    new_sentences = []
    for index in range(len(words)):
        new_sentences.append(words)
        words = words[1:] + [words[0]]
    return new_sentences


# display for part 1
def displayWords(words):
    print(words)

main()

# part 2 stuff

class Line():
    words = []

def getInputFromFile():
    with open('data.txt', 'r') as file:
        data = file.read().rstrip()
    dataList = data.split(' ')

    lineStorage = Line()
    for i in dataList:
        lineStorage.words.append(i)
    return lineStorage

def writeToFile(text):
    with open('output.txt', 'w') as file:
        file.write(text)
