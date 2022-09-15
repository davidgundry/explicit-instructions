#
# This script performs the pre-registered analysis for "data/data.json". It saves graphs in "out/".
#
# The working directory must be the directory containing the python/data/out folders.
#
# Requires pandas, scipy, statsmodels, matplotlib, ptitprince. Get them using
#  `pip install pandas scipy statsmodels matplotlib ptitprince`

import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import ttest_1samp
from scipy.stats import mannwhitneyu
from statsmodels.graphics.gofplots import qqplot
import matplotlib
import matplotlib.pyplot as plt
from statistics import mean, stdev
from math import sqrt
from scipy.stats import pearsonr, spearmanr
from statsmodels.stats.weightstats import ttost_ind

import seaborn as sns
sns.set(style="ticks", font_scale=1.5)
import ptitprince as pt

from load_process_exp4 import load_data, process_data

def hypothesis_test_1(high, low):
    print("""Hypothesis 1:  With explicit instructions, a greater proportion of the data will be accurate
    A two-tailed Mann-Whitney U test will be used to test whether the distribution of Accuracy differs
    significantly between the with-intruction condition than the without-instruction condition. α = 0.05""")
    c0 = high['proportion_of_valid_data_last10_idealised']
    c1 = low['proportion_of_valid_data_last10_idealised']
    alpha = 0.05
    mwu = mannwhitneyu(c0, c1,alternative='two-sided')
    n0 = len(c0)
    n1 = len(c1)
    cond0 = (n0 - 1) * (stdev(c0) ** 2)
    cond1 = (n1 - 1) * (stdev(c1) ** 2)
    pooledSD = sqrt((cond0 + cond1) / (n0 + n1 - 2))
    cohens_d = (mean(c0) - mean(c1)) / pooledSD
    print("With-Instruction mean" ,mean(c0), "sd" ,stdev(c0))
    print("Without-Instruction mean" ,mean(c1), "sd", stdev(c1))
    print("Mann-Whitney U test: p =", mwu.pvalue, "; U =",mwu.statistic, "; significant =",(mwu.pvalue < alpha), "; d =",cohens_d, "\n\n")

def hypothesis_test_2(high, low):
    print("""Hypothesis 2:  With explicit instructions, participants will enjoy the game less
    A two-tailed two-sample t-test will be used to test whether the mean scores of Enjoyment
    are greater in the without-instruction condition than the with-instruction condition. α = 0.05""")
    alpha = 0.05
    c0 = high['imi_enjoyment']
    c1 = low['imi_enjoyment']
    ttest = ttest_ind(c0,c1)
    n0 = len(c0)
    n1 = len(c1)
    cond0 = (n0 - 1) * (stdev(c0) ** 2)
    cond1 = (n1 - 1) * (stdev(c1) ** 2)
    pooledSD = sqrt((cond0 + cond1) / (n0 + n1 - 2))
    cohens_d = (mean(c0) - mean(c1)) / pooledSD
    print("With-Instruction mean" ,mean(c0), "sd" ,stdev(c0))
    print("Without-Instruction mean" ,mean(c1), "sd", stdev(c1))
    print("two tailed t test: p =", ttest.pvalue, "; t =",ttest.statistic, "; significant =",(ttest.pvalue < alpha), "; d =",cohens_d, "\n\n")

def hypothesis_test_3(high, low):
    print("""Hypothesis 3:  With explicit instructions, participants will experience the game
    with an 'experiment' frame rather than a 'play' frame.
    A two-tailed two-sample t-test will be used to test whether the mean scores of Play Framing
    are greater in the without-instruction condition than the with-instruction condition. α = 0.05""")
    alpha = 0.05
    c0 = high['play_framing']
    c1 = low['play_framing']
    ttest = ttest_ind(c0,c1)
    n0 = len(c0)
    n1 = len(c1)
    cond0 = (n0 - 1) * (stdev(c0) ** 2)
    cond1 = (n1 - 1) * (stdev(c1) ** 2)
    pooledSD = sqrt((cond0 + cond1) / (n0 + n1 - 2))
    cohens_d = (mean(c0) - mean(c1)) / pooledSD
    print("With-Instruction mean" ,mean(c0), "sd" ,stdev(c0))
    print("Without-Instruction mean" ,mean(c1), "sd", stdev(c1))
    print("two tailed t test: p =", ttest.pvalue, "; t =",ttest.statistic, "; significant =",(ttest.pvalue < alpha), "; d =",cohens_d, "\n\n")

def enjoyment_box_plot(df):
    plt.clf()
    boxplot = df.boxplot(column='imi_enjoyment', by='version', grid=False)
    plt.suptitle('')
    plt.title("")
    boxplot.set_xlabel("")
    boxplot.set_ylabel("IMI Enjoyment subscale")
    plt.savefig('out/imi_enjoyment_per_condition+'+dataset+'.pdf', bbox_inches='tight')

