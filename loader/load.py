import glob
import numpy as np

# Preload trace to get TraceLen
filelist = sorted(glob.glob("trace/trace*.txt"))
TraceNum = len(filelist)
TraceLen = len(np.loadtxt(filelist[0]))

# Load/Save Trace
Trace = np.zeros((TraceNum, TraceLen), np.dtype('i2'))
for i, f in enumerate(filelist):
    Trace[i] = np.genfromtxt(f,np.dtype('i2'))
np.save("trace.npy", Trace)

# Load Plaintext and Ciphertext
P = {}
C = {}
with open("trace/log/log1.txt", "r") as log:
	for i in range (TraceNum):
		P[i] = log.readline().rstrip()[-32:]
		C[i] = log.readline().rstrip()[-32:]

# Save Plaintext and Ciphertext
Plain = np.array([[0 for i in range (16)] for j in range (TraceNum)], np.dtype('u1'))
Cipher = np.array([[0 for i in range (16)] for j in range (TraceNum)], np.dtype('u1'))
for i in range (TraceNum):
	for j in range (16):
		Plain[i][j] = int(P[i][2*j:2*j+2], base=16)
		Cipher[i][j] = int(C[i][2*j:2*j+2], base=16)
np.save("plain.npy", Plain)
np.save("cipher.npy", Cipher)
