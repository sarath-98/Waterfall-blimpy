#import  the necessary libraries and Packages.
%matplotlib inline
import numpy as np
import pylab as plt
from blimpy import Waterfall

#Download the file from the Github repository.
file_path = 'Voyager1.single_coarse.fine_res.h5'
#Define the path of the downloaded file.

eobs = Waterfall(file_path)
 #Use obs.info() to get information about the downloaded file if needed.
 #printing obs.header() and obs.shape() gives you the header of the file and its shape.
 obs.plot_spectrum(logged=True)
obs.plot_spectrum(f_start=8419.2740, f_stop=8419.2750)
#f_start and f_stop can be used to give limit for the spectrum to be plotted.
plt.figure(figsize=(8, 6)) #define the siz of the plot
plt.subplot(3,1,1)
obs.plot_spectrum(f_start=8419.2740, f_stop=8419.2750)

obs.plot_waterfall(f_start=8419.274, f_stop=8419.275)
T#This gives the waterfal spectrum of the chosen area.
