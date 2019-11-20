# Border-Crossing-Analysis

## Required libraries

- import csv, sys
- from datetime import datetime as dt
- import collections

## Solution

### Read input file: read_border_data()

The input file **Border_Crossing_Entry_Data.csv** is read as a list, each element of the list is a namedtuple (BorderCross)  defined as below: 

```python
BorderCross = collections.namedtuple('BorderCross', 'Port_Name, State, Port_Code, Border, Date, Measure, Value, Location')
```

### Process the input file to generate running montly average: border_data_analysis

## Comments

The test dataset includes 8 fields, 'Port_Name, State, Port_Code, Border, Date, Measure, Value, Location'.

However, the [dataset](https://data.transportation.gov/Research-and-Statistics/Border-Crossing-Entry-Data/keg4-3bc2) in BTS website includes only 7 fields without **Location**.

So I defined 2 namedtuples in border_analytics.py for reading both types of dataset. 

```python
# For reading the test dataset
BorderCross = collections.namedtuple('BorderCross', 'Port_Name, State, Port_Code, Border, Date, Measure, Value, Location')

# For reading BTS dataset
#BorderCross = collections.namedtuple('BorderCross', 'Port_Name, State, Port_Code, Border, Date, Measure, Value')
```

​    

