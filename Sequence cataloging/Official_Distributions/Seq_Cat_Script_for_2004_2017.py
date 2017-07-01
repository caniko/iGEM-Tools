import csv
import os


# Function for analyzing the registry for the keywords
def analysis(outlist,row,keywords):
    for element in row:
        # k = keyword injected by the user
        for k in keywords:
            # If k is row the entire row will be added to the result file
            if k in element:
                outlist.append(row)
                break
            # else:
            #     break
    return outlist

def getOutputName():
    # Name of the result list
    name = input("What would you like the output .csv to be called? ")
    return name

def getKeyword():
    # Keyword injection
    keyword = input("What are the key words you are looking for? \n"
                    "Please distinguish these with a comma, for example: GFP, gfp, green fluorescent protein. ")
    keywords = keyword.split(",")
    n = 0
    while n < len(keywords):
        keywords[n] = keywords[n][1:]
        n += 1
    return keywords

def generateOutlist(name, keyword):
    years = list(range(2008, 2017 + 1))
    for year in years:
        if year == 2008:
            outlist = eight(year, keyword)
            writeToFile(name, year, outlist)
        else:
            outlist = nineseventeen(year,keyword)
            writeToFile(name, year, outlist)

def getAllFolders(dest):
    import glob
    dirlist = glob.glob(dest)
    return dirlist

def getAllFiles():
    allDirectories = getAllFolders('Official_Distributions/*')
    allFiles = []
    for directory in allDirectories:
        allFiles.append(getAllFolders(directory+'/*'))
    return allFiles

myAllFiles = getAllFiles()

def getYearNames(allFiles):
    years = []
    for files in allFiles:
        for file in files:
            years.append(file.split("\\",2)[1])
    return years
allYears = getYearNames(myAllFiles)

def cleanYearList(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

myAllYears = cleanYearList(allYears)



def makeFlatList(inputList):
    import itertools
    merged = list(itertools.chain(*inputList))
    return merged

def fileManipulator(files, keyword):  # 2008
    totalOutlist = []
    allFiles = makeFlatList(files)
    for file in allFiles:
        with open(file) as infile:
            reader = csv.reader(infile)
            for row in reader:
                myOutlist = analysis(totalOutlist, row, keyword)
    return myOutlist

userName = getOutputName()
userKeyword = getKeyword()



finalOutList = fileManipulator(myAllFiles, userKeyword)
with open(userName+".csv","w") as outfile:
    writer = csv.writer(outfile)
    for row in finalOutList:
        outfile.write("%s\n" % row)