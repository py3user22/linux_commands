#!/usr/bin/python3

print("Get a list of all packages on the system\n>> dpkg --list")
print("\n")
print("to see info about a particular pkg\n>> dpkg --list | grep <name_of_pkg>")
print("\n")
print("look for all pkg that contain the string <app_name>\n>> apt-cache search wget2")
print("\n")
print("install example\n>> sudo apt-get install wget2-dev")
print("install ex2\n>> sudo apt-get install dump")
print("\n")

print("to remove app example\n>> sudo apt-get remove wget2")
print("remove ex2\n>> sudo apt-get remove dump")





print("\n")
print("Operation                        Debian")
print("__________________________________\n")

print("Install package                          dpkg --install foo.deb")

print("Install package, dependencies            apt-get install foo")

print("Remove package                           dpkg --remove foo.deb")

print("Remove package, dependencies             apt-get autoremove foo")

print("Update package                           dpkg --install foo.deb")

print("Update package, dependencies             apt-get install foo")

print("Update entire system                     apt-get dist-upgrade")

print("Show all installed packages              dpkg --list")

print("Get information on package               dpkg --listfiles foo")

print("Show packages named foo                  apt-cache search foo")

print("Show all available packages              apt-cache dumpavail foo")

print("What package is file part of?            dpkg --search file")

print("Get list of available printers           lpstat -p -d")

print("check the status of all printers         lpstat -a")

print("cancel a print job                       cancel job-id  or  lprm job-id")

print("move a print job to new printer          lpmove job-id newprinter")

print("update all apps                          sudo apt update")

print("upgrade all apps                         sudo apt upgrade")
print("update your system			sudo apt update && sudo apt upgrade")

print("see the weather                          curl.wttr.in")
print("see the weather2                         inxi -w")

print("move files to other folders              mv file ~/Data/Linux")

print("copy file to another file name           cp file1 new_file1")

print("remove a file                            rm file_ex1.py")

print("change directory to home                 cd ~/.")

print("go back one folder                       cd ..")

print("change to folder from home               cd Data/CySec/")

print("check current directory                  pwd")


print("list files like -l, don't list owner     ls -g")

print("list files and sort by date& time        ls -gt")

print("help manual command to get details       man ls")

print("cut command from nano window             F9")
print("paste command from nano window           F10")
print("full screen & fs exit on any window      F11")

print("to see all prior commands from session   history")

print("move to beginning of line                ctrl +a")
print("move to end of line                      ctrl +e")


print("check what operating system -basic       uname")
print("chk OS -detailed info                    uname -a")


print("to check what graphics driver on PC      sudo lshw -c video")
print("check hardware info                      lshw")


print("\n-----------------------------------------------")
print("create a new user                        sudo useradd newuser")

print("create password for new user             sudo passwd newuser")

print("configure this user to use sudo \n>>")
print("With root privilege, (use sudo visudo) add this line to /etc/sudoers:")
print(">> newuser      ALL=(ALL)     ALL")

print("Alternatively, create a file named\n-----------------------------------")
print(">> /etc/sudoers.d/newuser")       #with just that one line as content.

print("login as or switch to this newuser \n& make sure can execute a cmd that requires root")
print("login command:                          sudo su newuser")

print("login2 command:                         ssh newuser@localhost")
print("\n-----------------------------------------------")


print("Create a new tar archive           tar cvf archive_name.tar dirname/")

print("extract from existing tar          tar xvf archive_name.tar")

print("view existing tar archive          tar tvf archive_name.tar")


print("\n-----------------------------------------------")

print("to check the MAC address            ifconfig")

print("to print a pdf in openoffice        file> export as pdf")

print("to install speedtest CLI		   sudo apt install speedtest-cli")

print("after installation of speedtest     speedtest-cli ,and enter")

print("get the guide of all feature        man speedtest")



print("\n-----------------------------------------------")


print("to make the window full or min           F11")

