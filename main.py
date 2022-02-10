
# part 1 stuff
def main():
    userInput = getInput()
    displayWords(userInput)

# user input for part 1
def getInput():
    return input("Enter String \n").split(' ')

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
