# Explicit Instructions (Effect of Experiment Framing on Game Data)

This is a repository of materials and data for the explicit instructions experiment in the Effect of Experiment Framing on Game Data study. 

## Directory Structure

* `data/` - processed/anonymised data
* `out/` - output of analysis scripts including data and graphs. Logs of script console output is saved here too
* `python/` - python scripts
* `r/` - r scripts
* `design/` - ethics, preregistration documents, etc.
* `final/` - versions of documents that have been officially submitted somewhere
* `materials/` - contains materials that were used in the experiment
* `img/` - screenshots of the game
* `raw/` - raw data stored here before processing and anonymisation

## Pre-Registration

Pre-registration documents are found in `design/`. The power analysis script used in the pre-registration can be found in `r/`, which generated `out/power-anaysis.Rout`. You can generate this using the following command:

    R CMD BATCH --quiet r/power-analysis.r out/power-analysis.Rout

## Why 10 inputs?

We want to reduce our exclusion rate from previous experiments. This will bring the exclusion rate for too few inputs to 0.07.

## Data collection

Data collection started 28 June 2021 10:47 Completed at 13:10. 193 began the study, 24 returned their submission, 1 timed out, leaving 168 who completed on Prolific.

164 records were retrieved from database. Of these 12 reported langauges other than English, leaving a dataset of 152 records.

Reward per hour: £5.84

One record had missing data. This is in `record-with-missing-data.json`.

Raw data deleted on 29 June 2021 at 10:54.

## Data Source

