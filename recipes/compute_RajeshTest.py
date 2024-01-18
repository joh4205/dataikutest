# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
crm_history = dataiku.Dataset("crm_history")
crm_history_df = crm_history.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

RajeshTest_df = crm_history_df # For this sample code, simply copy input to output


# Write recipe outputs
RajeshTest = dataiku.Dataset("RajeshTest")
RajeshTest.write_with_schema(RajeshTest_df)
