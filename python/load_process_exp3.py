import pandas as pd
import json

def load_data(filename):
    rawData = []
    with open(filename+".json") as f:
        content = f.read()
        rawData = json.loads(content)
    return rawData

def process_data(rawData):
    data, language, version = [], [], [],
    for d in rawData:
        data.append(d["data"])
        language.append(d["data"]["answers"][11])
        version.append(d["data"]["gameVersion"])
            
    gaming_frequency = []
    c1, c2, c3 = [], [], []
    pf1, pf2, pf3, pf4, pf_value = [], [], [], [], []
    imi1, imi2, imi3, imi4, imi5, imi6, imi7, imi_enjoyment = [], [], [], [], [], [], [], []
    bug, bugdesc = [], []
    grammatical_moves_idealised, moves_correct_form, total_moves = [], [] ,[]
    proportion_of_valid_data_idealised, proportion_of_valid_data_providing_mechanic_actuations_idealised = [], []
    proportion_of_valid_data_first20_idealised = []
    grammatical_moves_last16_idealised, moves_correct_form_last16 = [], []
    proportion_of_valid_data_last16_idealised = []
    proportion_of_valid_data_providing_mechanic_actuations_last16_idealised = []
    proportion_of_valid_data_last10_idealised = []
    grammatical_moves_last10_idealised, moves_correct_form_last10 = [], []
    time_per_input_from_moveDurations = []
    time_per_input_from_8min = []
    for i, d in enumerate(data):
        gaming_frequency.append(d["answers"][12])
        c1.append(d["consent"][0])
        c2.append(d["consent"][1])
        c3.append(d["consent"][2])

        # Calculate IMI Enjoyment subscale mean and Play Framing mean
        # Scores for questions 3 and 4 of IMI and 4 of Play Framing are reversed
        a = [int(numeric_string) for numeric_string in d["answers"][0:11]]
        pf1.append(a[0])
        pf2.append(a[1])
        pf3.append(a[2])
        pf4.append(a[3])
        imi1.append(a[4])
        imi2.append(a[5])
        imi3.append(a[6])
        imi4.append(a[7])
        imi5.append(a[8])
        imi6.append(a[9])
        imi7.append(a[10])
        imi_value = (a[4] + a[5] + (6-a[6]) + (6-a[7]) + a[8] + a[9] + a[10])/7 # Out of 5, so reverse is 6-x
        imi_enjoyment.append(imi_value)
        pf_mean = (a[0] + a[1] + a[2] + (7-a[3]))/4 # Out of 6, so reverse is 7-x
        pf_value.append(pf_mean)

        bug.append(d["answers"][13])
        bugdesc.append(d["answers"][14])

        # Calculate proportions of valid moves (from total):
        count_gram_idealised = sum([is_grammatical_idealised(a) and correct_form(a) for a in d["moves"]])
        count_gram_first20_idealised = sum([is_grammatical_idealised(a) and correct_form(a) for a in d["moves"][:20]])
        count_correct_form = sum([correct_form(a) for a in d["moves"]])
        count_all = len(d["moves"])
        total_moves.append(count_all)
        grammatical_moves_idealised.append(count_gram_idealised)
        moves_correct_form.append(count_correct_form)
        if (count_all > 0):
            proportion_of_valid_data_idealised.append(count_gram_idealised/count_all)
        else:
            proportion_of_valid_data_idealised.append(0)
        proportion_of_valid_data_first20_idealised.append(count_gram_first20_idealised/20)
        if (count_correct_form > 0):
            proportion_of_valid_data_providing_mechanic_actuations_idealised.append(count_gram_idealised/count_correct_form)
        else:
            proportion_of_valid_data_providing_mechanic_actuations_idealised.append(0)
        # Calculate proportions of valid moves (from last 16):
        count_gram_last_16_idealised = sum([is_grammatical_idealised(a) and correct_form(a) for a in d["moves"][-16:]])
        count_gram_last_10_idealised = sum([is_grammatical_idealised(a) and correct_form(a) for a in d["moves"][-10:]])
        count_correct_form_last_16 = sum([correct_form(a) for a in d["moves"][-16:]])
        count_correct_form_last_10 = sum([correct_form(a) for a in d["moves"][-10:]])
        grammatical_moves_last16_idealised.append(count_gram_last_16_idealised)
        grammatical_moves_last10_idealised.append(count_gram_last_10_idealised)
        moves_correct_form_last16.append(count_correct_form_last_16)
        moves_correct_form_last10.append(count_correct_form_last_10)
        proportion_of_valid_data_last16_idealised.append(count_gram_last_16_idealised/16)
        proportion_of_valid_data_last10_idealised.append(count_gram_last_10_idealised/10)
        if (count_correct_form_last_16 > 0):
            proportion_of_valid_data_providing_mechanic_actuations_last16_idealised.append(count_gram_last_16_idealised/count_correct_form_last_16)
        else:
            proportion_of_valid_data_providing_mechanic_actuations_last16_idealised.append(None)

        #Calculate Time per input
        if (len(d["moveDurations"]) > 0):
            time_per_input_from_moveDurations.append(sum(d["moveDurations"])/len(d["moveDurations"]))
        else:
            time_per_input_from_moveDurations.append(None)
        if count_all > 0:
            time_per_input_from_8min.append((8*60)/count_all)
        else:
            time_per_input_from_8min.append(0)
    d = { 
            "version": version,
            "language": language,
            "gaming_frequency": gaming_frequency,
            "consent_understand": c1,
            "consent_publication": c2,
            "consent":c3,
            "pf1": pf1, "pf2": pf2, "pf3": pf3, "pf4": pf4,
            "imi1": imi1, "imi2": imi2, "imi3": imi3, "imi4": imi4, "imi5": imi5, "imi6": imi6, "imi7": imi7,
            "bug": bug,
            "bugdesc": bugdesc,
            "imi_enjoyment": imi_enjoyment,
            "play_framing": pf_value,
            "total_moves" : total_moves,
            "moves_correct_form": moves_correct_form,
            "grammatical_moves_idealised": grammatical_moves_idealised,
            "proportion_of_valid_data_total_idealised" : proportion_of_valid_data_idealised,
            "proportion_of_valid_data_first20_idealised" : proportion_of_valid_data_first20_idealised,
            "proportion_of_valid_data_providing_mechanic_actuations_total_idealised": proportion_of_valid_data_providing_mechanic_actuations_idealised,
            "moves_correct_form_last16": moves_correct_form_last16,
            "moves_correct_form_last10": moves_correct_form_last10,
            "grammatical_moves_last16_idealised": grammatical_moves_last16_idealised,
            "grammatical_moves_last10_idealised": grammatical_moves_last10_idealised,
            "proportion_of_valid_data_last16_idealised" : proportion_of_valid_data_last16_idealised,
            "proportion_of_valid_data_last10_idealised" : proportion_of_valid_data_last10_idealised,
            "proportion_of_valid_data_providing_mechanic_actuations_last16_idealised": proportion_of_valid_data_providing_mechanic_actuations_last16_idealised,
            "time_per_input_from_moveDurations": time_per_input_from_moveDurations,
            "time_per_input_from_8min": time_per_input_from_8min
        }
    df = pd.DataFrame(data=d)
    return df

def is_grammatical_idealised(array):
    a = []
    adj1 = ["big", "small"]
    adj2 = ["empty", "filled"]
    adj3 = ["red", "blue", "green"]
    nouns = ["square","circle","triangle","diamond"]
    for word in array:
        if word in adj1:
            a.append(1)
        if word in adj2:
            a.append(2)
        if word in adj3:
            a.append(3)
        if word in nouns:
            a.append(4)
    return (a[0] < a[1] < a[2]) and has_noun(array)


def correct_form(array):
    a1, a2, a3, n = 0,0,0,0
    adj1 = ["big", "small"]
    adj2 = ["empty", "filled"]
    adj3 = ["red", "blue", "green"]
    nouns = ["square","circle","triangle","diamond"]
    for word in array:
        if word in adj1:
            a1 += 1
        elif word in adj2:
            a2 += 1
        elif word in adj3:
            a3 += 1
        elif word in nouns:
            n += 1
    return (a1 < 2) and (a2 < 2) and (a3 < 2) and (n == 1)

def has_noun(array):
    nouns = ["square","circle","triangle","diamond"]
    for word in array:
        if word in nouns:
            return True
    return False