Data downloaded from [Restdb.io](https://restdb.io) using the script [get-restdb-data](https://github.com/davidgundry/get-restdb-data).

### Pre-anonymised Data Format

Data will be collected using the non-relational database service [restdb.io](https://restdb.io). All data will be downloaded as a json file.

The expected data format is in `raw/debug-example.json`, it looks like this (IDs are random):

    [ 
        {"_id":"5f118222b0e1d1570001ce11","data":{"gameVersion":"HighFraming","loadTime":1594982440874,"uploadTime":1594982944815,"duration":485.424,"playDuration":480.002,"consent":[true,true,true],"answers":["6","6","6","6","1","2","2","2","2","2","2","nobug","","27","female","english","every-day"],"moves":[["circle","square","triangle"],["filled","empty","green"],["red","green","blue"],["big","empty","circle"],["small","empty","triangle"],["small","empty","triangle"],["filled","empty","green"],["red","green","blue"],["big","triangle","empty"],["small","empty","triangle"],["small","empty","circle"],["red","green","blue"],["empty","filled","green"],["empty","filled","green"],["green","red","blue"]],"moveDurations":[1.5314450000005309,1.915494999999486,1.7831050000004325,5.033134999999675,4.784264999998413,7.050825000000259,1.1063899999990099,2.8494300000002113,9.9504450000004,3.452929999999469,11.851834999999483,79.11336499999923,2.4985599999999977,34.44956000000093,3.0330149999990828]},"version":"3.1.0.explicit-framing-3.0.0.HighFraming","studyID":"daa2e38ef9864764b95f4e545","prolificPID":"6440a9870c404843a195ba4a","sessionID":"501517b49a904139b1508183","uid":176}
    ]

* **_id**: Database record ID
* **data**: Participant data recorded from game (a JSON object)
    * **gameVersion**: `HighFraming` (=With instruction) or `LowFraming` (=Without instruction)
    * **loadTime**: a timestamp at the point the game loads (uses JavaScript `Date.now()`)
    * **uploadTime**: a timestamp at the point the game begins uploading data to the server, which is immediately upon the final questionnaire being submitted (uses JavaScript `Date.now()`)
    * **duration**: seconds between submission of pre-test questionnaire (and start of **tutorial**), and play-end interrupt before post-test questionnaire
* **version**: Game version and condition data was collected from
* **studyID, prolificPID, sessionID**: Values from the Prolific service for particiant payment purposes.
* **uid**: Auto-incrementing datanbase record UID.

For other variables, see the 'Data Format' section below.

### Anonymising Data

To prepare (i.e. anonymise) the raw data run the following command from the project directory. 

    python python/prepare-data_exp4.py

Edit that file to set the source data filename to match the one as downloaded.

The script will write files to disk in the folder "data". It will also write many files to disk in the same directory as the source (raw) data file. Many of these are for sanity checking purposes and should be deleted as they are not fully anonymised. The important files are:

* `data.json` (containing the main data)
* `duration.csv` (associating duration and condition)
* `age-gender.csv` (associating age and gender)

**Note:** The script shuffles the lines of the data file and it doesn't do any JSON parsing, so it is almost certain that the end-of-line commas will be incorrect. This will lead cause errors in later analysis scripts. To fix this, ensure there is a comma at the end of each line of data, except for the last one.

## Data Format

### Data.json

After processing, the data (`data.json`) looks like this:

    [
        {"data":{"gameVersion":"HighFraming","playDuration":480.002,"consent":[true,true,true],"answers":["6","6","6","6","1","2","2","2","2","2","2","nobug","","english","every-day"],"moves":[["circle","square","triangle"],["filled","empty","green"],["red","green","blue"],["big","empty","circle"],["small","empty","triangle"],["small","empty","triangle"],["filled","empty","green"],["red","green","blue"],["big","triangle","empty"],["small","empty","triangle"],["small","empty","circle"],["red","green","blue"],["empty","filled","green"],["empty","filled","green"],["green","red","blue"]],"moveDurations":[1.5314450000005309,1.915494999999486,1.7831050000004325,5.033134999999675,4.784264999998413,7.050825000000259,1.1063899999990099,2.8494300000002113,9.9504450000004,3.452929999999469,11.851834999999483,79.11336499999923,2.4985599999999977,34.44956000000093,3.0330149999990828]},"version":"4.1.0.explicit-framing-4.0.0.HighFraming"}
    ]

* **gameVersion**: Either "HighFraming" (with-instruction) or "LowFraming" (without-instruction).
* **playDuration**: seconds between start of logged (non-tutorial) levels, and play-end interrupt before post-test questionnaire
* **consent**: Checkbox values to consent questions, in order
* **answers**: Answers to the questions:
    1. Seven (7) Likert scale (`1-5`) answers to the Intrinsic Motivation Inventory: Enjoyment Subscale, in default question order
    2. Four (4) Likert scale (`1-6`) answers to the Play Framing questions (see `materials/questions.md`) in order
    3. What is your first language (`english`/`other`)
    4. How often do you play digital games? (`every-day`/`several-times-a-week`/`about-once-a-week`/`about-once-a-month`/`almost-never`)
    5. Answer to the question "Finally, did you encounter any bugs that may have had an effect on how you played the game? No/Yes" (`nobug`/`bug`)
    6. Description of the bug (optional, string / `null`)
* **moves**: Array of moves attempted by the player (sets of three words inputted, whether or not they trigger an action in the game). These are in order they were selected. Moves are in order attempted.
* **moveDurations**: Array of time taken (in seconds) for each move listed in `moves`.
* **version**: Game version and condition data was collected from. Note that 4.x is the explicit instructions experiment, the "explicit framing" tag is out of date.

### Age and Gender

`data/age-gender.csv` has records in the format: `age (number entry), gender (female/male/other/prefer-not-to-say)`

    36,female
    19,female
    58,male

This also includes participants who are excluded from the hypothesis tests due to too few inputs. (This also applies to participants who reported bugs). If this were not the case, it would prevent changing the minimum-input threshold after data collection (for example, if it becomes clear that the threshold as set is too high) due to the excluded data already being deleted during the process of anonymisation. Either we might not record all the age/genders (if the threshold is lowered), or we record too many age/genders. As we want to publish `data.json` including particpants excluded due to low input (to allow re-running the analysis with different thresholds), it seems better to record the age/genders that match to this potential superset and accept that the counts may not add up to exactly the same number.

### Duration

`data/duration.csv` has records in the format: `condition (HighFraming/LowFraming), duration in seconds`

    HighFraming,486.424
    LowFraming,485.231
    HighFraming,482.029

Because the duration of play (with tutorial) was controlled at 480 seconds (8 minutes), the variation that is observed here is accounted for by the time spent in menus/questionnaires. To see the time spent while moves were being logged in the main game, see the `playDuration` variable in `data.json`. This `duration` is separated from the rest of the data as (in principle) a player who spent an exceptional amount of time in the questionnaires could have their data identified in combination with Prolfic's log data. (`playDuration` is contained within the play and tutorial time that is fixed to almost exactly 480 seconds, so there is no such threat.)

This also includes participants who are excluded from the hypothesis tests due to too few inputs (or reporting bugs) as above.

## Analysis

In the project directory (for this experiment) run the following commands (on Linux). These create (or overwrite) files in `out/`).

    python python/check_exclusions.py > out/check_exclusions.txt

    python python/create_data_csv.py
    
    python python/hypothesis_test_exp4.py > out/hypothesis_test_exp4.txt

    python python/duration_analysis.py > out/duration_analysis.txt

    python python/age_gender_analysis.py  > out/age_gender_analysis.txt

## Output Dataset

The file `out/data.csv` is generated by running the `python/create_data_csv.py` script. This is for sanity checking and accessibility to future research.

* **version** - experiment condition
* **language** - first language (english/other)
* **gaming_frequency** - `every-day`/`several-times-a-week`/`about-once-a-week`/`about-once-a-month`/`almost-never`
* **consent_understand, consent_publication, consent** - three explicit consent checkboxes
* **pf1, pf2, pf3, pf4** - answers to 4 Play Framing questions (see `materials/questions.md`)
* **imi1, imi2, imi3, imi4, imi5, imi6, imi7** - answers to the 7 Intrinsic Motivation Inventory questions
* **bug** - whether or not bug reported (bug/nobug)
* **bugdesc** - optional text description of bug
* **imi_enjoyment** - overall IMI Enjoyment score
* **play_framing** - overall Play Framing score
* **total_moves** - number of moves made in game
* **moves_correct_form** - number of moves made that the game could detect are correctly formed (i.e. no duplicate in category, contains exactly 1 noun). In other words, a move that was potentially successful (assuming there were matching blocks to clear)
* **grammatical_moves_idealised** - number of grammatical moves, if against the idealised grammar described below
* **proportion_of_valid_data_total_idealised** - % grammatical (by idealised grammar) moves overall
* **proportion_of_valid_data_first20_idealised** - % grammatical (by idealised grammar) moves out of first 20
* **proportion_of_valid_data_providing_mechanic_actuations_total_idealised** - % grammatical (by idealised grammar) moves out of moves with correct form
* **moves_correct_form_last16** - number of moves with the correct form (see moves_correct_form) out of last 16 moves
* **grammatical_moves_last16_idealised** - number of grammatical moves out of last 16, if against idealised grammar
* **proportion_of_valid_data_last16_idealised** - % grammatical (by idealised grammar) moves out of last 16 moves
* **proportion_of_valid_data_providing_mechanic_actuations_last16_idealised** - % grammatical (by idealised grammar) out of last 16 moves of correct form
* **time_per_input_from_moveDurations** - average number of seconds taken by a move based on data recorded by game. This excludes time spent outside of the level/in level intro/ending modal dialogues. This is the best measure for considering how efficient the _core mechanic_ is at collecting data because it excludes extraneous interaction time.
* **time_per_input_from_8min** - average number of seconds taken by a move if we consider all the play time (after tutorial) including time the player isn't actively in the level, which was set by the experiment at 8 minutes. This is a fairer measure than moveDurations for the efficiency of the game overall at collecting data, as in practice a game is more than just its core mechanic.

### Idealised Grammar

For the idealised grammar, the following rules apply. The words in the game are grouped into category:

    Size: big, small
    Filledness: empty, filled
    Colour: red, blue, green
    Noun: square, circle, triangle, diamond

A grammatical noun phrase must contain a noun and the following precedence must hold (read `<<` to mean preceeds):

    Size << Filledness << Colour << Noun

And they must satisfy the "correct form" rule below.

Thus "big empty blue triangle" is judged grammatical, but if you rearrange that phrase in any way it is ungrammatical. The phrase "big blue empty triangle" would be judged ungramamtical but it might be an acceptable order for many people. As an idealised grammar, it will not necessarily correspond in all ways to actual usage.

### Correct form / mechanic actuations

The game mechanic can never be succesfully actuated by certain types of input. For example, blocks can never be described by two adjectives of the same type (e.g. "red" and "blue"). The game also requires that exactly 1 noun be selected.
