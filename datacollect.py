#!/usr/bin/python3
#hamid abdul
import time
import  datetime
import subprocess
starttime = time.time()

# Run the Tp-Link smart plug class
class Tp_Link:
    def __init__(self, plugName):
        self.plugName = plugName


    def run(self):
        print("running")
        while True:
            x = open("d.txt", "a")
            y = subprocess.Popen(["pyhs100"], stdout=x)
            time.sleep(60.0 - ((time.time() - starttime) % 60.0))  # run every minutes

    def __repr__(self):
        today = datetime.date.today()
        return "current Time >>>"+today + run()
if __name__ == "__main__":
    tp_link= Tp_Link("Model Name: HS110")
    tp_link.run()




