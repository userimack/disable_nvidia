import os
import time

def fn():
    print("Run this program using command 'su python <filename>")
    print("Running command 'yum install kernel-headers kernel-devel dkms")
    os.system("yum install kernel-headers kernel-devel dkms")
    print("Cloning the bbswitch repo from github:")
    os.system("git clone https://github.com/Bumblebee-Project/bbswitch.git")
   
    os.chdir("bbswitch")
    print("")
    os.system("pwd")
    print("installing bbswitch:")
    os.system("sudo make -f Makefile.dkms")
    os.chdir("..")
    print("")
    os.system("pwd")


    print("Running program one_nvidia_heating_problem.py")
    os.system("python one_nvidia_heating_problem.py")
    

if __name__ == "__main__":
    fn()