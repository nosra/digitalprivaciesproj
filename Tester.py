from ScrubberModule import ScrubberModule
urls = open('urls.txt', 'r')
results = open('results.txt', 'w')
lines = urls.readlines()
scrubberList = []
bigCompList = []


def addSimiliarBlurbs(scrubber, otherScrubber):
    # print(scrubber.blurbList)
    # print(otherScrubber.blurbList)
    # print("Yes")
    simTotal, compList = scrubber.checkBlurbSimliarities(
        otherScrubber.blurbList)

    if(len(compList) == 0):
       return
    # print(compList[indexOfMostSimilarBlurb])
    compList.sort(key=lambda a: a[1])
    for i in range(1, 10):
        # prints the top ten
        # im only adding the top ten for efficiency sake
        # may change in the future
        bigCompList.append((scrubber.url + " /\ VS. /\ " + otherScrubber.url, compList[i*-1]))

        # print(compList[i*-1])
    
    print("FINISHED: " + scrubber.url + " /\ VS. /\ " + otherScrubber.url)
    

# add all of the urls
for line in lines:
    scrubberList.append(ScrubberModule(line, "information"))

# begin master algorithm
def executeAlgorithm():
    for i in range(len(scrubberList)):
        # initializing the word blurbs first
        scrubberList[i].findWordBlurbs()
        
    for i in range(len(scrubberList)):
        if(i != 0):
            for bigTuple in bigCompList:
                results.write(bigTuple[0])
                results.write('\n')
                for element in bigTuple[1]:
                    results.write(str(element))
                results.write('\n')
                results.write("___")
                results.write('\n')
            bigCompList.clear()
        for j in range(i+1, len(scrubberList)):
            addSimiliarBlurbs(scrubberList[i], scrubberList[j])


        
# print(len(scrubberList))
# scrubberList[7].findWordBlurbs()
# print(scrubberList[2])
# scrubberList[9].findWordBlurbs()
# print(scrubberList[3])
# addSimiliarBlurbs(scrubberList[7], scrubberList[9])
# print(bigCompList)
'''
for bigTuple in bigCompList:
    results.write(bigTuple[0])
    results.write('\n')
    for element in bigTuple[1]:
        results.write(str(element))
    results.write('\n')
    results.write("___")
    results.write('\n')
'''
executeAlgorithm()

urls.close()
results.close()
# print(scrubberList)
