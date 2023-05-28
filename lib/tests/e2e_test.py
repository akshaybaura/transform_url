import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import polars as pl
import pytest
from polars.testing import assert_frame_equal
from transformer import Transformer

@pytest.fixture
def transformer():
    # Create an instance of the Transformer class
    return Transformer()

@pytest.fixture
def input_file():
    # Specify the input file path
    return f"{os.path.dirname(__file__)}/data/test_input.csv"

@pytest.fixture
def output_file():
    # Specify the output file path
    return f"{os.path.dirname(__file__)}/data/test_output.csv"

@pytest.fixture
def expected_dataframe():
    # Define the expected dataframe
    return pl.DataFrame([
        {'UserId': 1, 'ContentId': 1, 'ContentUrl': 'https://www.google.com', 'HostName': 'www.google.com',
         'Domain': 'google.com'},
        {'UserId': 2, 'ContentId': 2, 'ContentUrl': 'https://www.abc.gov', 'HostName': 'www.abc.gov',
         'Domain': 'abc.gov'},
        {'UserId': 4, 'ContentId': 4, 'ContentUrl': 'file://abcde', 'HostName': 'NA', 'Domain': 'NA'}
    ])

def test_transform_content_hostname(transformer, input_file, output_file, expected_dataframe):
    # Execute the transformation
    transformer.transform_content_hostname(input_file, output_file)

    # Read the resultant dataframe from the output file
    left_df = pl.read_csv(output_file)

    # Compare the expected dataframe with the resultant dataframe
    assert_frame_equal(left_df, expected_dataframe, check_column_order=False, check_row_order=False)

