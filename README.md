# EZLiveStream
Custom web server for live streaming from embedded devices with USB webcam.

# Hardware:
- You need Odroid or Raspberry Pi any version, or any development board which support Linux/Python.
- Preinstall Unbutu is the best, ready to download any missing python pkg.
- An USB camera, any old-webcam can work, I am using HD one from Odroid.

# Software:

## Download Code:
- Download code above, put it to your home folder, for example, /home/user/ipcam
- Edit livestream.py to customize username and password protection (YOUR_USER_NAME_HERE, and YOUR_PASS_WORD_HERE)
- Edit port you want, default port is 65432.

## Open Router Port:
- Following the Port Forwarding master guide here: https://portforward.com/router-password/ then open your Router port 65432.
- By default, server will work on port 65432, if your IP address is 1.2.3.4, you can access to your server via:
-- http://1.2.3.4:65432

Input your user name and password, then enjoy your live stream.
