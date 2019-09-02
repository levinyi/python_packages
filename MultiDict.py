#!/usr/bin/env python


def two_dim_all_uniq(thedict, key_a, key_b, val):
    ''' this is a function to add two dimetion dict
    dict_a = {
        'd1' : {'umi1':'a','umi8':'b'},
        'd2' : {'umi2':'b'},
        'd3' : {'umi3':'c'},
    }
    '''
    if key_a in thedict:
        thedict[key_a].setdefault(key_b, []).append(val)
    else:
        thedict.update({key_a: {key_b: [val]}})
    return thedict


def two_dim_value_sum(thedict, key_a, key_b, value):
    '''  value is number, and need sum up.   '''
    if key_a in thedict:
        if key_b in thedict[key_a]:
            value = thedict[key_a][key_b] + value
            thedict[key_a].update({key_b: value})
        else:
            thedict[key_a].update({key_b: value})
    else:
        thedict.update({key_a: {key_b: value}})
    return thedict


def two_dim_value_list(thedict, key_a, key_b, val):
    ''' two dim: the value is a list.
    dict_a = {
        'A1' : {'umi1'：['AB','CD','EF'], 
                'umi8':['DW','KI']},
        'B2' : {'umi2': ['GB','RE','SD']},
        'C3' : {'umi3': ['GE','WE','WE','WQ']},
    }
    '''
    if key_a in thedict:
        thedict[key_a].setdefault(key_b, []).append(val)
    else:
        thedict.update({key_a: {key_b: [val]}})
    return thedict
