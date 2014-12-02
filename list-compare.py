#!/usr/bin/python
#
# Description: This script will ask you for two files containing
#              list (one object per row) to compare.
#              The result will be written to a new file.
#
# Running: Just run the script: ./list-compare.py
#
# Created by: Andreas Bjorshammar <andreas@bjorshammar.se>

import sys


class listCompare:
    def __init__(self):
        self.compare = 'match'
        self.compareOpts = ['match', 'merge']
        self.list1 = []
        self.list2 = []
        self.result = []
        self.output = ''

    def setCompare(self, compare):
        if str(compare) in self.compareOpts:
            self.compare = str(compare)
            return(0, self.compare)
        else:
            return(1, 'Not a supported comparison!')

    def getCompare(self):
        return(self.compare)

    def setList(self, listName, fileName):
        with open(fileName) as f:
            for line in f:
                line = line.strip().lower()
                if line not in listName:
                    listName.append(line)
        return(len(listName))

    def setList1(self, fileName):
        return(self.setList(self.list1, fileName))

    def setList2(self, fileName):
        return(self.setList(self.list2, fileName))

    def setOutputFile(self, fileName):
        if not fileName.endswith('.txt'):
            fileName = str(fileName) + '.txt'
            
        self.output = fileName
        return(self.output)

    def runCompare(self):
        if self.compare == 'match':
            for line in self.list1:
                if line in self.list2:
                    self.result.append(line)
        elif self.compare == 'merge':
            self.result = list(self.list1)
            for line in self.list2:
                if line not in self.result:
                    self.result.append(line)


        # Print results to file
        with open(self.output, 'w') as f:
            for line in self.result:
                f.write(line + '\n')

        return(len(self.result))

comparison = listCompare()

print('\nCompare lists!\n')
list1 = raw_input('File name of the first list: ')
rows = comparison.setList1(list1)
print('Read ' + str(rows) + ' rows of data\n')

list2 = raw_input('File name of the second list: ')
rows = comparison.setList2(list2)
print('Read ' + str(rows) + ' rows of data\n')

output = raw_input('File name of the output file: ')
outputFile = comparison.setOutputFile(output)
print('Output file name: ' + outputFile + '\n')

compareSet = False
while compareSet == False:
    compare = raw_input('Type of comparison <merge|[match]>: ')
    if compare:
        comp = comparison.setCompare(compare)
        if comp[0] == 1:
            print(comp[1])
        else:
            compareSet = True

print('Type of comparison: ' + comparison.getCompare() + '\n')

sys.stdout.write('Running comparison...')
rows = comparison.runCompare()
print('done!\n')
print('Wrote ' + str(rows) + ' rows to "' + output + '"\n')
