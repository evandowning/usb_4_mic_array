import argparse
import pyaudio
import wave
import numpy as np
 
def record(channel,outFN):
    RESPEAKER_RATE = 16000
    RESPEAKER_CHANNELS = 6 # change base on firmwares, 1_channel_firmware.bin as 1 or 6_channels_firmware.bin as 6
    RESPEAKER_CHANNELS = 1 # change base on firmwares, 1_channel_firmware.bin as 1 or 6_channels_firmware.bin as 6
    RESPEAKER_WIDTH = 2
    RESPEAKER_INDEX = 2  # refer to input device id from executing "get_index.py"
    CHUNK = 1024
    RECORD_SECONDS = 5
    RECORD_SECONDS = 10

    p = pyaudio.PyAudio()

    stream = p.open(
                rate=RESPEAKER_RATE,
                format=p.get_format_from_width(RESPEAKER_WIDTH),
                channels=RESPEAKER_CHANNELS,
                input=True,
                input_device_index=RESPEAKER_INDEX,)

    print("* recording")

    frames = []

    for i in range(0, int(RESPEAKER_RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        # if you want to extract channel X, please change to [X::6]
        a = np.fromstring(data,dtype=np.int16)[channel::6]
        frames.append(a.tostring())

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(outFN, 'wb')
    wf.setnchannels(RESPEAKER_CHANNELS)
    wf.setsampwidth(p.get_sample_size(p.get_format_from_width(RESPEAKER_WIDTH)))
    wf.setframerate(RESPEAKER_RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def _main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--channel', type=int, help='channel', required=True)
    parser.add_argument('--output', help='output wav filename', required=True)

    args = parser.parse_args()

    # Store arguments
    channel = int(args.channel)
    outFN = args.output

    # Record audio
    record(channel,outFN)

if __name__ == '__main__':
    _main()
