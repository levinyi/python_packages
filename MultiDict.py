import sys

def addtwodimdict(thedict, key_a, key_b, val):
    ''' this is a function to add two dimetion dict '''
    if key_a in thedict:
        thedict[key_a].setdefault(key_b,[]).append(val)
    else:
        thedict.update({key_a:{key_b:[val]}})
    return thedict
