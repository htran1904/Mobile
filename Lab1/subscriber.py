import pandas
from record import Record

DATA = 'data.csv'

class Subscriber:
    def __init__(self, phoneNumber):
        self.phoneNumber = phoneNumber
        self.originRecords = []
        self.destRecords =[]
        self.getRecords()

    def getRecords(self):
        data = pandas.read_csv(DATA)
        for itm in data.values:
            if itm[1] == self.phoneNumber:
                record = Record(itm[0], itm[1], itm[2], itm[3], itm[4])
                self.originRecords.append(record)
            if itm[2] == self.phoneNumber:
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