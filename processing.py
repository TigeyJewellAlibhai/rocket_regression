import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def strip_values(data, strippable):
    '''
    Takes a dataframe row and strips specific values off of it at all points
    in the data.

    Args:
        data: the dataframe column to process
        strippable: a list of all strings to strip from the the data. The full
        string has to be present for it to be stripped

    Returns:
        a dataframe column with the processed data
    '''
    for string in strippable:
        data = data.str.replace(string, '')
    data = pd.to_numeric(data)
    return data


def text_to_numeric(df, which_row, lookup):
    '''
    Takes a dataframe and a dictionary, and creates a new numeric dataframe row
    based on entries in the dictionary. If no value is given for a specific
    item, makes the value 0.

    Args:
        dataframe: the dataframe in which to find the non numeric values
        which_row: the row of the dataframe to make numerical
        lookup: a dictionary consisting of keys that are in arg row, and their
        numerical translation as the value

    Returns:
        a dataframe row consisting of values that have been made numerical
    '''
    return df.apply(lambda row: lookup.get(str(row[which_row]), 0), axis=1)


def clean_dataframe(df, time_col):
    '''
    Takes a dataframe and cleans it according to a slightly hardcoded system
    where units are removed from Price, Liftoff Thrust, and Rocket Height
    columns, None values are dropped, and a designated time column is
    converted to official datetime format.

    Args:
        dataframe: the input dataframe to clean
        time_col: the time column of the dataframe

    Returns:
        a cleaned dataframe
    '''
    df = df.dropna(subset=['Time', 'Outcome', 'Price'])
    df['Price'] = strip_values(df['Price'], ['$', ' million', ','])
    df['Liftoff Thrust'] = strip_values(df['Liftoff Thrust'], [' kN', ','])
    df['Rocket Height'] = strip_values(df['Rocket Height'], [' m'])
    df[time_col] = pd.to_datetime(df[time_col], infer_datetime_format=True,
                                  utc=True)
    return df


def resample_numeric(df, num):
    '''
    Takes a dataframe and a number of points, and resamples the dataframe along
    the preset index column so that is has a specified numer of evenly
    distributed points along the index. Interpolates to generate this evenness.
    I don't pytest this function because it is to do with visualization and
    would be complex to implement an effective pytest for.

    Args:
        df: the dataframe to resample
        num: the number of rows for the final dataframe to include

    Returns:
        a resampled dataframe
    '''
    resampled = np.linspace(df.index[0], df.index[-1], num)
    print(df.index[0], df.index[-1])
    df_resampled = df.reindex(df.index.union(resampled)).interpolate('linear') \
                     .loc[resampled]
    return df_resampled.reset_index()
