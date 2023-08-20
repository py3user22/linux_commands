#!/bin/python3


""" The File-system Hierarchy
All files on a Linux system are stored on file systems, which are organized into a single inverted tree
of directories, known as a file-system hierarchy. This tree is inverted because the root of the tree
is said to be at the top of the hierarchy, and the branches of directories and subdirectories stretch
below the root."""

"""The / directory is the root directory at the top of the file-system hierarchy.
The / character is also used as a directory separator in file names.
For example, if etc is a subdirectory of the / directory, you could refer to that directory as /etc.

Likewise, if the /etc directory contained a file named issue, you could refer to that file as /etc/issue.
Subdirectories of / are used for standardized purposes to organize files by type and purpose.
This makes it easier to find files.
For example, in the root directory, the subdirectory /boot is used for storing files needed to boot the system
"""

rhel_file_system_directories = {
    " / ": "root directory at the top of hierarchy",
    "bin": "contains regular commands and utilities | user commands | same as /usr/bin",
    "boot": "Files needed in order to start the boot process",
    "/boot/grub2/grub.CFG": "grub2s configuration file location",
    "dev": "Contains special device files that are used by the system to access hardware.",
    "": "",
    "etc": "Configuration files specific to this system.\n"
           "\t\tcontains persistent, system-specific configuration data",
    "/etc/fstab": "mountable file system, files used by systemd",
    "/etc/systemd/system/default.target": "used to determine which state or target to boot the host in",
    "/etc/passwd": "\tmapping of usernames to UID, GID, real name of user | used to store local user info.",
    "/etc/shadow": "\twhere the hash & salted password is stored",
    "/etc/group": "\t\tstores info about local groups | 1-name of group, 2- x, 3- GID, 4- list of users in group",
    "/etc/login.defs": "",
    "/etc/profile": "systems default umask -values for bash shell users are defined here",
    "/etc/bashrc": "systems default umask -values for bash shell users are defined here",
    "/etc/sudoers": "info for the sudo users on system",
    "/etc/systemd": "access config files | provides links to /usr/lib/systemd",
    "/etc/yum.repos.d": "repositories | location of repo, security controls (keys, pkg signature chks), status, ",
    "/etc/rsyslog.conf": "rainers syslog, default on linux",
    "/etc/syslog.conf": "",
    "home": "Home directories are where regular users store their personal data and configuration files.",
    "run": "Runtime data for processes started since the last boot. This includes process\n"
           "\t\tID files and lock files | contains non-persistent process runtime data",
    "sbin": "system admin commands | same as /usr/sbin",
    "tmp": "A world-writable space for temporary files.",
    "usr": "Installed software, shared libraries, include files, and read-only program data.",
    "var": "Variable data specific to this system that should persist between boots\n"
           "\t\tcontains files data that is dynamic, such as for databases and website content\n"
           "\t\tlog files, cache directories, printer-spool docs\n"
    "/var/tmp > 30day save & auto delete",
    "/var/log/secure": "\tall sudo commands executed are logged by default to this folder",
    "/var/log/messages": "\tfile that contains system messages in a log | sudo tail -n 5 /var/log/messages",
    "/root": "is the administrative superuser's home directory",
}


for el, fl in rhel_file_system_directories.items():
    print("{}:\t{}".format(el, fl))

print("\n======================\n")
