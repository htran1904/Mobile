import tkinter as tk
from traffic import *
import datetime
import matplotlib.pyplot as plt
from constants import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.traffic = Traffic(IP)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.labelIpAddr = tk.Label(self, text='IP')
        self.labelIpAddr.grid(row=1, column=1, padx=8, pady=8)

        self.txtIpAddr = tk.Text(self, height=1, width=18)
        self.txtIpAddr.insert('1.0', IP)
        self.txtIpAddr.grid(row=1, column=2, padx=8, pady=8)

        self.btCheckTariff = tk.Button(self, text='Check', command=self.showCalculation)
        self.btCheckTariff.grid(row=4, column=1, padx=8, pady=8)

        self.labelCheckTariff = tk.Label(self, text='Flow (MB)')
        self.labelCheckTariff.grid(row=2, column=1, padx=8, pady=8)

        self.txtTraffic = tk.Text(self, height=1, width=18)
        self.txtTraffic.grid(row=2, column=2, padx=8, pady=8)

        self.labelTotalPrice = tk.Label(self, text='Total Price (ruble)')
        self.labelTotalPrice.grid(row=3, column=1, padx=8, pady=8)

        self.txtTotalPrice = tk.Text(self, height=1, width=18)
        self.txtTotalPrice.grid(row=3, column=2, padx=8, pady=8)

        self.btAnalysisByDiagram = tk.Button(self, text='Analysis', command=self.analysisByDiagram)
        self.btAnalysisByDiagram.grid(row=4, column=2, padx=8, pady=8)

    def cleanOldData(self):
        self.txtTotalPrice.delete('1.0', 'end-1c')
        self.txtTraffic.delete('1.0', 'end-1c')

    def showCalculation(self):
        self.cleanOldData()
        trf = Traffic(IP)
        self.txtTraffic.insert('1.0', str(round(trf.flow / 1024, 2)))
        self.txtTotalPrice.insert('1.0', str(round(trf.billing(), 2)))

    def analysisByDiagram(self):
        data = Traffic(IP).ownRecords
        timeArr = []
        totalTrafficArr = []
        currentSumTraffic = 0
        for rc in data:
            timeArr.append(datetime.datetime.strptime(rc.time, '%Y-%m-%d %H:%M:%S.%f'))
            currentSumTraffic += float(rc.bytes)/1024
            totalTrafficArr.append(currentSumTraffic)
        plt.plot(timeArr, totalTrafficArr)
        plt.xticks(rotation=30)
        plt.ylabel("Flow (MB)")
        plt.xlabel('Time')
        plt.title('Diagram of flow')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.master.title("Proccess and billing NetFlow")
    app.mainloop()