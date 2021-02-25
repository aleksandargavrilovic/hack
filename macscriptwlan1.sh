#!/bin/bash

ifconfig wlan1 down
sleep 1
macchanger -r wlan1
sleep 1
ifconfig wlan1 up
