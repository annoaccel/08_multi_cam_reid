import subprocess
import os

kk = "--" + "videos"


jj = "videos\init\Double1.mp4"
hh = "videos\init\Single1.mp4 "
oo = "--version v3"


pp = "python" + " " + "demo.py" + " " + kk + " " + jj + " " + hh + " " + oo

subprocess.call('python convert_y3.py model_data/weights/yolov3.weights model_data/models/yolov3.h5', shell=True)

subprocess.call('python convert_y4.py model_data/weights/yolov4.weights model_data/models/yolov4.h5', shell=True)

subprocess.call(
    pp,
    shell=True,
)





