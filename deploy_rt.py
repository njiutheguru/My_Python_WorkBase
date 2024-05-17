## since the machine learning model runs infinitely on the embedded system, then we need to capture the output in real time and take decision depending on the real data

#prior commands to be run 
# fuser -v /dev/snd/* # check all mics connected
# fuser -k /dev/snd/* # disconnects all running mic
# pkill sox # kills sox

# The first three commands are a must run
# alternatives
# arecord -l # to list all audio
# using the deployment with another command
#  edge-impulse-linux-runner --audio-device <alternative-device> # pick one device listed in the arecord -l
#  e.g
# edge-impulse-linux-runner --audio-device hw:1,0

# # you can opt to restart the audio service
# sudo systemctl restart alsa
# sudo reboot
# # 


##################################################################
#WEARABLE IOT ....NJIU .....ANGIE........#####################

import subprocess

# Run the edge impulse command
command = 'edge-impulse-linux-runner'
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=True)

# Print the output in real-time
while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if 'calm' and 'stress' and 'classifyRes' in output:
        required_output =output.strip()
        print(required_output)

# Get the exit code of the process
exit_code = process.returncode
print(f"Command exited with code: {exit_code}")
