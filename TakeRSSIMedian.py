# ble_scan_connect.py:
from bluepy.btle import Peripheral, UUID, AssignedNumbers
from bluepy.btle import Scanner, DefaultDelegate
import time
import statistics


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            #print ("Discovered device", dev.addr)
            pass
        elif isNewData:
            #print ("Received new data from", dev.addr)
            pass

count = 0
dbList = []

InputDeviceName = input("Please Enter Device Name: ")



while True: 

    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(1.0)
    count += 1
    n=0
    addr = []



    for dev in devices:
        addr.append(dev.addr)
        n += 1
        for (adtype, desc, value) in dev.getScanData():
            if(desc=="Complete Local Name" and value==InputDeviceName):
                # print ("%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr, dev.addrType, dev.rssi))
                # print (" %s = %s" % (desc, value))
                dbList.append(dev.rssi)
                

    if count == 10:
        print(dbList)
        print(statistics.median(dbList))
        count = 0
        dbList = []




