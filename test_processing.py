import pytest
import processing
import pandas as pd

TEST_DATAFRAME_1 = pd.DataFrame(
    [['$4$4', 44, '44 Thousand', 'Mark', 1, 0],
     ['8%M', 8, '8 kN', 'Bois', 2, 1],
     ['M0', 0, '0 bois', 'and', 0, 100],
     [' 0!  ', 0, '0 copepods', 'the', 0, 0]],
    columns=['1', '2', '3', '4', '5', '6']
)

TEST_DATAFRAME_2 = pd.DataFrame(
    {'Time': ['Sun Nov 10, 1968 19:11 UTC', 'Mon May 10, 1971 16:58 UTC'],
     'Price': ['$47.0 million', '$100.0 million'],
     'Outcome': ['Success', 'Failure'],
     'Rocket Height': ['20 m', '50 m'],
     'Liftoff Thrust': ['150 kN', '20 kN']}
)

TEST_DATAFRAME_3 = pd.DataFrame(
    {'Time': pd.to_datetime(['Sun Nov 10, 1968 19:11 UTC',
                             'Mon May 10, 1971 16:58 UTC']),
     'Price': [47.0, 100.0],
     'Outcome': ['Success', 'Failure'],
     'Rocket Height': [20, 50],
     'Liftoff Thrust': [150, 20]}
)

TEST_DATAFRAME_4 = pd.DataFrame(
    {'Time': ['Sun Nov 10, 1968 19:11 UTC', 'Mon May 10, 1971 16:58 UTC'],
     'Price': ['$47.0 million', '$100.0 million'],
     'Outcome': ['Success', None],
     'Rocket Height': ['20 m', '50 m'],
     'Liftoff Thrust': ['150 kN', '20 kN']}
)

TEST_DATAFRAME_5 = pd.DataFrame(
    {'Time': pd.to_datetime(['Sun Nov 10, 1968 19:11 UTC']),
     'Price': [47.0],
     'Outcome': ['Success'],
     'Rocket Height': [20],
     'Liftoff Thrust': [150]}
)

# Test cases for strip_values
strip_values_cases = [
    (TEST_DATAFRAME_1['1'], ['$', '!', '%', 'M', ' '], TEST_DATAFRAME_1['2']),
    (TEST_DATAFRAME_1['3'], ['', 'Thousand', 'kN', 'bois', 'copepods'],
     TEST_DATAFRAME_1['2'])
]


@pytest.mark.parametrize("input1,strippables,expected", strip_values_cases)
def test_strip_values(input1, strippables, expected):
    assert processing.strip_values(input1, strippables).equals(expected)


# Test cases for text_to_numeric
text_to_numeric_cases = [
    (TEST_DATAFRAME_1, '4', {'Mark': 1, 'Bois': 2}, TEST_DATAFRAME_1['5']),
    (TEST_DATAFRAME_1, '4', {'Bois': 1, 'and': 100}, TEST_DATAFRAME_1['6'])
]


@pytest.mark.parametrize("dataframe,row,lookup,expected", text_to_numeric_cases)
def test_text_to_numeric(dataframe, row, lookup, expected):
    assert processing.text_to_numeric(dataframe, row, lookup).equals(expected)


# Test cases for clean_dataframe
clean_dataframe_cases = [
    (TEST_DATAFRAME_2, 'Time', TEST_DATAFRAME_3),
    (TEST_DATAFRAME_4, 'Time', TEST_DATAFRAME_5),
]


@pytest.mark.parametrize("dataframe,time_col,expected", clean_dataframe_cases)
def test_clean_dataframe(dataframe, time_col, expected):
    assert processing.clean_dataframe(dataframe, time_col).equals(expected)
