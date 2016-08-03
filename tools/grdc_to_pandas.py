import pandas as pd

def convert(filename, area):
    #specify a file
    filepath = '../data/'+filename

    #read the data
    data = pd.read_csv(filepath, skiprows=40, header=0, sep=';',\
    index_col = 0, parse_dates=True, usecols=[0, 3],\
    names = ['Data', 'Runoff'], na_values='-999')

    #calculate the transformation coefficient
    #86400 for seconds to day transformation
    #1'000'000 for sq.km to sq.m trasformation
    #1000 for m/day to mm/day transformation
    coef = (86400*1000)/(area*1000000)

    #add a column with mm/day values
    data['Qobs'] = data['Runoff']*coef

    Qobs = data['Qobs']

    return Qobs

def convert_mon(filename, area):
    # changes from DAILY vesrsion:
    # 1. pd.read_csv reads 2nd column (in daily we read 3rd one)

    #specify a file
    filepath = '../data/'+filename

    #read the data
    data = pd.read_csv(filepath, skiprows=40, header=0, sep=';',\
    index_col = 0, parse_dates=True, usecols=[0, 2],\
    names = ['Data', 'Runoff'], na_values=[-999, -9999])

    #calculate the transformation coefficient
    #86400 for seconds to day transformation
    #1'000'000 for sq.km to sq.m trasformation
    #1000 for m/day to mm/day transformation
    coef = (86400*1000)/(area*1000000)

    #add a column with mm/day values
    data['Qobs'] = data['Runoff']*coef

    Qobs = data['Qobs']

    return Qobs
