#!/usr/bin/env python

import os
from time import time, sleep
import daemon

def main_program():
    while True:
        cnt = 0
        while cnt < 1440: # run for 24h
            sleep(60 - time() % 60) # run every 60 second
            os.system("date -u >> top_mem_consumers.log\n"
                      "ps -o pid,user,%mem,command ax | sort -b -k3 -r | awk '$3 >= 4' >> top_mem_consumers.log\n"
                      "date -u >> top_cpu_consumers.log\n"
                      "ps aux k-pcpu | head -6 | awk '$3 >= 4' >> top_cpu_consumers.log")
            cnt += 1

with daemon.DaemonContext(
        chroot_directory=None,
        working_directory='./'):
    main_program()
