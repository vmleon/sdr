import numpy as np
import matplotlib.pyplot as plt

Fs = 1 # Hz
N = 100 # Number of points to simulate, and out FFT size

t = np.arange(N)
s = np.sin(0.15 * 2 * np.pi * t)

fig, axs = plt.subplots(3,1, layout='constrained')
axs[0].plot(t, s)
axs[0].set_xlabel('n')
axs[0].set_ylabel('Signal Amplitude')
# axs[0].set_xlim(-10, 120)
axs[0].grid(True)


s = s * np.hamming(N)
S = np.fft.fftshift(np.fft.fft(s))

f = np.arange(Fs/-2, Fs/2, Fs/N)

S_mag = np.abs(S)
axs[1].plot(f, S_mag, '.-')
axs[1].set_xlabel('Hz')
axs[1].set_ylabel('FTT of Signal (Magniture)')

S_phase = np.angle(S)
axs[2].plot(f, S_phase, '.-')
axs[2].set_xlabel('Hz')
axs[2].set_ylabel('FTT of Signal (Phase)')

plt.show()