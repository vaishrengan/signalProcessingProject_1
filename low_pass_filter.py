import numpy as np 
import matplotlib.pyplot as plt 
from scipy import signal
from numpy.fft import fft,ifft,fftfreq

N = 1000
Lx = 100
t = np.linspace(0,Lx,N)
omg = 2*np.pi/Lx

plt.subplot(311)
y = 75*np.sin(omg*250*t) + 100*np.sin(omg*5*t) + 15*np.cos(omg*10*t) 
plt.plot(t,y)

freqs = fftfreq(N)
mask = freqs > 0
fft_vals = np.asarray(fft(y))  #this will contain mirror images of the fourier transform 
actual_fft = 2.0*np.abs(fft_vals/N)  #plots only half the values of the fft since the other half is not needed
FFT = actual_fft

plt.subplot(312)
plt.plot(fft_vals)

plt.subplot(313)
plt.plot(ifft(fft_vals))  #ifft requires a mirror image input to work, it won't work on corrected input as in actual_fft, but only on fft_vals

print(ifft(fft_vals))

f = np.arange(0,1000)

def step(f):
    low_filter = np.zeros(len(f))
    ind = np.where((f<50))
    ind2 = np.where((f>950))
    low_filter[ind] = 1
    low_filter[ind2]= 1

    return low_filter #the actual filter is from 0 to 50, and the rest is 0; the domain exists only until 500

low_filter = step(f)
plt.figure(2)
plt.subplot(311)
plt.plot(f,step(f))

applied_filter = fft_vals * low_filter
plt.subplot(312)
plt.plot(f,applied_filter)

plt.subplot(313)
plt.plot(ifft(applied_filter))

print(ifft(applied_filter))
plt.show()
