import csv
import os

year = "2008"   # This script is designed for 2008, so no need to change this
num_o_kits = len(next(os.walk(year + "/"))[2])
kits = ["%02d" % x for x in range(num_o_kits)]

name_o_list = input("What would you like the output list, or the .csv file, to be called? ")

outlist = []

for n in kits:
    x = "Source Plate 10" + n + ".csv"
    with open(os.path.join("Official_Distributions/" + year + "/", x), "r") as infile:
        outlist.append(n)
        reader = csv.reader(infile)
        for row in reader:
            for element in row:
                # Please exchange the strings below with the strings you are looking for in the database
                if "fp" in element or "GFP" in element or "reen fluorescent protein" in element:
                    outlist.append(row)

with open(name_o_list + year + ".csv", "w") as outfile:
    writer = csv.writer(outfile)
    for row in outlist:
        outfile.write("%s\n" % row)
