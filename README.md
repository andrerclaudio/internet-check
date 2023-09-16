# internet-check
A simple script to continuously check if the internet connection is Ok and force Reset otherwise.

To make it work, you need to chown -R root:root ./internet-check
Also, it is good to add it as service.


[Unit]
Description=Internet Connection Checker Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/internet-check/internet-check.py
WorkingDirectory=/home/pi/internet-check
Restart=always
User=root
Group=root

[Install]
WantedBy=multi-user.target
