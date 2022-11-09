import streamlit as st
import subprocess
import os

# import streamlit as st
# from demo import multicam

# # from demo import multicam

# with st.form(key="input form for video"):
#     vid_input = st.text_input("video_in", "input location")
#     vid_output = st.text_input("video_out", "output location")
#     connect1 = st.form_submit_button(label="Connect0")
# disconnect = st.button("Disconnect!")


# if connect1:
#     st.write(vid_input)
#     st.write(vid_output)
#     # multicam(vid_input, vid_output)


kk = "--" + "videos"


jj = "videos\init\Double1.mp4"
hh = "videos\init\Single1.mp4 "
oo = "--version v3"


pp = "python" + " " + "demo.py" + " " + kk + " " + jj + " " + hh + " " + oo


subprocess.call(
    pp,
    shell=True,
)
