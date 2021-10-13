# ds18b_script
A python script for DS18b temperature sensor which writes to InfluxDB 2.0

Tested with InfluxDB 2 and Raspberry Pi 4 running Raspbian 64bit. InfluxDB 2 runs on the same host that hosts the script (localhost). 

The script runs 

# Dependencies
Python3. Also:

`pip install influxdb-client`

Edit /boot/config.txt to enable GPIO. Add the following to the `[all]` section:

`dtoverlay=w1-gpio`


Find out manually which unique ID to use. Something like: 

`sudo modprobe w1-gpio`

`sudo modprobe w1-therm`

`ls /sys/bus/w1/devices/28-*/w1_slave` 

You can test it with:

`cat /sys/bus/w1/devices/28-*/w1_slave`

The output should look like: 

```
2a 01 55 05 7f a5 81 66 8c : crc=8c YES
2a 01 55 05 7f a5 81 66 8c t=18625
```


Once you find it copy and paste the path into `temp_sensor1` variable.

Put the InfluxDB 2 token into `token` variable.

Put the hostname into `host` variable.

Change the `org` variable if necessary.

# Daemonize
The script will run continiously in foreground. You can use it with screen or tmux and detach. However cleaner way would be to install `supervisord` and use it with supervisor. 

Install supervisor with: 

`sudo apt install supervisor` 

And add the config for our temperature sensor by creating a new file at `/etc/supervisor/conf.d/temperature.conf`. The contents of the file should be:
```
[program:supervisor_temperature]
command=/usr/bin/t1-logger.py
```
Change the command path to the path of your t1-logger.py script.

check with `sudo supervisorctl status`
```
supervisor_temperature           RUNNING   pid 4963, uptime 0:26:09
```
