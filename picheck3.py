#!/usr/bin/env python3
#
#  vcgencmd Decoder Python3 Script - RPI Throttling info
#
#  Also a Python & github Refresher... any/all help appreciated
#
#  Converted python2 script from booton of this page:
#  https://harlemsquirrel.github.io/shell/2019/01/05/monitoring-raspberry-pi-power-and-thermal-issues.html
#  Also migrated some of the script from:
#  https://jamesachambers.com/measure-raspberry-pi-undervoltage-true-clock-speeds/ 
#

import subprocess
import re

GET_THROTTLED_CMD = 'vcgencmd get_throttled'
GET_CONFIG_CMD = 'vcgencmd get_config int'
MEASURE_VOLTS_CMD = 'vcgencmd measure_volts '
MEASURE_TEMP_CMD = 'vcgencmd measure_temp'
MEASURE_CLOCK_CMD = 'vcgencmd measure_clock arm' 

THROTTLED_MESSAGES = {
    0: 'Under-voltage!',
    1: 'ARM frequency capped!',
    2: 'Currently throttled!',
    3: 'Soft temperature limit active',
    16: 'Under-voltage has occurred since last reboot.',
    17: 'Throttling has occurred since last reboot.',
    18: 'ARM frequency capped has occurred since last reboot.',
    19: 'Soft temperature limit has occurred'
}

print("\nCurrent Configuration:")
config_response = subprocess.check_output(GET_CONFIG_CMD, shell=True)
pattern = re.compile("(arm|core|gpu|sdram)_freq|over_volt")
for line in config_response.splitlines():
	if pattern.search(str(line)):
		print(str(line, "utf-8"))
		
print("\nCurrent Voltage:")
voltages = ["core", "sdram_c", "sdram_i", "sdram_p"] 
for id in voltages:
	id_volts = subprocess.check_output(MEASURE_VOLTS_CMD+id, shell=True)
	print(id, ":  ", str(id_volts, "utf-8"), end="")
	
print("\nCurrent Temperature:")
current_temp = subprocess.check_output(MEASURE_TEMP_CMD, shell=True)
print(str(current_temp, "utf-8"), end="")
	
print("\nChecking for throttling issues since last reboot...")

throttled_output = subprocess.check_output(GET_THROTTLED_CMD, shell=True)
print(str(throttled_output, "utf-8"))
throttled_bytes = int(throttled_output.split(b'=')[1],0)
throttled_binary = bin(throttled_bytes)

warnings = 0
for position, message in THROTTLED_MESSAGES.items():
    # Check for the binary digits to be "on" for each warning message
    if len(throttled_binary) > position and throttled_binary[0 - position - 1] == '1':
        print(message)
        warnings += 1

if warnings == 0:
    print("\nNo Throttling, Things are looking good!")
else:
    print("\nHouston, we may have a problem!")
