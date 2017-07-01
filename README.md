# iGEM Tools
Welcome to the iGEM tools repository created by iGEM UiO. We hope that you can share the benefits of these tools that have saved us many hours. We only have one tool so far, but many more may come.

## Sequence cataloging (Python 3.x)
This tool was conceved on a summerday session, when we needed to find the sequences that may have been similar to one of our parts, the GFP gene. In order to determine if our part is new, modified, or identical compared to existing parts.
But, as you may have already seen, the iGEM part registry is a nightmare. This tool, scans through the [iGEM Official Distribution](http://parts.igem.org/assembly/libraries.cgi) for the keywords provided by the user.
The rows with the keywords are taken out, and grouped together with the other rows from the same kit. These groups are grouped together with the other kits from that year, and the data is exported into a .csv file (can be read with Xcel).


After using this tool, you can use a software like [nucleotide BLAST](blast.ncbi.nlm.nih.gov/Blast.cgi), to align the sequences.


## Seq_Cat_Script_for_2004_2017.py (Python 3.x)
This tool does a similar job as the previous one, and is not finished yet, but the outputs are usable as of now.
The tool searches in all the iGEM distribution files for complete iGEM history for the keyword provided by the user, and corresponding rows from all the respective years(files) are extracted and put together in a single file. Here, as of the current functionality, we will not be getting a year-wise distribution of files, but all the data is collected in a single file.
The following table should be helpful to sort the resultant output file according to years :
see the table as [image](http://prntscr.com/fqhfdo)
