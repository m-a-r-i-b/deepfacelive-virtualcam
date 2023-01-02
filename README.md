# Deepfacelive-virtualcam
Following steps allows you to create a virtual camera and write a custom stream to its output. Note this guide is specific to <b>LINUX</b>.

### Step 1

Install v4l2loopback utility
```
sudo apt install v4l2loopback-dkms
```


### Step 2

Create a virtual camera
```
modprobe v4l2loopback video_nr=2
```



### Step 3

Verify virtual camera has been created
```
ls -1 /sys/devices/virtual/video4linux

Output:
video2
```


### Step 4

Modify start script of deepfacelive app, allowing it to use host network
```
git clone https://github.com/iperov/DeepFaceLive
cd DeepFaceLive/build/linux

# In start.sh script add '--network host' in the docker run command

# BEFORE
docker run --ipc host --gpus all -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $DATA_FOLDER:/data/ $CAM0 $CAM1 $CAM2 $CAM3  --rm -it deepfacelive

# AFTER
docker run --network host --ipc host --gpus all -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $DATA_FOLDER:/data/ $CAM0 $CAM1 $CAM2 $CAM3  --rm -it deepfacelive

# Start the app, remember to pass the '-c' flag to pass host cameras to docker container
./start.sh -c
```



### Step 5

Verify deepfacelive app container is outputing a UDP stream on set port
```
tcpdump -i lo -n udp port 1234
```



### Step 6

Start the virtualcam script
```
python virtualcam.py
```

