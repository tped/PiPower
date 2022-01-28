# PiPower
Raspberry Pi Power &amp; Throttling Decoder (vcgencmd) - Python 3

A Python & github Refresher project ... seems to work:  any/all suggestions appreciated

Converted python2 script from booton of this page:
https://harlemsquirrel.github.io/shell/2019/01/05/monitoring-raspberry-pi-power-and-thermal-issues.html
Also migrated some of the bash script from:
https://jamesachambers.com/measure-raspberry-pi-undervoltage-true-clock-speeds/ 

Output now looks like this:
```
Current Configuration:
arm_freq=2000
gpu_freq=600
gpu_freq_min=250
over_voltage=6
over_voltage_avs=-11250

Current Voltage:
core :   volt=1.0187V
sdram_c :   volt=1.1000V
sdram_i :   volt=1.1000V
sdram_p :   volt=1.1000V

Current Temperature:
temp=46.7'C

Checking for throttling issues since last reboot...
throttled=0x0

No Throttling, Things are looking good!
```
