#!/usr/bin/python2

# Kindle CPU Stat display
# Tim Bowers
# March 2019
#

import datetime
import socket
import sys
import time
import codecs
import re
from xml.dom import minidom

template = 'cpu-script-preprocess.svg'

#
# Preprocess SVG
#

cpu = open('/sys/class/hwmon/hwmon1/device/temp1_input','r')
for line in cpu:
	cpu_temp = (float(line) / 1000)


nb = open('/sys/class/hwmon/hwmon1/device/temp3_input','r')
for line in nb:
	nb_temp = (float(line) / 1000)

#hdd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((host,port))
#hdd_temp = s.recv(4096)
#s.close()

hdd_temp = "test"

load = "100"

def colon_split(a):
    if a.count(":") == 1:
            return a.split(":")[0]
    else:
            return ":".join(a.split(":", 2)[:2])


with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])
    uptime_string = str(datetime.timedelta(seconds = uptime_seconds))

uptime = colon_split(uptime_string)
#uptime1 = re.sub(r',\s' , ',\n', uptime)
uptime1 = uptime.split(', ')

dtnow=datetime.datetime.now().strftime("%d-%b %H:%M")

# Open SVG to process
output = codecs.open(template , 'r', encoding='utf-8').read()

output = output.replace('CPU_V',str(cpu_temp))
output = output.replace('NB_V',str(nb_temp))
output = output.replace('HDD_V',str(hdd_temp))
output = output.replace('LOAD_V',str(load))
output = output.replace('UPTIME1_V',str(uptime1[0]))
output = output.replace('UPTIME2_V',str(uptime1[1]))

# Insert current time
# (thanks Jennifer http://www.shatteredhaven.com/2012/11/1347365-kindle-weather-display.html)
output = output.replace('DATE_VALPLACE',str(dtnow))

# Write output
codecs.open('cpu-script-output.svg', 'w', encoding='utf-8').write(output)

# EOF
