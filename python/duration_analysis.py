#
# This script generates the analysis for "data/duration.csv". It saves
# output data and graphs in "out/".
#

#
# Note: The duration in `/data/duration.csv` include time spent in the tutorial.
#

import numpy as np
import pandas as pd
import json
from scipy.stats import ttest_ind
from scipy.stats import ttest_1samp
import matplotlib
import matplotlib.pyplot as plt
from statistics import mean, stdev
from math import sqrt

def duration_histogram(high, low):
    plt.clf()
    bins = np.linspace(500, 1200, 24)
    plt.hist(high['duration'], bins, alpha=0.5, label="High Framing")
    plt.hist(low['duration'], bins, alpha=0.5, label="Low Framing")
    plt.suptitle('')
    plt.title("")
    plt.legend(loc='upper right')
    plt.savefig('out/duration_hist+'+dataset+'.pdf', bbox_inches='tight')

def duration_boxplot(df):
    plt.clf()
    boxplot = df.boxplot(column='duration', by='version', grid=False)
    plt.suptitle('')
    plt.title("")
    boxplot.set_xlabel("")
    boxplot.set_ylabel("Duration")
    plt.savefig('out/duration_per_condition+'+dataset+'.pdf', bbox_inches='tight')


dataset = 'duration'
print("Analysing dataset", dataset, "\n")
df=  pd.read_csv("data/"+dataset+".csv", names=["version","duration"])

high = df[df['version']=='HighFraming']
low = df[df['version']=='LowFraming']

duration_histogram(high,low)
duration_boxplot(df)

c0 = high['duration']
c1 = low['duration']

print("High Framing condition: mean", mean(c0), "sd", stdev(c0), "Min", min(c0), "Max", max(c0))
print("Low Frmaing condition: mean", mean(c1), "sd", stdev(c1), "Min", min(c1), "Max", max(c1))

