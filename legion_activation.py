import pvporcupine
import pyaudio
import struct

def wait_for_wake_word():
    porcupine = pvporcupine.create(
        access_key="FfPuSHaG7sc44I5LNly9Ls2EXIIY2rTxIXhJK3Nz0z7qG7Nh0+cGHw==",
        keyword_paths=[r"C:\Users\Nam\Desktop\Legion 1.0\Legion-Five_en_windows_v3_0_0.ppn"]
    )

    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("Listening for 'Legion Five'...")

    try:
        while True:
            audio = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, audio)

            result = porcupine.process(pcm)
            if result >= 0:
                print("Wake word detected!")
                break

    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()

# wait_for_wake_word()
