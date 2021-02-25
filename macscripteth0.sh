#!/bin/bash

ifconfig eth0 down
sleep 1
macchanger -r eth0
sleep 1
ifconfig eth0 up


