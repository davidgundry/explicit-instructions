# Effect of Explicit Instructions on Game Data

## Description

Investigating whether telling players of an applied game to give accurate data affects data quality, enjoyment, and percieved play framing. Previous work has manipulated the out-of-game framing of the game task to present it either as more experiment-like or more game-like. This did not have an effect on data quality, enjoyment, or play framing. So now we check whether giving a direct instruction has an effect.

This study will let participants play a game in one of two conditions. Either they are told to answer grammatically, or they are told to play however they like. We will analyse the results to determine whether there is an effect of explicit instructions on the accuracy (grammaticality) of the data collected and the enjoyment and play framing. The manipulation will be limited to the text content of the instruction presented to participants immediately before the task begins.

Study Information
-----------

## Hypotheses

1. With explicit instructions, a greater proportion of the data will be accurate
2. With explicit instructions, participants will enjoy the game less
3. With explicit instructions, participants will experience the game with an 'experiment' frame rather than a 'play' frame.

Design Plan
-----------

### Study type

Experiment - A researcher randomly assigns treatments to study subjects, this includes field or lab experiments. This is also known as an intervention experiment and includes randomized controlled trials.

### Blinding

* For studies that involve human subjects, they will not know the treatment group to which they have been assigned.
* Personnel who interact directly with the study subjects (either human or non-human subjects) will not be aware of the assigned treatments. (Commonly known as “double blind”)

### Is there any additional blinding in this study?

Participants will be assigned automatically by the game.

### Study design

Between-participant design with two groups.

### Randomization

Simple randomisation.

Sampling Plan
-------------

### Existing Data

Registration prior to creation of data

### Data collection procedures

Participants will be recruited from Prolific with a study description as in `description.md`. The following filters will apply on Prolific:

1. Age >= 18
2. First language English
3. Have not participated in any of my previous studies

Participants will be paid £1.00 for a 10 minute task. 

### Sample Size

168 participants

### Sample Size Rationale

See the file `power-analysis.Rout`.

Variables
---------

### Manipulated Variable

We will manipulate the information and instructions given to participants at the start of the experiment. There were two conditions:

**With Intruction**: In the with-instruction condition, participants will be given the following instruction before playing the game: "While you are playing this game, enter words in the order that feels most grammatically correct to you."

**Without Instruction**: In the without-instruction condition, participants will be given the following instruction before playing the game: "Play this game however you like."

### Measured Variables

**Accuracy**: Accuracy will be measured as the proportion of data collected that corresponds to standard English word order. It will be calculated for each player from the last 16 inputs made by the player.

**Enjoyment**: Enjoyment will be measured using the Intrinsic Motivation Inventory: Enjoyment Subscale. (Deci and Ryan, n.d.)

**Play Framing** Play Framing will be measured with adapted versions of the "Direct Play" questions of the Play Experience Scale (Pavlas et al. 2012):

1. When I was using the app, it felt like I was playing rather than doing an experiment
2. I would characterize my experience with the app as playing
3. I was playing a game rather than doing an experiment
4. (R) Using the app felt like doing an experiment 

Analysis Plan
-------------

### Statistical Models

**Hypothesis 1**: A two-tailed Mann-Whitney U test will be used to test whether the distribution of Accuracy differs significantly between the high-framing condition than the low-framing condition. α = 0.05

**Hypothesis 2**: A two-tailed two-sample t-test will be used to test whether the mean scores of Enjoyment are greater in the low-framing condition than the high-framing condition. α = 0.05

**Hypothesis 3**: A two-tailed two-sample t-test will be used to test whether the mean scores of Play Framing are greater in the low-framing condition than the high-framing condition. α = 0.05

### Data Exclusion

The following will be excluded:

1. Participants reporting their age as under 18
2. Participants reporting their first langauge as other than English.
3. Participants with fewer than 16 moves
4. Participants reporting a bug

### Missing Data

Incomplete records will be excluded from hypothesis tests

References
----------

Deci, E. L., and Ryan, R. M. (n.d.). Intrinsic Motivation Inventory. Available at: https://selfdeterminationtheory.org/questionnaires/

Pavlas D, Jentsch F, Salas E, Fiore SM, Sims V. The Play Experience Scale: Development and Validation of a Measure of Play. Human Factors. 2012;54(2):214-225. doi:10.1177/0018720811434513
