import tkinter as tk
import requests
from subscriber import Subscriber
    
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWindow()

    def createWindow(self):
        self.labelPhoneNumber = tk.Label(self, text='Phone Number:')
        self.labelPhoneNumber.pack()
        self.txtPhoneNumber = tk.Text(self, height=1, width=9)
        self.txtPhoneNumber.insert('1.0', '915642913')
        self.txtPhoneNumber.pack()

        self.topBtFrame = tk.Frame(self)
        self.topBtFrame.pack()

        self.addBtToFrame(self.topBtFrame, 'Billing', self.handleBilling)
        self.addBtToFrame(self.topBtFrame, 'Tariff', self.handleCheckTariff)
        self.addBtToFrame(self.topBtFrame, 'Record', self.handleGetRecords)

        self.botframe = tk.Frame(self)
        self.botframe.pack()

    def handleBilling(self):
        sb = Subscriber(int(self.txtPhoneNumber.get('1.0', 'end-1c')))
        sms = sb.smsBill()
        originCall = sb.originCallBill()
        destCall = sb.destCallBill()
        text = '______Bill______\nSMS: %drub\nOutgoing Call: %drub\nIncoming Call: %drub\nTotal: %drub\n' \
            % (sms, originCall, destCall, sms+originCall+destCall)
        self.showContent('text', text)

    def handleCheckTariff(self):
        text = '______Tariff______\nYour phone number: %s\nYour tarrif:\n1rub/min outgoing call\n1rub/min incoming call\nsms - 1rub/sms (5 first sms for free)' \
                % self.txtPhoneNumber.get('1.0', 'end-1c')
        self.showContent('text', text)

    def handleGetRecords(self):
        sb = Subscriber(int(self.txtPhoneNumber.get('1.0', 'end-1c')))
        table = [
            ['timestamp', 'msisdn_origin', 'msisdn_dest', 'call_duration', 'sms_number']
        ]
        for rc in sb.originRecords + sb.destRecords:
            table.append(rc.toStringArray())
        self.showContent('table', table)

    def showContent(self, kind, content):
        childWids = self.botframe.winfo_children()
        for item in childWids:
            item.grid_forget()
        if kind == 'table':
            for i in range(len(content)):
                for j in range(5):
                    en = tk.Entry(self.botframe, width=17)
                    en.insert(0, content[i][j])
                    en.grid(row=i, column=j)
        if kind == 'text':
            ct = tk.Text(self.botframe, height=6, width=88)
            ct.insert('1.0', content)
            ct.grid()

    def addBtToFrame(self, frame, btName, cmd):
        bt = tk.Button(frame, text=btName, command=cmd)
        bt.pack(side='left', ipadx=20, padx=5, pady=5)

    def showBill(self):
        print(5)

    def checkTariff(self):
        print(7)

    def showRecords(self):
        print(7)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.master.title("Proccessing and billing CDR")
    app.mainloop()