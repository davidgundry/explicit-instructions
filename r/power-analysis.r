
library("pwr")
# These calculations are to determine the required sample size for the Explicit Instructions study to
# compare Adjective Game with and without explicit instructions to give grammatical data.
#
# Two hypotheses will be tested, each independent of the other and with an alpha of 0.05.  The first is that
# players will provide lower accuracy data in the without-instructions condition. The second is that the players will
# report higher enjoyment in the without-instructions condition.

# Hypothesis 1 (based on previous experiments)
# A two-tailed Mann-Whitney U test will be used to test whether the distribution of Accuracy
# differs significantly between the high-framing condition than the low framing condition. α = 0.05
alt <- "two.sided"
observedEffectSize <- 1.0005893861300805 # From exploratory analysis of the "Enjoyment and data
                                         # quality in a game for human-subject data collection"
                                         # experiments. We found this decrease in accuracy between
                                         # experiment 1 and experiment 2 in the control condition. One
                                         # main change was whether explicit instuctions for
                                         # grammaticality were given
pwr.t.test(d = observedEffectSize, sig.level = 0.05, power = 0.8, alternative = alt)


# Hypothesis 1 (effect size of interest)
effectSizeOfInterest <- cohen.ES(test = "t", size = "medium")$effect.size
                                         # Because the previous experiment is not directly comparable
                                         # and other factors may have significantly contributed (such as
                                         # history effects), we should still check for medium sized effects.
                                         # This assumes about half of the previously observed effect
                                         # was to do with framing(/instructions)
pwr.t.test(d = effectSizeOfInterest, sig.level = 0.05, power = 0.8, alternative = alt)

# Hypothesis 2
# A two-tailed two-sample t-test will be used to test whether the mean scores of Enjoyment
# are greater in the low-framing condition than the high-framing condition. α = 0.05.

observedEffectEnjoyment <- 0.13
# Our previous experiment suggests this effect might be small, if it exists - smaller than
# is of interest. As we can achieve medium-to-large and greater effects on enjoyment through
# the game design, anything less than a medium effect is not of enough importance to warrent
# spending a lot more money to detect it.


# Hypothesis 3
observedEffectPlayFraming <- -0.23
# Our previous experiment suggest the effect might be small. We can't afford to look for effects
# this small, so we will be cautious in interpreting null results for this hypothesis test. However,
# if it is not also having effects on enjoyment, it is probably smaller than is of interest.


# Largest sample size is is 63.76561 per group. These sample sizes are based on t-tests, which can be less efficient
# than Wilcoxon signed rank tests. The Asymptotic Relative Efficiency (ARE) of a Wilcoxon test relative to a t-test
# has a lower bound of 0.864, meaning that at worst we require 1/0.864 = 1.1574 times the sample size of a t test (Riffenburgh, 2012).
sampleSize <- 63.76561/0.864
sampleSize

# Which we will round to 74. This makes the sample size in both groups 148.
# However, we expect a number of exclusions. Our previous exclusion rate was high ~1/3.
# This time we have significantly decreased the required number of moves from 16 to 10.
# This should significantly reduce our exclusion rate.
# If we add 20 to our sample to increase to 168 participants, that gives us room for an exclusion
# rate of just under 0.12. Including this in the original sample size means we don't need a complicated stopping rule.

# Final sample size: 168


# References

# R.H. Riffenburgh, 2012. Chapter 18 - Sample Size Estimation and Meta-Analysis, in: Statistics in Medicine (Third Edition),
# Editor(s): R.H. Riffenburgh, Academic Press, pp. 365-391, [Relevant section available at:
# https://www.sciencedirect.com/topics/mathematics/asymptotic-relative-efficiency]
