import os

def fn():
    print("Run this program using command 'su python <filename>")
    print("Running command 'mv /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r)-nouveau.img': ")
    os.system("mv /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r)-nouveau.img")

    print("Running command 'dracut --omit-drivers nouveau /boot/initramfs-$(uname -r).img $(uname -r)'")
    os.system("dracut --omit-drivers nouveau /boot/initramfs-$(uname -r).img $(uname -r)")
    print("Reboot needed : Press y to reboot else n to terminate reboot")
    ans = raw_input("Enter your choice: ")
    if (ans=="y" or ans=="Y"):
        os.system("reboot")
    else:
        print("Terminated!!")

if __name__ == "__main__":
    fn()