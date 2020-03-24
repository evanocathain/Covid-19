#!/usr/bin/python
# Thanks XKCD for being awesome! 
# Credit to this page: https://matplotlib.org/xkcd/examples/showcase/xkcd.html
#
# Wash your hands
# @evanocathain

from matplotlib import pyplot as plt
import numpy as np

plt.xkcd()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
ax.set_ylim([-10,120])
ax.set_xlim([-10,120])

# Zoom is going up
zoom = np.arange(100)
# Everything else is going down
fifties = 100.0 - np.arange(100)

# Do a couple of arrows
plt.annotate(
    'Zoom Stock Value',
    xy=(95,95), arrowprops=dict(arrowstyle='->'), xytext=(40, 90))
plt.annotate(
    'Perceived Value of', xy=(30,10), xytext=(30, 10))
plt.annotate(
    '1950s Work Practices',
    xy=(90,10), arrowprops=dict(arrowstyle='->'), xytext=(30, 0))

plt.plot(zoom)
plt.plot(fifties)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title("COVID-19 TRENDS - MARCH 2020")

plt.show()