def enjoyment_raincloud(df):
    dy="imi_enjoyment"; dx="version"; ort="v"; pal = sns.color_palette(n_colors=2)
    f, ax = plt.subplots(figsize=(7, 5))
    ax=pt.half_violinplot( x = dx, y = dy, data = df, palette = pal, bw = .2, cut = 0.,
                        scale = "area", width = .6, inner = None, orient = ort)
    ax=sns.stripplot( x = dx, y = dy, data = df, palette = pal, edgecolor = "white",
                    size = 3, jitter = 1, zorder = 0, orient = ort)
    ax=sns.boxplot( x = dx, y = dy, data = df, color = "black", width = .15, zorder = 10,\
                showcaps = True, boxprops = {'facecolor':'none', "zorder":10},\
                showfliers=True, whiskerprops = {'linewidth':2, "zorder":10},\
                saturation = 1, orient = ort)
    plt.xticks(plt.xticks()[0], ["With Instruction","Without Instruction"])

    ax.set_xlabel("")
    ax.set_ylabel("IMI Enjoyment")
    plt.savefig('out/imi_enjoyment_per_condition_raincloud+'+dataset+'.pdf', bbox_inches='tight')

def valid_proportion_all_data_idealised_boxplot(df):
    plt.clf()
    boxplot = df.boxplot(column='proportion_of_valid_data_last10_idealised', by='version', grid=False)
    plt.suptitle('')
    plt.title("")
    plt.xticks(plt.xticks()[0], ["With Instruction","Without Instruction"])
    boxplot.set_xlabel("")
    boxplot.set_ylabel("Proportion of Valid Data")
    plt.savefig('out/prop_valid_data_last10_idealised_per_condition+'+dataset+'.pdf', bbox_inches='tight')

def valid_proportion_all_data_idealised_raincloud(df):
    dy="proportion_of_valid_data_last10_idealised"; dx="version"; ort="v"; pal = sns.color_palette(n_colors=2)
    f, ax = plt.subplots(figsize=(7, 5))
    ax=pt.half_violinplot( x = dx, y = dy, data = df, palette = pal, bw = .2, cut = 0.,
                        scale = "area", width = .6, inner = None, orient = ort)
    ax=sns.stripplot( x = dx, y = dy, data = df, palette = pal, edgecolor = "white",
                    size = 3, jitter = 1, zorder = 0, orient = ort)
    ax=sns.boxplot( x = dx, y = dy, data = df, color = "black", width = .15, zorder = 10,\
                showcaps = True, boxprops = {'facecolor':'none', "zorder":10},\
                showfliers=True, whiskerprops = {'linewidth':2, "zorder":10},\
                saturation = 1, orient = ort)
    plt.xticks(plt.xticks()[0], ["With Instruction","Without Instruction"])
    ax.set_xlabel("")
    ax.set_ylabel("Proportion of Valid Data")
    plt.savefig('out/prop_valid_data_last10_idealised_per_condition_raincloud+'+dataset+'.pdf', bbox_inches='tight')


def play_framing_all_data_idealised_raincloud(df):
    dy="play_framing"; dx="version"; ort="v"; pal = sns.color_palette(n_colors=2)
    f, ax = plt.subplots(figsize=(7, 5))
    ax=pt.half_violinplot( x = dx, y = dy, data = df, palette = pal, bw = .2, cut = 0.,
                        scale = "area", width = .6, inner = None, orient = ort)
    ax=sns.stripplot( x = dx, y = dy, data = df, palette = pal, edgecolor = "white",
                    size = 3, jitter = 1, zorder = 0, orient = ort)
    ax=sns.boxplot( x = dx, y = dy, data = df, color = "black", width = .15, zorder = 10,\
                showcaps = True, boxprops = {'facecolor':'none', "zorder":10},\
                showfliers=True, whiskerprops = {'linewidth':2, "zorder":10},\
                saturation = 1, orient = ort)
    plt.xticks(plt.xticks()[0], ["With Instruction","Without Instruction"])
    ax.set_xlabel("")
    ax.set_ylabel("Play framing")
    plt.savefig('out/play_framing_per_condition_raincloud+'+dataset+'.pdf', bbox_inches='tight')


def time_per_input_boxplot(df):
    plt.clf()
    boxplot = df.boxplot(column='time_per_input_from_8min', by='version', grid=False)
    plt.suptitle('')
    plt.title("")
    boxplot.set_xlabel("")
    boxplot.set_ylabel("Time per input (from 8 min)")
    plt.savefig('out/time_per_input_per_condition+'+dataset+'.pdf', bbox_inches='tight')

