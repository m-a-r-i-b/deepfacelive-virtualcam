import pyvirtualcam
import cv2

# Create virtual loopback device(s)
# modprobe v4l2loopback video_nr=2,7

# Check if virtual device is created successfully
# ls -1 /sys/devices/virtual/video4linux

# Check UDP traffic on port
# tcpdump -i lo -n udp port 1234

cap = cv2.VideoCapture('udp://127.0.0.1:1234')

fmt = pyvirtualcam.PixelFormat.BGR

with pyvirtualcam.Camera(width=640, height=480, fps=30,device='/dev/video2',fmt=fmt) as cam:
    print(f'Using virtual camera: {cam.device}')
    while True:
        ret, frame = cap.read()
        cam.send(frame)
        cam.sleep_until_next_frame()