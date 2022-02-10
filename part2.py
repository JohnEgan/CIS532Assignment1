# part 2 stuff

class Word:
    def init(self,word):
        self.value = word


class Line:
    def init(self):
        self.words = []

def main():
    userInput = getInputFromFile()
    sortedInput = bubbleSort(userInput)

def getInputFromFile():
    with open('input.txt', 'r') as file:
        data = file.read().rstrip()
    dataList = data.split(' ')

    lineStorage = Line()
    for i in dataList:
        lineStorage.words.append(Word(i))
    return dataList

def bubbleSort(array):
    length = len(array)
    lowerSentences = []
    for i in range(length):
        lowerSentences.append(array[i].lower())

    for x in range(length-1):
        for y in range(length - x - 1):
            if lowerSentences[y] > lowerSentences[y + 1]:
                lowerSentences[y], lowerSentences[y + 1] = lowerSentences[y + 1], lowerSentences[y]

def writeToFile(text):

    string = ""
    for i in range(len(text)):
        for j in range(len(text[i])):
            string += (text[i][j] + " ")
        string += ("\n")
    print(string)

    with open('output.txt', 'w') as file:
        file.write(string)