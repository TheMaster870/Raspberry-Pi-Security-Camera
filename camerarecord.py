#/usr/bin python
#Import the necessary modules
from time import sleep
import datetime
import os

#Loop Endlessly
while True:
    #Get current date and time
    thedatetime = datetime.datetime.now().strftime("%d-%m-%Y.%H,%M,%S")
    #Set the name for the video
    videoname = "video" + str(thedatetime) + ".flv"
    print("Recording " + videoname)
    #Get the mjpg stream and convert it to the videoname and extention
    #Set the recording framerate by changing the number after -r (note: the actual output framerate can be less if you Pi can't keep up)
    #Set the length of the recording by changing the number after -t (its in seconds)
    #-y overwrites the video if a file with the same name already exists (not likely to though)
    #-an means it doesn't record the audio (remove this if you want to add audio to the recording)
    os.system("ffmpeg -f mjpeg -i http://127.0.0.1:8000/stream.mjpg -r 10 -t 300 " + videoname + " -y -an")
    print("done recording")
    #Move the recording to a NAS or SMB storage
    #This is setup for a share with no authentication, on a NAS called videosnas, a share called stuff and to save the recording in a folder called cctv
    #Add "-U yourUsername%yourPassword" if your Share requres authentication and enter your username and password, leave out "%yourPassword" if there is no password for the user
    os.system("smbclient //videosnas/stuff -N -c 'cd cctv ; put " + videoname + "'")
    print("copied " + videoname)
    #Delete the recording after copying to free up space on the Pi's SD card
    os.remove("/" + videoname)
    print("deleted " + videoname)
    #Loop
