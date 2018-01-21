import numpy as np
from utils import Utils

T = np.load("trace_cpp.npy")
P = np.load("plain.npy")
C = np.load("cipher.npy")
K = np.arange(16)
K10 = np.array([0x13, 0x11, 0x1d, 0x7f, 0xe3, 0x94, 0x4a, 0x17, 0xf3, 0x07, 0xa7, 0x8b, 0x4d, 0x2b, 0x30, 0xc5])
TraceNum = len(T)
TraceLen = len(T[0])

MC = [0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12, 1, 6, 11]

AveTrace = np.average(T, axis=0)
VarTrace = np.var(T, axis=0)

Left = 1660
Right = 1670

def main():
    utils = Utils()

    for byte in range (16):
        MaxValue = np.zeros(256, dtype=np.float64)
        for i in range (256):
            X = np.zeros(TraceNum, np.float64)
            Y = np.zeros(TraceNum, np.int)
            CorrTrace = np.zeros(TraceLen, np.float64)
            for j in range (TraceNum):
                Y[j] = utils.HW(C[j][MC[byte]] ^ (utils.ISB[C[j][byte] ^ i]))
            for j in range (Left, Right):
                X = T[0:TraceNum, j]
                CorrTrace[j] = abs(utils.npCalCorr(X,Y))
            MaxValue[i] = max(CorrTrace[Left:Right])
        ansbyte = np.argmax(MaxValue)

        if ansbyte == K10[byte]:
            s = "(O)"
        else:
            s = "(X)"
        print("Byte {} = {} with correlation {:.4f} {}".format(
                hex(byte)[2:], hex(ansbyte).rstrip('L')[2:].zfill(2), max(MaxValue), s))

if __name__ == "__main__":
    main()
