# ds18b_script
A python script for DS18b temperature sensor which writes to InfluxDB 2.0

Tested with InfluxDB 2 and Raspberry Pi 4 running Raspbian 64bit. InfluxDB 2 runs on the same host that hosts the script (localhost). 

# Dependencies

`pip install influxdb-client`

Edit /boot/config.txt to enable GPIO. Add the following to the `[all]` section

`dtoverlay=w1-gpio`


Find out manually which unique ID to use. Something like: 

`sudo modprobe w1-gpio`

`sudo modprobe w1-therm`

`ls /sys/bus/w1/devices/28-*/w1_slave` 

You can test it with:

`cat /sys/bus/w1/devices/28-*/w1_slave`

The output should look like: 

`2a 01 55 05 7f a5 81 66 8c : crc=8c YES`

`2a 01 55 05 7f a5 81 66 8c t=18625`


Once you find it copy and paste the path into `temp_sensor1` variable.

Put the InfluxDB 2 token into `token` variable.

Put the hostname into `host` variable.

Change the `org` variable if necessary.