def time_per_input_raincloud(df):
    dy="time_per_input_from_8min"; dx="version"; ort="v"; pal = sns.color_palette(n_colors=2)
    f, ax = plt.subplots(figsize=(7, 5))
    ax=pt.half_violinplot( x = dx, y = dy, data = df, palette = pal, bw = .2, cut = 0.,
                        scale = "area", width = .6, inner = None, orient = ort)
    ax=sns.stripplot( x = dx, y = dy, data = df, palette = pal, edgecolor = "white",
                    size = 3, jitter = 1, zorder = 0, orient = ort)
    ax=sns.boxplot( x = dx, y = dy, data = df, color = "black", width = .15, zorder = 10,\
                showcaps = True, boxprops = {'facecolor':'none', "zorder":10},\
                showfliers=True, whiskerprops = {'linewidth':2, "zorder":10},\
                saturation = 1, orient = ort)
    plt.xticks(plt.xticks()[0], ["Low Framing","High Framing"])
    ax.set_xlabel("")
    ax.set_ylabel("Time per input (from 8 min)")
    plt.savefig('out/time_per_input_per_condition_raincloud+'+dataset+'.pdf', bbox_inches='tight')


def gaming_frequency_bar_plot(df):
    plt.clf()
    boxplot = df['gaming_frequency'].value_counts().plot.bar(grid=False)
    plt.suptitle('')
    plt.title("")
    #boxplot.set_xlabel("Gaming Frequency")
    boxplot.set_ylabel("Count")
    plt.savefig('out/gaming_frequency+'+dataset+'.pdf', bbox_inches='tight')

def correlation(df):
    print("\nExploratory: Correlation between play framing and accuracy")
    print("(Correlation, p)")
    print("Pearson's r", pearsonr(df['play_framing'], df['proportion_of_valid_data_last10_idealised']))
    print("Spearman's rho", spearmanr(df['play_framing'], df['proportion_of_valid_data_last10_idealised']))
    print("Degrees of freedom", len(df['play_framing']) - 2)

    plt.clf()
    plt.suptitle('')
    plt.title("")
    plt.scatter(df['play_framing'], df['proportion_of_valid_data_last10_idealised'])
    plt.xlabel("Play Framing")
    plt.ylabel("Proportion of Valid Data")
    plt.savefig('out/scatter-play-framing-accuracy+'+dataset+'.pdf', bbox_inches='tight')

    print("\nExploratory: Correlation between play framing and enjoyment")
    print("Pearson's r", pearsonr(df['play_framing'], df['imi_enjoyment'])) 
    print("Spearman's rho", spearmanr(df['play_framing'], df['imi_enjoyment']))
    print("Degrees of freedom", len(df['play_framing']) - 2)

    print("\nExploratory: Correlation between enjoyment and accuracy")
    print("Pearson's r", pearsonr(df['imi_enjoyment'], df['proportion_of_valid_data_last10_idealised'])) 
    print("Spearman's rho", spearmanr(df['imi_enjoyment'], df['proportion_of_valid_data_last10_idealised']))
    print("Degrees of freedom", len(df['imi_enjoyment']) - 2)

def correlationEnjoyment(df):
    plt.clf()
    plt.suptitle('')
    plt.title("")
    plt.scatter(df['play_framing'], df['imi_enjoyment'])
    plt.xlabel("Play Framing")
    plt.ylabel("Enjoyment")
    plt.savefig('out/scatter-play-framing-enjoyment+'+dataset+'.pdf', bbox_inches='tight')


def tost(high, low):
    print("\nExploratory: TOST test")
    s1 = high['proportion_of_valid_data_last10_idealised']
    s2 = low['proportion_of_valid_data_last10_idealised']
    p1 = ttest_ind(s1, s2)
    p2 = ttost_ind(s1, s2, -0.125, 0.125, usevar='unequal')
    print('diff in means:', s2.mean() - s1.mean())
    print('ttest:', p1)
    print('   tost:', p2)

minimum_moves = 10
dataset = 'data'
print("Analysing dataset", dataset, "\n")
rawData = load_data("data/"+dataset)
df = process_data(rawData)
df = df[df['total_moves']>=minimum_moves]
df = df[df['bug'] == "nobug"]

highFramingCondition = df[df['version']=='HighFraming']
lowFramingCondition = df[df['version']=='LowFraming']

hypothesis_test_1(highFramingCondition, lowFramingCondition)
hypothesis_test_2(highFramingCondition, lowFramingCondition)
hypothesis_test_3(highFramingCondition, lowFramingCondition)
enjoyment_box_plot(df)
enjoyment_raincloud(df)
valid_proportion_all_data_idealised_boxplot(df)
valid_proportion_all_data_idealised_raincloud(df)
play_framing_all_data_idealised_raincloud(df)
time_per_input_boxplot(df)
time_per_input_raincloud(df)
gaming_frequency_bar_plot(df)
print(df['gaming_frequency'].value_counts())
correlation(df)
correlationEnjoyment(df)
tost(highFramingCondition, lowFramingCondition)