## Output the number of users in each condition that are not excluded from analysis

import numpy as np
from load_process_exp4 import load_data, process_data

minimum_moves = 10

dataset = 'data'
print("Analysing dataset", dataset, "\n")
rawData = load_data("data/"+dataset)
df = process_data(rawData)

before_consent = len(df.index)
df = df[df['consent_understand'] == True]
df = df[df['consent_publication'] == True]
df = df[df['consent'] == True]
print("Excluded due to lack of consent (should be 0)", before_consent - len(df.index))

before_move_min = len(df.index)
df = df[df['total_moves'] >= minimum_moves]
print("Excluded due to moves <", minimum_moves, "=", (before_move_min - len(df.index)))

before_nobug = len(df.index)
df = df[df['bug'] == "nobug"]
print("Excluded due reporting bugs", before_nobug - len(df.index))

before_language = len(df.index)
df = df[df['language'] == "english"]
print("Excluded due to language", before_language - len(df.index), "(should be 0 as already excluded)")

highFramingCondition = df[df['version']=='HighFraming']
lowFramingCondition = df[df['version']=='LowFraming']

print("Total count", len(df.index))
print("Count in HighFraming condition", len(highFramingCondition.index))
print("Count in LowFraming condition", len(lowFramingCondition.index))