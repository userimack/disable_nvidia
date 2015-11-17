import os

def fn():
    print("Run this program using command 'su python <filename>'  after the reboot ")
    print("Running command 'modprobe -r nouveau'")
    os.system("modprobe -r nouveau")

    print("Running command 'modprobe bbswitch'")
    os.system("modprobe bbswitch")

    print("Status: ")    
    os.system("tee /proc/acpi/bbswitch <<< OFF")
    


if __name__ == "__main__":
    fn()