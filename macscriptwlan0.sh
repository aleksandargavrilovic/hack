#!/bin/bash

ifconfig wlan0 down
sleep 1
macchanger -r wlan0
sleep 1
ifconfig wlan0 up
