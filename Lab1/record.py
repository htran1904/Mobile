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