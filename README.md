# Raspberry Pi Security Camera
This is for a Raspberry Pi with a camera module attached.
The Raspberry Pi camera can be viewed live and record at the same time by streaming the camera module to a mjpeg for viewing on a web browser then recording that stream to a local NAS or SMB file share.
It is done this way because the camera can only be used by one program or script at one time.

This how I set it up and the scripts I used.

Full-Disclosure: I am not an expert with python and Raspberry Pis so I may not be able to answer every question asked but i will try my best

My Setup:  
Raspberry Pi 3 B+  
Raspberry Pi OS  
Pi Camera V1.3  

1. Put the two files (camerastream.py, camerarecord.py) in the root of the Pi
2. Modify the camerarecord.py file and enter your SMB server name, Share name and the folder in the share to place the videos

	*cd /  
	nano camerarecord.py*  
	
3. Turn on camera
	
	*sudo raspi-config  
	3 Interface Options  
	P1 Camera  
	Yes  
	OK*

4. (Optional) Set Pi OS to boot to console to use less resources

	*sudo raspi-config  
	1 System Options  
	S5 Boot / Auto Login  
	B2 Console Autologin  
	Finish  
	No (To rebooting)*  

5. (Recommended) Enable SSH for remote management
	
	sudo raspi-config  
	3 Interface Options  
	P1 SSH  
	Yes (To enabling)  
	OK  
	Finish  
	passwd  
	(Enter a password for the Pi user - Default Password raspberry)  
	

6. Ensure python and python3 are installed:

    *sudo apt-get update  
    sudo apt-get install python  
    sudo apt-get install python3*  

7. Open /etc/rc.local

	*sudo nano /etc/rc.local*
	
8. Just before the line "exit 0", enter:

	*sudo python /camerastream.py &  
	sudo python /camerarecord.py &*

9. I would recomend checking the script are working before rebooting as you can't see any errors that appear when running at boot.  
Ether open two terminals in desktop mode and run camerastream.py in one then camerarecord.py in another  
Or do the same with two SSH terminals on another pc. See links at the bottom for info

# Useful Sites  
camerastream:  
http://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming

SSH:  
https://www.raspberrypi.org/documentation/remote-access/ssh/  
https://www.raspberrypi.org/documentation/remote-access/ssh/windows10.md  

smbclient:  
https://www.samba.org/samba/docs/current/man-html/smbclient.1.html  
https://www.itprotoday.com/linux/linuxs-smbclient-command

Run program at startup:  
https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/
