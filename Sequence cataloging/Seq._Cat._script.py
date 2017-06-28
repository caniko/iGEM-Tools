import csv
import os


# Function for analyzing the registry for the keywords
def analysis(row):
    print(row)
    for element in row:
        # k = keyword injected by the user
        for k in keywords:
            # If k is row the entire row will be added to the result file
            if k in element:
                outlist.append(row)
                break
        return outlist

def eight(year):    # 2008
    # Analysis of the number of kits in registry
    kit_lo = "Official_Distributions/" + str(year) + "/"  # Kit location
    num_o_kits = len(next(os.walk(kit_lo))[2])
    kits = ["%02d" % x for x in range(num_o_kits)]

    n = 0
    while n < len(keywords):
        keywords[n] = keywords[n][1:]
        n += 1

    # Register analysis
    for k in kits:
        register = "Source Plate 10" + k + ".csv"
        with open(os.path.join(kit_lo, register), "r") as infile:
            outlist.append(k)
            # Syntax of the csv module
            reader = csv.reader(infile)
            for row in reader:
                analysis(row)

    return outlist


def nineseventeen(year):    # 2009-2017
    # Register analysis
    year = str(year)
    num_o_kits = len(next(os.walk("Official_Distributions/" + year + "/"))[2])
    kits = range(1, num_o_kits + 1)
    for n in kits:
        register = str(year) + " Kit Plate " + str(n) + ".csv"
        with open(os.path.join("Official_Distributions/" + year + "/", register), "r") as infile:
            outlist.append(n)
            # Syntax of the csv module
            reader = csv.reader(infile)
            for row in reader:
                analysis(row)  # Using this function to find the relevant sequences
    return outlist


# Name of the result list
name = input("What would you like the output .csv to be called? ")

# Keyword injection
keyword = input("What are the key words you are looking for? \n"
                "Please distinguish these with a comma, for example: GFP, gfp, green fluorescent protein. ")
keywords = keyword.split(",")
n = 0
while n < len(keywords):
    keywords[n] = keywords[n][1:]
    n += 1


years = range(2008, 2017+1)
for year in years:
    outlist = []
    if year == 2008:
        outlist = eight(year)
    else:
        outlist = nineseventeen(year)

    # Generation of the result file
    with open(name + str(year) + ".csv", "w") as outfile:
        writer = csv.writer(outfile)
        for row in outlist:
            outfile.write("%s\n" % row)
