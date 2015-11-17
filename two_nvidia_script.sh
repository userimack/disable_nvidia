#!/bin/bash
#Disable nvidia driver script 2


echo "Running command 'modprobe -r nouveau'"
echo`sudo modprobe -r nouveau`

echo "Running command 'modprobe bbswitch'"
echo `sudo modprobe bbswitch`

shopt -s nullglob
echo "Status: "   
echo `sudo tee /proc/acpi/bbswitch <<< OFF`
    
