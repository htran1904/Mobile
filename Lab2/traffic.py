from data import *
from constants import *

class Traffic:
    def __init__(self, ipAddr):
        self.ownRecords = self.getAllRecords(ipAddr)
        self.flow = self.getFlow()

    def getAllRecords(self, ipAddr):
        ownRecords = []
        dt = Data(DATAFILENAME)
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