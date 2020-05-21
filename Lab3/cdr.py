import pandas

class Record:
    def __init__(self, timestamp, msidnOrigin, msisdnDest, callDuration, smsNumber):
        self.timestamp = timestamp
        self.msidnOrigin = msidnOrigin
        self.msisdnDest = msisdnDest
        self.callDuration = callDuration
        self.smsNumber = smsNumber

    def billSms(self):
        if self.smsNumber > 5:
            return self.smsNumber - 5
        else:
            return 0

    def billCall(self):
        return self.callDuration

    def show(self):
        print(self.msidnOrigin, self.msisdnDest)

    def toStringArray(self):
        return [self.timestamp, str(self.msidnOrigin), str(self.msisdnDest), str(self.callDuration), str(self.smsNumber)]

class Subscriber:
    def __init__(self, phoneNumber):
        self.phoneNumber = phoneNumber
        self.originRecords = []
        self.destRecords =[]
        self.getRecords()

    def getRecords(self):
        data = pandas.read_csv('cdr.csv')
        for itm in data.values:
            if str(itm[1]) == self.phoneNumber:
                record = Record(itm[0], itm[1], itm[2], itm[3], itm[4])
                self.originRecords.append(record)
            if str(itm[2]) == self.phoneNumber:
                record = Record(itm[0], itm[1], itm[2], itm[3], itm[4])
                self.destRecords.append(record)
    
    def smsBill(self):
        total = 0
        for record in self.originRecords:
            total += record.billSms()
        return total

    def originCallBill(self):
        total = 0
        for record in self.originRecords:
            total += record.billCall()
        return total
    
    def destCallBill(self):
        total = 0
        for record in self.destRecords:
            total += record.billCall()
        return total