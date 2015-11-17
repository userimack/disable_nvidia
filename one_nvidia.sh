#!/bin/bash
#Disable nvidia driver script 1


shopt -s nullglob
echo "Enter the root user password::"
#echo `su`

echo "Running command 'mv /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r)-nouveau.img': "

#echo `sudo mv /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r)-nouveau.img`

echo "Running command 'dracut --omit-drivers nouveau /boot/initramfs-$(uname -r).img $(uname -r)'"
#echo `sudo dracut --omit-drivers nouveau /boot/initramfs-$(uname -r).img $(uname -r)`

echo "Reboot required"
echo -e "Press y to reboot else n to terminate reboot"
read ans

if [ $ans == 'y'] ; then
    echo "in"
    #echo `reboot`
else
    echo "You have presses n : Terminated"

