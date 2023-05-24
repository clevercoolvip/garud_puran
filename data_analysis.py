import pandas as pd
import numpy as np
import seaborn as sns
import statistics as st
import matplotlib.pyplot as plt

def removenan(df):
    """
    Param1: pandas dataframe

    return: pandas dataframe
    """
    df.dropna(inplace=True)
    return df


def check_dtype(col):
    """
    Param1: pandas series

    return: Boolean
    """
    df = pd.DataFrame(col)
    df = df.squeeze()
    dtype = col.dtype
    if dtype=="float64" or dtype=="int64":
        return True
    else:
        return False


def mean(col):
    """
    Param1: pandas series

    return: int
    """
    if check_dtype(col):
        return np.mean(col)
    return -1


def median(col):
    """
    Param1: pandas series

    return: int
    """
    if check_dtype(col):
        return np.median(col)
    return -1


def std(col):
    """
    Param1: pandas series

    return: int
    """
    if check_dtype(col):
        return st.stdev(col)
    return -1
    

def removeOutlier(col):
    """
    Param1: pandas series

    return: pandas dataframe
    """
    if check_dtype(col):
        init_thresh = mean(col) - 3*std(col)
        final_thresh = mean(col) + 3*std(col)
        print(init_thresh)
        print(final_thresh)
        df = pd.DataFrame(col, columns=["col1"])
        return df[(df.col1>init_thresh) & (df.col1<final_thresh)]
    return -1


def uniques_bar_graph(col):
    """
    Param1: pandas series

    return: seaborn plot
    """

    if check_dtype(col) == False:
        unq_len = len(pd.unique(col))
        print(f"Unique Values: {unq_len}")
        if unq_len<20:
            sns.countplot(data=col, x=col, hue=col)
            plt.show()
        else:
            pass
    return -1


def column_description(col):
    """
    Param1: pandas series

    return: dictionary/JSON
    """

    json = {
        "Datatype":{type(col)},
        "Description":pd.DataFrame(col).describe(),
    }
    return json


def domains(col):
    """
    Param1: pandas series

    return: dictionary/JSON
    """
    json = {
        "Min":pd.DataFrame(col).min(),
        "Max":pd.DataFrame(col).max()
    }
    return json


path2 = "test1.csv"
df = pd.read_csv(path2)
print(df.head())
removenan(df)
for i in range(len(df.columns)):
    print(domains(df.iloc[:, i]))
# uniques_bar_graph(df.iloc[:, 0])