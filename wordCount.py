#!/usr/bin/env python3

"""
File that will count occurrences of every word in a given file
"""
import sys # Provides access to arguments in the command-line
import os  # Interacts with OS
import re  # Has findall()

if len(sys.argv) is not 3:
    print("Should be three arguments")
    exit()

inputFile = sys.argv[1]
outputFile = sys.argv[2]

if not os.path.exists(inputFile):
    print("No such Input file name: %s" % inputFile)
    exit()

if not os.path.exists(outputFile):
    print("No such Output file name: %s" % outputFile)
    exit()
                        
outF = open(outputFile, "w")
wordCount = {}

with open(inputFile) as file:
    for line in file:
        lowerLine = line.lower()
        words = re.findall(r'\w+', lowerLine)
        for word in words:
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1

sortedDict = sorted(wordCount)
with open(outputFile, "w") as file:
    for key in sortedDict:
        file.write(key + " " + str(wordCount[key]) + "\n")
outF.close()
