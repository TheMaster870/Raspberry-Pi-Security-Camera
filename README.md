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

1. Clone this git and move the two .py files to the root
	
	*sudo apt-get install git  
	git clone https://www.github.com/themaster870/raspberry-pi-security-camera  
	cd raspberry-pi-security-camera  
	sudo mv camerastream.py /  
	sudo mv camerarecord.py /*

2. Modify the camerarecord.py file and enter your SMB server name, Share name and the folder in the share to place the videos

	*cd /  
	sudo nano camerarecord.py*  
	
3. Connect Pi to WiFi
	
	*sudo raspi-config  
	1 System Options  
	S1 Wireless LAN*  
	Enter your WiFi SSID and it's password
	
4. Set password for pi
	
	*sudo raspi-config
	1 System Options
	S3 Password*  
	Enter a password for the default pi user
	
4. Turn on camera
	
	*sudo raspi-config  
	3 Interface Options  
	P1 Camera  
	Yes  
	OK*

5. Set Pi OS to boot to console to use less resources

	*sudo raspi-config  
	1 System Options  
	S5 Boot / Auto Login  
	B2 Console Autologin  
	Finish  
	No (To rebooting)*  

6. Enable SSH for remote management
	
	sudo raspi-config  
	3 Interface Options  
	P1 SSH  
	Yes (To enabling)  
	OK  
	Finish  
	passwd  
	(Enter a password for the Pi user - Default Password raspberry)  
	

7. Ensure python, python3 and smbclient are installed and reboot:

    *sudo apt-get update  
    sudo apt upgrade  
    sudo apt-get install python  
    sudo apt-get install python3  
    sudo apt-get install smbclient  
    sudo apt-get install python-picamera python3-picamera  
    sudo apt-get install ffmpeg
    sudo reboot*  

8. Open /etc/rc.local

	*sudo nano /etc/rc.local*
	
9. Just before the line "exit 0", enter:

	*sudo python3 /camerastream.py &  
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
