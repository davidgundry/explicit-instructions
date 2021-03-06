# 
# This script was used to process the raw data collected from the
# game. The data is collected using the non-relational database
# service restdb.io. It was downloaded in JSON format. The purpose
# of this processing is to make the data entirely anonymous.
#
# This script first defines a number of functions. It declares a
# variable `f`, which is the filename of the raw data file, as
# downloaded from the database. It strips data out of this file
# using regular expressions. (This is adapted from the script
# written for the previous experiment)
#
# The script will write files to disk in the folder "data". It
# will also generate files in the same directory as the source file.
# Many of these are for sanity checking purposes and should be
# deleted as they are not fully anonymised. The important files are:
#
# * data.json (containing the main data)
# * duration.csv (associating duration and condition)
# * age-gender.csv (associating age and gender)

import random
import re

filename = "raw/raw.json"

def shuffle(filename):
    with open(filename) as f:
        lines = f.readlines()
    random.shuffle(lines)
    outputFile = filename
    with open(outputFile, "w") as f:
        f.writelines(lines)
    return outputFile

def removeLinesWithoutProlificPIDS(filename):
    output = []
    excluded = []
    with open(filename) as f:
        for line in f:
            x = re.search('prolificPID', line) 
            if x:
                output.append(line)
            else:
                excluded.append(line)
    
    outputFile = filename+"+nonPIDremoved"
    with open(outputFile, "w") as f:
        f.writelines(output)
    with open(filename+"+PIDexcluded", "w") as f:
        f.writelines(excluded)
    return outputFile
    
def removeLinesWithBadAgesOrLanguages(filename):
    game, tool = 0, 0
    output = []
    excluded = []
    with open(filename) as f:
        for line in f:
            x = re.search('"([\-0-9]+)","((male)|(female)|(other)|(prefer))","([a-z]+)"', line) 
            language = x.group(7)
            if language == "other":
                excluded.append(line)
            else:
                age = int(x.group(1))
                if (age >= 18):
                    output.append(line)
                else:
                    excluded.append(line)

    
    outputFile = filename+"+badLinesRemoved"
    with open(outputFile, "w") as f:
        f.writelines(output)
    with open(filename+"+BadLines", "w") as f:
        f.writelines(excluded)
    return outputFile

def removeMarkers(filename):
    with open(filename) as f:
        content = f.read()
    content = re.sub(',"studyID":"[a-z0-9]+","prolificPID":"[a-z0-9]+","sessionID":"[a-z0-9]+","uid":[0-9]+',"",content)
    content = re.sub('"loadTime":[0-9]+,"uploadTime":[0-9]+,',"",content)
    content = re.sub('"_id":"[a-z0-9]+",',"",content)
    outputFile = filename+"+markersRemoved"
    with open(outputFile, "w") as f:
        f.write(content)
    return outputFile

def createDurationCSV(filename):
    outputFile = "data/duration.csv"
    with open(filename) as f:
        with open(outputFile, "w") as csv:
            for line in f:
                x = re.search('"loadTime":([0-9]+),"uploadTime":([0-9]+)', line)
                y = re.search('(HighFraming|LowFraming)', line)
                if (x == None or y == None):
                    print("duration skipped line: " + line)
                else:
                    start = int(x.group(1))
                    end = int(x.group(2))
                    dur = (end-start)/1000
                    condition = y.group(1)
                    csv.write(condition + "," + str(dur) + "\n")
    return outputFile

def createAgeGenderCSV(filename):
    with open(filename) as f:
        content = f.read()
    content = re.sub('.+"([\-0-9]+)","((male)|(female)|(other)|(prefer))","([a-z]+)".+', r'\1,\2', content)
    outputFile = "data/age-gender.csv"
    with open(outputFile, "w") as f:
        f.write(content)
    return outputFile

def justData(filename):
    with open(filename) as f:
        content = f.read()
    content = re.sub('"duration":[0-9\.]+,', '', content)
    content = re.sub('"([\-0-9]+)","((male)|(female)|(other)|(prefer))","([a-z]+)"', r'"\7"', content)
    content = re.sub('\["start"\],?', '', content) # Recoding pressing the "start" button to start the game. This shouldn't have been logged.
    outputFile = "data/data.json"
    with open(outputFile, "w") as f:
        f.write(content)
    return outputFile

def wrapWithSquareBrackets(filename):
    with open(filename) as f:
        content = f.read()
    with open(filename, "w") as f:
        f.write("[\n")
        f.write(content)
        f.write("]")

f = filename
f = removeLinesWithoutProlificPIDS(f)
f = removeLinesWithBadAgesOrLanguages(f)
dcsv = createDurationCSV(f)
shuffle(dcsv)
f = removeMarkers(f)
agcsv = createAgeGenderCSV(f)
shuffle(agcsv)
jdjson = justData(f)
shuffle(jdjson)
wrapWithSquareBrackets("data/data.json")

