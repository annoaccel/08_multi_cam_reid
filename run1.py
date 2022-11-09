import subprocess
import os

kk = "--" + "videos"


jj = "videos\init\Double1.mp4"
hh = "videos\init\Single1.mp4 "
oo = "--version v3"


pp = "python" + " " + "demo.py" + " " + kk + " " + jj + " " + hh + " " + oo

subprocess.call(
    pp,
    shell=True,
)





