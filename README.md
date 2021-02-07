# Raspberry Pi Security Camera
This is for a Raspberry Pi with a camera module attached.
The Raspberry Pi camera can be viewed live and record at the same time by streaming the camera module to a mjpeg for viewing on a web browser then recording that stream to a local NAS or SMB file share.
It is done this way because the camera can only be used by one program or script at one time.

This how I set it up and the scripts I used.

Full-Disclosure: I am not an expert with Python and Raspberry Pis so I may not be able to answer every question asked but i will try my best

My Setup:  
Raspberry Pi 3 B+  
Raspberry Pi OS  
Pi Camera V1.3  

1. Put the two files (camerastream.py, camerarecord.py) in the root of the Pi

2. Modify the camerarecord.py file and enter your SMB server name, Share name and the folder in the share to place the videos

	*cd /  
	nano camerarecord.py*  
	
3. Connect Pi to WiFi (easier to do in Desktop mode)

4. Turn on camera
	
	*sudo raspi-config  
	3 Interface Options  
	P1 Camera  
	Yes  
	OK*

5. (Optional) Set Pi OS to boot to console to use less resources

	*sudo raspi-config  
	1 System Options  
	S5 Boot / Auto Login  
	B2 Console Autologin  
	Finish  
	No (To rebooting)*  

6. (Recommended) Enable SSH for remote management
	
	sudo raspi-config  
	3 Interface Options  
	P1 SSH  
	Yes (To enabling)  
	OK  
	Finish  
	passwd  
	(Enter a password for the Pi user - Default Password raspberry)  
	

7. Ensure python and python3 are installed:

    *sudo apt-get update  
    sudo apt-get install python  
    sudo apt-get install python3*  

8. Open /etc/rc.local

	*sudo nano /etc/rc.local*
	
9. Just before the line "exit 0", enter:

	*sudo python /camerastream.py &  
	sudo python /camerarecord.py &*

10. I would recomend checking the scripts are working before rebooting as you can't see any errors that appear when it's running at boot.  
Go to http://PIs-ip-address:8000 and see if it displays a live camera feed.  
You can find the Pi's IP address by entering ifconfig into a terminal, it probably will be 192.168.1.X.  
Temporarily set the "-t" to 10 to record 10 seconds and see if it copies to your share. 
Ether open two terminals in desktop mode and run camerastream.py in one then camerarecord.py in another  
Or do the same with two SSH terminals on another pc. See links at the bottom for info  

11. When your happy it's working:

	sudo reboot  

And watch the SMB share for the recording

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
