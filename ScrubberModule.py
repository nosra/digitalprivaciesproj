from bs4 import BeautifulSoup
from urllib.request import urlopen
from nltk.corpus import wordnet
import spacy
nlp = spacy.load("en_core_web_md")


class ScrubberModule:
    def __init__(self, url):
        self.url = url
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        self.text = soup.get_text()
        self.tokenizedText = self.text.split()
        self.synsSet = None
        self.blurbList = []
        self.word = None

    def __init__(self, url, word):
        self.url = url
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        self.text = soup.get_text()
        self.tokenizedText = self.text.split()
        self.blurbList = []
        self.word = word
        # self.setSynsToFind(word)

    def changeWord(self, word):
        self.word = word

    def getSynonyms(self, word):
        synsSet = wordnet.synsets(word)
        syns = []
        for syn in synsSet:
            for l in syn.lemmas():
                syns.append(l.name())
        return syns
        # returns list

    def reverseSentence(self, sentence):
        s = sentence.split()[::-1]
        l = []
        for i in s:
            l.append(i)
        return " ".join(l)

    def findWordBlurbs(self):
        self.blurbList.clear()
        syns = self.getSynonyms(self.word)
        mentionsOfInformation = 0
        # blurbList = []
        c = 0

        for word in self.tokenizedText:
            c += 1
            if word in set(syns):
                mentionsOfInformation += 1
                newStr = ""
                i = -1
                while c+i >= 0:

                    if ("." in self.tokenizedText[c+i] or "?" in self.tokenizedText[c+i] or "!" in self.tokenizedText[c+i]):
                        break
                    newStr = newStr + self.tokenizedText[c+i] + " "
                    i -= 1
                # need a better algorithm for this
                newStr = self.reverseSentence(newStr)
                newStr = newStr + " "

                i = 0
                while c+i < len(self.tokenizedText):
                    newStr = newStr + self.tokenizedText[c+i] + " "
                    if ("." in self.tokenizedText[c+i] or "?" in self.tokenizedText[c+i] or "!" in self.tokenizedText[c+i]):
                        break
                    i += 1
                self.blurbList.append(newStr)

                # print(newStr)
                # print(c)

        #print(mentionsOfInformation)
        # self.checkBlurbSimliarities(blurbList)
        # print(self.blurbList)
        # print("WHATS GOING ON!")

    def checkBlurbSimliarities(self, otherBlurbList):
        if(len(otherBlurbList) == 0): return
        blurbComparisonList = []
        similarityTotal = 0
        for otherBlurb in otherBlurbList:
            print("WORKING: " + str(similarityTotal))
            otherSpacyBlurb = nlp(otherBlurb.lower())
            for blurb in self.blurbList:
                spacyBlurb = nlp(blurb.lower())
                similarity = otherSpacyBlurb.similarity(spacyBlurb)
                
                if (similarity > 0):
                    blurbComparisonList.append(
                        ((otherBlurb + " || " + blurb), similarity))
                    # print(otherBlurb)
                    # print("vs:")
                    # print(blurb)
                    

                similarityTotal += similarity

            # print(similarityTotal)

        
        return similarityTotal, blurbComparisonList

'''
def printSimilarBlurbs(scrubber, otherScrubber):

    simTotal, compList = scrubber.checkBlurbSimliarities(
        otherScrubber.blurbList)
    # rint(len(compList))
    if(len(compList) == 0):
        return
    # print(compList[indexOfMostSimilarBlurb])
    compList.sort(key=lambda a: a[1])
    for i in range(1, 10):
        # prints the top ten
        print(compList[i*-1])
'''

#snapChatScrubber = ScrubberModule(
#    "https://values.snap.com/privacy/your-information", "information")
#snapChatScrubber.findWordBlurbs()
#spotifyScrubber = ScrubberModule(
#    "https://twitter.com/en/privacy", "information")
#spotifyScrubber.findWordBlurbs()
# https://en.wikipedia.org/wiki/Phryganodes_selenalis
# https://www.spotify.com/us/legal/privacy-policy/#3-personal-data-we-collect-about-you


#printSimilarBlurbs()
#print("------------")
#snapChatScrubber.changeWord("collect")
#spotifyScrubber.changeWord("collect")
#snapChatScrubber.findWordBlurbs()
#spotifyScrubber.findWordBlurbs()
#printSimilarBlurbs()


# print(syns)


# print(tokenizedText)
