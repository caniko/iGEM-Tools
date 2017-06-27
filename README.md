# iGEM Tools
Welcome to the iGEM tools repository created by iGEM UiO. We hope that you can share the benefits of these tools that have saved us many hours. We only have one tool so far, but many more may come.

## Sequence cataloging (Python 3.x)
This tool was conceved on a summerday session, when we needed to find the sequences that may have been similar to one of our parts, the GFP gene. In order to determine if our part is new, modified, or identical compared to existing parts.
But, as you may have already seen, the iGEM part registry is, quite frank, a nightmare. This tool or script, scans through the iGEM registry for the keywords provided by the user.
The rows with the keywords are taken out, and grouped together with the other rows from the same kit. These groups are grouped together with the other kits from that year, and the data is exported into a .csv file.
This is done automatically for all the years on the name of the .py file. Example: 2009-2017.py will scan through all the kits between 2009 and 2017.

After using this tool, you can use a software like [nucleotide BLAST](blast.ncbi.nlm.nih.gov/Blast.cgi), to align the sequences.
