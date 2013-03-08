import alsaaudio, wave, numpy
import sys

print sys.argv
sound_files_folder = "data"
delimiter = "/"
file_suffix = ".wav"
file_name = raw_input("What is the word?\n")
file_name = file_name
full_file_name = sound_files_folder + delimiter + file_name + file_suffix
#file_name = sys.argv[1]


inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
inp.setchannels(1)
inp.setrate(44100)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(1024)

w = wave.open(file_name, 'w')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)

while True:
    l, data = inp.read()
    a = numpy.fromstring(data, dtype='int16')
    print numpy.abs(a).mean()
    w.writeframes(data)

