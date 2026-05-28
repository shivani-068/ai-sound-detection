import sounddevice as sd
import numpy as np

duration = 3
sample_rate = 44100

print("AI Sound Detection Started")
print("Recording...")

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1
)

sd.wait()

print("Recording Completed")

volume = np.linalg.norm(audio)

print("Sound Level:", volume)

if volume > 30:
    print("Loud Sound Detected!")

else:
    print("Quiet Sound Detected")
