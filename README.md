# Raspbery_switch
This is a project that use a switch to shut down the Raspberry Pi system. You can follow the tutorial on Instructables:
https://www.instructables.com/id/Raspberry-Pi-Zero-Switch-Off-by-Button/

Or

Make the shutdown.py file on yuor Raspberry Pi desktop and editing rc.local.

EDITING RC.LOCAL

On your Pi, edit the file /etc/rc.local using the editor of your choice. You must edit with root, for example:

sudo nano /etc/rc.local
Add commands in the rc.local file below the comment, but leave the line exit 0 at the end, then save the file and exit.

by (https://www.raspberrypi.org/documentation/linux/usage/rc-local.md)
