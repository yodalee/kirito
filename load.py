import glob
import numpy as np

# Load Trace
TraceNum = 0
T = {}
for i in sorted(glob.glob("trace/*.txt")):
	T[TraceNum] = np.loadtxt(i)
	TraceNum = TraceNum + 1
TraceLen = len(T[0])

# Load Plaintext and Ciphertext
P = {}
C = {}
with open("trace/log/log1.txt", "r") as log:
	for i in range (TraceNum):
		P[i] = log.readline().rstrip('\n').rstrip('\r')[-32:]
		C[i] = log.readline().rstrip('\n').rstrip('\r')[-32:]

# Save Trace
Trace = np.array([[0 for i in range (TraceLen)] for j in range (TraceNum)], np.dtype('i2'))
for i in range (TraceNum):
	Trace[i] = T[i]
np.save("trace.npy", Trace)

# Save Plaintext and Ciphertext
Plain = np.array([[0 for i in range (16)] for j in range (TraceNum)], np.dtype('u1'))
Cipher = np.array([[0 for i in range (16)] for j in range (TraceNum)], np.dtype('u1'))
for i in range (TraceNum):
	for j in range (16):
		Plain[i][j] = int(P[i][2*j:2*j+2], base=16)
		Cipher[i][j] = int(C[i][2*j:2*j+2], base=16)
np.save("plain.npy", Plain)
np.save("cipher.npy", Cipher)
