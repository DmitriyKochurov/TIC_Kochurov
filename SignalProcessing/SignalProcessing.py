import numpy
import scipy
from scipy import signal
from scipy import signal, fft
import matplotlib.pyplot as plt
n = 500
Fs = 1000
F_max = 21

generation = numpy.random.normal(0, 10, n)

time_check = numpy.arange(n)/Fs

w = F_max/(Fs/2)
parametr = scipy.signal.butter(3, w, 'low', output='sos')
filtered_signal = scipy.signal.sosfiltfilt(parametr, generation)

fig, ax = plt.subplots(figsize=(21/2.54, 14/2.54))
ax.plot(time_check, filtered_signal, linewidth=1)
ax.set_xlabel('«текст»', fontsize=14)
ax.set_ylabel('«текст»', fontsize=14)
plt.title('«текст»', fontsize=14)

fig.savefig("./SignalProcessing/title.png", dpi = 600)

spectrum = scipy.fft.fft(filtered_signal)

mod = numpy.abs(scipy.fft.fftshift(spectrum))
print("Mодульне значення:" + str(mod))

checks = scipy.fft.fftfreq(n, 1/n)

fftshift = scipy.fft.fftshift(checks)

print("Процедура fftshift" + str(fftshift))


ax.plot(checks, spectrum, linewidth=1)
ax.set_xlabel('«текст»', fontsize=14)
ax.set_ylabel('«текст»', fontsize=14)
plt.title('«текст»', fontsize=14)

fig.savefig("./SignalProcessing/title2.png", dpi = 600)


