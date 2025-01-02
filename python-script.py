#!/usr/env/ python3

import argparse
from subprocess import Popen, PIPE
import time

parser = argparse.ArgumentParser()

parser.add_argument("cpubench", help="number of cpubench", type=int)
parser.add_argument("iobench", help="number of iobench", type=int)

args = parser.parse_args()

num_cpubench = args.cpubench
num_iobench = args.iobench

string = ("cpubench & ; "*num_cpubench + "iobench & ; "*num_iobench)
string+="\n"

p = Popen(["make", "CPUS=1", "qemu"], stdout=PIPE, stdin=PIPE)
time.sleep(5)
p.stdin.write(string.encode())
p.stdin.close()

for line in iter(p.stdout.readline, ""):
    if not line:
        break
    print(line.decode().rstrip())

