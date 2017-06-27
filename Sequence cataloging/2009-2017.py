import csv
import os


years = [2009 + x for x in range(8)]    # 2008-2017
name_o_list = input("What would you like the output .csv to be called? ")

outlist = []

for year in years:
    year = str(year)
    num_o_kits = len(next(os.walk(year + "/"))[2])
    kits = range(1, num_o_kits + 1)

    for n in kits:
        x = str(year) + " Kit Plate " + str(n) + ".csv"
        with open(os.path.join("Official_Distributions/"+ year + "/", x), "r") as infile:
            outlist.append(n)
            reader = csv.reader(infile)
            for row in reader:
                for element in row:
                    # Please exchange the strings below with the strings you are looking for in the database
                    if "gfp" in element or "GFP" in element or "reen fluorescent protein" in element:
                        outlist.append(row)
            outlist.append("")

    with open(name_o_list + year + ".csv", "w") as outfile:
        writer = csv.writer(outfile)
        for row in outlist:
            outfile.write("%s\n" % row)
