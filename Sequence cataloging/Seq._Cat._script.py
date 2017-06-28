import csv
import os


# Year to analyzed
class YearError(Exception):     # This is an exception class for the year injection below
    def __init__(self):
        pass

b = True
while b:
    try:
        end_year = int(input("What year would you like to analyze? "))
        if end_year <= 2007:
            raise YearError
        b = False
    except ValueError:
        print("The input has to be an integer")
    except YearError:
        print("This script wont work for years before 2008")

if end_year != 2008:
    years = range(2009, end_year+1)  # 2009 - Current year

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


    # Function for analyzing the registry for the keywords
    def analysis(row):
        for element in row:
            # k = keyword injected by the user
            for k in keywords:
                # If k is row the entire row will be added to the result file
                if k in element:
                    outlist.append(row)
                    break
            break


    # Register analysis
    outlist = []
    for year in years:
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

        name_o_list = name + year + ".csv"
        with open(name_o_list, "w") as outfile:
            writer = csv.writer(outfile)
            for row in outlist:
                outfile.write("%s\n" % row)

else:   # If not 2008
    name_o_list = input("What would you like the output list, or the .csv file, to be called? ")

    # Keyword injection
    keyword = input("What are the key words you are looking for? \n"
                    "Please distinguish these with a comma, for example: GFP, gfp, green fluorescent protein. ")
    keywords = keyword.split(",")

    # Analysis of the number of kits in registry
    kit_lo = "Official_Distributions/" + str(end_year) + "/"  # Kit location
    num_o_kits = len(next(os.walk(kit_lo))[2])
    kits = ["%02d" % x for x in range(num_o_kits)]

    n = 0
    while n < len(keywords):
        keywords[n] = keywords[n][1:]
        n += 1

    # Register analysis
    outlist = []
    for n in kits:
        register = "Source Plate 10" + n + ".csv"
        with open(os.path.join(kit_lo, register), "r") as infile:
            outlist.append(n)
            # Syntax of the csv module
            reader = csv.reader(infile)
            for row in reader:
                for element in row:
                    # k = keyword injected by the user
                    for k in keywords:
                        # If k is row the entire row will be added to the result file
                        if k in row:
                            outlist.append(row)

    # Generation of the result file
    with open(name_o_list + str(end_year) + ".csv", "w") as outfile:
        writer = csv.writer(outfile)
        for row in outlist:
            outfile.write("%s\n" % row)


print("You can find the lists in the same directory as the .py file")
