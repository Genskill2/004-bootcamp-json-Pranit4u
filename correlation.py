# Add the functions in this file
import json
import math
def load_journal(fileName):
    f = open(fileName)
    data = f.read()
    parsed_data = json.loads(data)
    return parsed_data
def compute_phi(parsed_data,event):
    n11 = n00 = n10 = n01 = n1_ = n0_ = n_1 = n_0 = 0
    for i in parsed_data:
        ev = event in i["events"]
        sq = i["squirrel"]
        if ev == True:
            n1_ += 1
            if sq == True:
                n_1 += 1
                n11 += 1
            elif sq == False:
                n_0 += 1
                n10 += 1
        elif ev == False:
            n0_ += 1
            if sq == True:
                n_1 += 1
                n01 += 1
            elif sq == False:
                n_0 += 1
                n00 += 1
    cor = ((n11 * n00) - (n10 * n01)) / math.sqrt(n1_ * n0_ * n_1 * n_0)
    return cor
def compute_correlations(fileName):
    parsed_data = load_journal(fileName)
    myDict = {}
    for d in parsed_data:
        for e in d["events"]:
            if e not in myDict:
                cor = compute_phi(parsed_data,e)
                myDict[e] = cor
    return myDict
def diagnose(fileName):
    myDict = compute_correlations(fileName)
    max_event = max(myDict, key=lambda x:myDict[x])
    min_event = min(myDict, key=lambda x:myDict[x])
    return max_event,min_event

