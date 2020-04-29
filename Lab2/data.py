import os
import pandas
import re

os.system('nfdump -r data/nfcapd.202002251200 -O tstart -o "fmt:%ts,%sa,%da,%byt" > data/nfcapd.txt')

class Record:
    def __init__(self, strinfo):
        arrinfo = strinfo.split(',')
        self.time = arrinfo[0]
        self.sa = re.findall('[\d.]+', arrinfo[1], 0)[0]
        self.sd = re.findall('[\d.]+', arrinfo[2], 0)[0]
        self.bytes = re.findall('[\d.]+', arrinfo[3], 0)[0]
    
    def show(self):
        print('%s\t%s\t%s\t%s' % (self.time, self.sa, self.sd, self.bytes))

class Data:
    def __init__(self, filename):
        self.dataFile = filename
        self.data = self.getAllLine()

    def getAllLine(self):
        fp = open(self.dataFile, 'r')
        allLines = fp.readlines()
        fp.close()
        return allLines[1:-4]