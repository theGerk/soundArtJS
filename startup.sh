#!/bin/sh

#sleep 20 seconds to wait for an internet connection
sleep 20s

#pull any updates
git pull

#RUN THE PROGRAM!!! :D
python3 /home/pi/soundArtJS/bathroomNoise.py
