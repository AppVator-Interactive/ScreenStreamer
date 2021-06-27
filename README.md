# ScreenStreamer
Stream screen over HTTP

Installing
==========

Install all required libraries by running:

    pip install -r requirements.txt
    
Configuration
=============

Open `config.py`

    host = "192.168.0.136" # IP of stream. For example: put here IP of your PC
    port = "80" # Port of stream. Default is 80
    width = 1920 # Width of your screen
    height = 1080 # Height of your screen
    top = 0 # Top offset
    left = 0 # Left offset
    screen = 1 # Number of screen to capture. Default is 1

Run
===

To run this program type:

    python stream.py
