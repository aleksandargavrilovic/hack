#!/bin/bash

ifconfig eth0 down
sleep 2
macchanger -r eth0
sleep 2
ifconfig eth0 up


