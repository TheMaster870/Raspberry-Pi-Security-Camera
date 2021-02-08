
# How to set a record timer
You may want to only record the camera between a certain time,  
Maybe to reduce on storage or it's not needed between a time, it's quite simple.

Edit the camerarecord.py file, and add the following after the while loop starts but before it starts recording:  
		   
    #Get the currnt hour in 24 hour format  
    thehour = datetime.datetime.now().strftime("%H")  
    #If the hour is before 7AM or after 8PM wait 5 mins and try again  
    if int(thehour) > 20 or int(thehour) < 7:  
        print("Hour is later than 8PM or before 7AM")  
        sleep(300)  
    else:  
    

It should now look something like this:  

    #/usr/bin python  
    #Import the nessesery modules  
    from time import sleep  
    import datetime  
    import os  

    #Loop Endlessly  
    while True:  
        #Get the currnt hour in 24 hour format  
        thehour = datetime.datetime.now().strftime("%H")  
        #If the hour is before 7AM or after 8PM wait 5 mins and try again  
        if int(thehour) > 20 or int(thehour) < 7:  
            print("Hour is later than 8PM or before 7AM")  
            sleep(300)  
        else:  
            print("Hour is between 7AM and 8PM")  
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
            os.system("ffmpeg -f mjpeg -i http://127.0.0.1:8000/stream.mjpg -r 10 -t 60 " + videoname + " -y -an")  
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

You can now change the times in the if statement to suit you.  
Remember it's in 24 hour format
