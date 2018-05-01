story = open("SherlockHolmes.txt", "r").read()
wordList = [word.strip('''.'!?:"''') for word in story.split(" ")]
def frequency(text):
    return sum([1 for each in wordList if each == text ])

def totalPhraseFrequency(argList):
    return sum([frequency(word) for word in argList])

#Takes a very long time since text is very big
def mostFrequent():
    distinctList = []
    [distinctList.append(x) for x in wordList if x not in distinctList]
    return reduce(lambda prev, curr: prev if frequency(prev) > frequency(curr) else curr, distinctList)

print "Frequency of Holmes appearing: " + str(frequency("Holmes"))
print "Frequency of doctor appearing: " + str(frequency("doctor"))
print "Frequency of Holmes and doctor appearing: " + str(totalPhraseFrequency(["Holmes", "doctor"]))
print "most frequent word is " + str(mostFrequent())

