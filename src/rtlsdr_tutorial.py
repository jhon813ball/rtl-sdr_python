"""
Python Script to capture RF signal wave using RTL-SDR
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import rtlsdr

def main():
    # Constructor
    sdr = rtlsdr.RtlSdr(device_index=0)
    # Parameters
    sdr.sampling_rate = 20.48*10**6
    sdr.center_freq = 400*10**6
    sdr.set_agc_mode(True)
    sdr.gain = 50
    # Capture signal wave
    observationTime = 10**(-3)
    nSamples = observationTime*sdr.sampling_rate
    signalWave = sdr.read_samples(nSamples)
    # Plot
    plt.figure()
    plt.plot(signalWave.real)
    plt.title("Capture Signal Wave using RTL-SDR (Real)", fontsize=14)
    plt.xlabel("Index", fontsize=14)
    plt.ylabel("Amplitude", fontsize=14)
    plt.tick_params(labelsize=14)
    plt.tight_layout()

    plt.figure()
    plt.plot(signalWave.imag)
    plt.title("Capture Signal Wave using RTL-SDR (Imaginary)", fontsize=14)
    plt.xlabel("Index", fontsize=14)
    plt.ylabel("Amplitude", fontsize=14)
    plt.tick_params(labelsize=14)
    plt.tight_layout()

    plt.show()
    # Destructor
    del sdr


if __name__ == '__main__':
    main()
    sys.exit(0)




