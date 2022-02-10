# part 2 stuff

class Word:
    def _init_(self,word):
        self.value = word


class Line:
    def _init_(self):
        self.words = []

def main():
    userInput = getInputFromFile()
    shifted_output = circularShift(userInput)
    print(shifted_output[0].words[0].value)
    #sortedInput = bubbleSort(userInput)
    #writeToFile(sortedInput)

def getInputFromFile():
    with open('input.txt', 'r') as file:
        data = file.read().rstrip()
    dataList = data.split(' ')

    lineStorage = Line()
    for i in dataList:
        lineStorage.words.append(Word(i))
    return lineStorage

# first circular shift
def circularShift(line):
    new_sentences = []
    current_line = line
    for index in range(len(line.words)):
        new_sentences.append(current_line)
        new_line = Line()
        new_line.words = current_line.words[1:] + [current_line.words[0]]
    return new_sentences

def bubbleSort(array):
    length = len(array)
    lowerSentences = []
    for i in range(length):
        lowerSentences.append(array[i].lower())

    for x in range(length-1):
        for y in range(length - x - 1):
            if lowerSentences[y] > lowerSentences[y + 1]:
                lowerSentences[y], lowerSentences[y + 1] = lowerSentences[y + 1], lowerSentences[y]

    print(lowerSentences)
    nonInterestingSentences = []
    interestingSentences = []
    for sentence in lowerSentences:
        if sentence.startswith('a') or sentence.startswith('the') or sentence.startswith('is') or sentence.startswith('and') or sentence.startswith('or') or  sentence.startswith('at') or sentence.startswith('an'):
            nonInterestingSentences.append(sentence)

    for sentence2 in lowerSentences:
        if sentence2 not in nonInterestingSentences:
            interestingSentences.append(sentence2)

def writeToFile(text):

    string = ""
    for i in range(len(text)):
        for j in range(len(text[i])):
            string += (text[i][j] + " ")
        string += ("\n")
    print(string)

    with open('output.txt', 'w') as file:
        file.write(string)

main()