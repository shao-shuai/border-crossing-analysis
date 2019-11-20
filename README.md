# Border-Crossing-Analysis

## Required libraries

- import csv, sys
- from datetime import datetime as dt
- import collections

## Solution

### read_border_data()

`read_border_data()` is used to read input file **Border_Crossing_Entry_Data.csv** as a list defined as `borderCross`, each element of the list is a namedtuple (BorderCross)  defined as below: 

```python
BorderCross = collections.namedtuple('BorderCross', 'Port_Name, State, Port_Code, Border, Date, Measure, Value, Location')
```

`borderCross` for the test dataset is below:

```python
BorderCross(Port_Name='Derby Line', State='Vermont', Port_Code='209', Border='US-Canada Border', Date='03/01/2019 12:00:00 AM', Measure='Truck Containers Full', Value='6483', Location='POINT (-72.09944 45.005)')
BorderCross(Port_Name='Norton', State='Vermont', Port_Code='211', Border='US-Canada Border', Date='03/01/2019 12:00:00 AM', Measure='Trains', Value='19', Location='POINT (-71.79528000000002 45.01)')
BorderCross(Port_Name='Calexico', State='California', Port_Code='2503', Border='US-Mexico Border', Date='03/01/2019 12:00:00 AM', Measure='Pedestrians', Value='346158', Location='POINT (-115.49806000000001 32.67889)')
BorderCross(Port_Name='Hidalgo', State='Texas', Port_Code='2305', Border='US-Mexico Border', Date='02/01/2019 12:00:00 AM', Measure='Pedestrians', Value='156891', Location='POINT (-98.26278 26.1)')
BorderCross(Port_Name='Frontier', State='Washington', Port_Code='3020', Border='US-Canada Border', Date='02/01/2019 12:00:00 AM', Measure='Truck Containers Empty', Value='1319', Location='POINT (-117.78134000000001 48.910160000000005)')
BorderCross(Port_Name='Presidio', State='Texas', Port_Code='2403', Border='US-Mexico Border', Date='02/01/2019 12:00:00 AM', Measure='Pedestrians', Value='15272', Location='POINT (-104.37167 29.56056)')
BorderCross(Port_Name='Eagle Pass', State='Texas', Port_Code='2303', Border='US-Mexico Border', Date='01/01/2019 12:00:00 AM', Measure='Pedestrians', Value='56810', Location='POINT (-100.49917 28.70889)')
```

### border_data_analysis()

`border_data_analysis()` is used to:

- merge data entries with the same Border, Date and Measure in `borderCross` into a single entry, and generate `report` based on the merged entries
- calculate running monly average of each entry in `report`

#### Merge data entries with the same Border, Date, and Measure in borderCross

A Report (also a namedtuple) is created for writing running monthly average data.

```python
Report = collections.namedtuple('Report', 'Border, Date, Measure, Value, Average')
```

`border_measure_date_string` is a list created to store unique string of border, date and measure in `borderCross`. Before looping an element in `borderCross`, whether the border_date_measure string of the element is in `border_measure_date_string` is determined. If no, the element's corresponding fields (Border, Date, Measure, and Value) will be assigned to `report` plus an average field of value 0, and the border_date_measure string will be appended to `border_measure_date_string`. If yes, the Value of the element will be summed up with the value under the same border_date_measure string in the `report`.

```python
Report(Border='US-Mexico Border', Date=datetime.datetime(2019, 3, 1, 0, 0), Measure='Pedestrians', Value=346158, Average=114487)
Report(Border='US-Canada Border', Date=datetime.datetime(2019, 3, 1, 0, 0), Measure='Truck Containers Full', Value=6483, Average=0)
Report(Border='US-Canada Border', Date=datetime.datetime(2019, 3, 1, 0, 0), Measure='Trains', Value=19, Average=0)
Report(Border='US-Mexico Border', Date=datetime.datetime(2019, 2, 1, 0, 0), Measure='Pedestrians', Value=172163, Average=56810)
Report(Border='US-Canada Border', Date=datetime.datetime(2019, 2, 1, 0, 0), Measure='Truck Containers Empty', Value=1319, Average=0)
Report(Border='US-Mexico Border', Date=datetime.datetime(2019, 1, 1, 0, 0), Measure='Pedestrians', Value=56810, Average=0)
```

#### Calculate running monthly average

`border_measure_string` is a dictionary with its keys storing unique string of border and measure, the value of each key is a list of tuples including `(date, value)` pairs. when looping an element in `report`, the date of the element will be compared with the date in `(date, value)` pairs to filter out all previous months and the corresponding values. The running monthly is calculated based on the previous months and the values.

### write_report()

`write_report()` is used to write `report` into **report.csv**

## Comments

The test dataset includes 8 fields, 'Port_Name, State, Port_Code, Border, Date, Measure, Value, Location'.

However, the [dataset](https://data.transportation.gov/Research-and-Statistics/Border-Crossing-Entry-Data/keg4-3bc2) in BTS website includes only 7 fields without **Location**.

So I defined 2 namedtuples in border_analytics.py for reading both types of data. 

```python
# For reading the test dataset
BorderCross = collections.namedtuple('BorderCross', 'Port_Name, State, Port_Code, Border, Date, Measure, Value, Location')

# For reading BTS dataset
#BorderCross = collections.namedtuple('BorderCross', 'Port_Name, State, Port_Code, Border, Date, Measure, Value')
```

​    

