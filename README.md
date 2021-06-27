# ScreenStreamer
Stream screen over HTTP

Installing
==========

Install all required libraries by running:

    pip install -r requirements.txt
    
Configuration
=============

Open `config.py`

    # IP of stream. For example: put here IP of your PC
    host = "192.168.0.136"
    # Port of stream. Default is 80
    port = "80" 
    # Width of your scree
    width = 1920
    # Height of your screen
    height = 1080 
    # Top offset
    top = 0 
    # Left offset
    left = 0 
    # Number of screen to capture. Default is 1
    screen = 1 

Run
===

To run this program type:

    python stream.py
    
Watch
=====

To see the stream type ip adress and port plus /stream. If port is 80 you do't have to type it. For example:
    
    http://192.168.0.136/stream
    
Example for other port than 80:
    
    http://192.168.0.136:90/stream
