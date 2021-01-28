#!/usr/bin/env python3
import subprocess
import optparse

parser=optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="interfcae to change MAC Address")
parser.add_option("-m", "--mac", dest="new_mac", help="new Mac address")
(options, arguments)=parser.parse_args()

interface = options.interface
new_mac = options.new_mac
print("[+]changing the mac address for  "  + interface +  " to "  +new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
