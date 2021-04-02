"""
Module for visualization and plotting.

TODO.

Implement this module in any way you are comfortable with. You are free to use\
any visualization library you like. Providing live plotting and animations is\
also a bonus. The visualizations you will definitely need are as follows:

1. F-I curve.
2. Voltage/current dynamic through time.
3. Raster plot of spikes in a neural population.
4. Convolutional weight demonstration.
5. Weight change through time.
"""
import matplotlib.pyplot as plt


def plot_result(it, ut, threshold) -> None:
    plt.figure(figsize=(20,10))
    plt.subplot(121)
    plt.plot(it)
    plt.ylabel('I(t)')
    plt.grid(True)

    plt.subplot(122)
    plt.plot(ut)
    plt.hlines(threshold, 0, len(ut), colors="red")
    plt.ylabel('U(t)')
    plt.xlabel('time')
    plt.grid(True)

    plt.show()

    return