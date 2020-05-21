import pandas
import re

class Record:
    def __init__(self, strinfo):
        arrinfo = strinfo.split(',')
        self.time = arrinfo[0]
        self.sa = re.findall('[\d.]+', arrinfo[1], 0)[0]
        self.sd = re.findall('[\d.]+', arrinfo[2], 0)[0]
        self.bytes = re.findall('[\d.]+', arrinfo[3], 0)[0]

class Data:
    def __init__(self, filename):
        self.dataFile = filename
        self.data = self.getAllLine()

    def getAllLine(self):
        fp = open(self.dataFile, 'r')
        allLines = fp.readlines()
        fp.close()
        return allLines[1:-4]

class Traffic:
    def __init__(self, ipAddr):
        self.ownRecords = self.getAllRecords(ipAddr)
        self.flow = self.getFlow()

    def getAllRecords(self, ipAddr):
        ownRecords = []
        dt = Data('netflow.txt')
        for line in dt.data:
            rc = Record(line)
            if rc.sa == ipAddr or rc.sd == ipAddr:
                ownRecords.append(rc)
        return ownRecords
    
    def getFlow(self):
        totalFlow = 0.0
        for rc in self.ownRecords:
            totalFlow += float(rc.bytes)
        return totalFlow

    def billing(self):
        return max(0, self.flow / 1024 - 1000) * 1