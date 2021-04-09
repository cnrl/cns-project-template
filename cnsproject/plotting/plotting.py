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
import numpy as np


class plotting():

    def reset(self):
        self.figure = plt.figure(figsize=(10,5))
        self.colors = plt.rcParams["axes.prop_cycle"]()
        self.counter = 0


    def show(self):
        self.figure.legend()
        plt.show()
        return


    def plot_ut_it_init(self, time) -> None:
        self.reset()
        self.ax1 = self.figure.add_subplot(121)
        self.ax1.set_ylabel('I(t)')
        self.ax1.set_xlabel('time')
        self.ax1.set_title("Current per second")
        self.ax1.grid(True)
        self.ax1.set_xticks(np.arange(time+1, dtype=int)*100)
        self.ax1.set_xticklabels(np.arange(time+1, dtype=int))
        
        self.ax2 = self.figure.add_subplot(122)
        self.ax2.set_ylabel('U(t)')
        self.ax2.set_xlabel('time')
        self.ax2.set_title("Potential per second")
        self.ax2.grid(True)
        self.ax2.set_xticks(np.arange(time+1, dtype=int)*100)
        self.ax2.set_xticklabels(np.arange(time+1, dtype=int))
        return


    def plot_ut_it_update(self, it, ut, threshold, spikes) -> None:
        c = next(self.colors)["color"]
        self.ax1.plot(it, label = "I & U "+str(self.counter), color=c)
        self.ax2.plot(ut, color=c)
        c = next(self.colors)["color"]
        self.ax2.hlines(threshold, 0, len(ut), label = "threshold "+str(self.counter), colors = c)
        c = next(self.colors)["color"]
        self.ax2.scatter(spikes, [threshold]*len(spikes), label = "spikes "+str(self.counter), color = c)
        self.counter += 1
        return


    def plot_fi_init(self) -> None:
        self.reset()
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel('I(t)')
        self.ax.set_ylabel('f=1/T')
        self.ax.set_title("Frequency per current")
        self.ax.grid(True)
        return


    def plot_fi_update(self, spikes) -> None:
        self.ax.plot(spikes, color = "blue")
        plt.pause(0.005)
        self.figure.canvas.draw()
        return
