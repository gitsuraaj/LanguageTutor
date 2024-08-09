import sounddevice as sd
import numpy as np
import wave

# Parameters
duration = 10  # seconds
sample_rate = 44100  # Sample rate in Hz

# Record audio
print("Recording...")
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
sd.wait()  # Wait until the recording is finished
print("Recording complete")

# Save as WAV file
output_file = "output.wav"
with wave.open(output_file, 'w') as wf:
    wf.setnchannels(2)  # Stereo
    wf.setsampwidth(2)  # Sample width in bytes
    wf.setframerate(sample_rate)
    wf.writeframes(audio_data.tobytes())

print(f"Audio saved to {output_file}")
