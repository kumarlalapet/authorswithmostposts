#!/usr/bin/python

import sys
import csv

authorcount = 0
oldKey = None

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    data_mapped = line

    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey = data_mapped[0]

    if oldKey and oldKey != thisKey:
        print oldKey , "\t" , authorcount
        oldKey = thisKey
        authorcount = 0
    
    oldKey = thisKey
    authorcount = authorcount + 1

if oldKey != None:
    print oldKey , "\t" , authorcount
