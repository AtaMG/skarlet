#!/usr/bin/python3

import sys
import os
import psutil
import json
from psutil._common import bytes2human


def disk():
    temp = "%-17s %8s %8s %8s %5s%% %9s  %s"
    print(temp % ("Device", "Total", "Used", "Free", "Use ", "Type",
                  "Mount"))
    for part in psutil.disk_partitions(all=False):
        usage = psutil.disk_usage(part.mountpoint)
        print(temp % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint))


print("CPU cores utilization: ", psutil.cpu_percent(interval=1, percpu=True))
print("Memory utilization (%): ", psutil.virtual_memory().percent)
print("Disk utilization : ")
disk()
print("Network Status:\n Ethernet Name:\n \tBytes Sent\n \tBytes Received\n \tPackets Sent\n \tPacket Received\n "
      "\tError In\n \tError "
      "Out\n \tDrop In\n \tDrop Out")
print(json.dumps(psutil.net_io_counters(pernic=True), indent=4, sort_keys=False))
