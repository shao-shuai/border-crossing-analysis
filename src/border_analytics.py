#!/usr/bin/env python
# coding: utf-8

import csv, sys
from datetime import datetime as dt
import collections

# Read Border_Crossing_Entry_Data.csv as a list of namedtuple
def read_border_data(input_file):
    borderCross=[]
    for emp in map(BorderCross._make, csv.reader(open(input_file, "r"))):
        borderCross.append(emp)
    
    # Remove first row of field names
    borderCross.pop(0)

    return borderCross

# Merge data with the same Border, Measure, and Date to write report, and calculate running monthly average
def border_data_analysis(borderCross):
    report=[]
    border_measure_date_string = []
    border_measure_string = dict()

    for entry in borderCross:
        border_measure = entry.Border + ',' + entry.Measure
        unique_record_string = border_measure + ',' + entry.Date

        if unique_record_string not in border_measure_date_string:
            border_measure_date_string.append(unique_record_string)
            temp_output = Report(entry.Border, dt.strptime(entry.Date, '%m/%d/%Y %I:%M:%S %p'), entry.Measure, int(entry.Value), 0)
            report.append(temp_output)
                
        else:
            record_index = border_measure_date_string.index(unique_record_string)
            report[record_index]=report[record_index]._replace(Value=report[record_index].Value+int(entry.Value))
        
        if border_measure not in border_measure_string:
            border_measure_string[border_measure] = []
    
        border_measure_string[border_measure].append((dt.strptime(entry.Date, '%m/%d/%Y %I:%M:%S %p'), int(entry.Value)))

    # Sort report by Date, Value, Measure, and Border 
    report.sort(key=lambda x:x.Border, reverse = True)
    report.sort(key=lambda x:x.Measure, reverse = True)
    report.sort(key=lambda x:x.Value, reverse = True)
    report.sort(key=lambda x:x.Date, reverse = True)            

    # Calculate running monthly average
    for index, entry in enumerate(report):
        border_measure = entry.Border + ',' + entry.Measure
        current_date = entry.Date
        
        date_value = border_measure_string[border_measure]

        # Get all previous values
        previous_values = [value for datestr, value in date_value if datestr<current_date]
        
        # Get all previous months for each pair of border and measure
        previous_months = set([datestr for datestr,_ in date_value if datestr<current_date])
        
        if previous_months:
            report[index]=report[index]._replace(Average=round(0.1+sum(previous_values)/len(previous_months)))

    return report

# Write report to report.csv
def write_report(report):
    with open(output_file, 'w') as f:
        w = csv.writer(f)
        w.writerow(('Border', 'Date', 'Measure', 'Value', 'Average'))
        w.writerows([i.Border, i.Date.strftime('%m/%d/%Y %I:%M:%S %p'), i.Measure, i.Value, i.Average] for i in report)


if __name__ == '__main__':

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    print('input file is ', input_file +'\n')
    print('output file is ', output_file + '\n')

    # Namedtuple for reading Border_Crossing_Entry_Data.csv
    BorderCross = collections.namedtuple('BorderCross', 'Port_Name, State, Port_Code, Border, Date, Measure, Value, Location')

    # Namedtuple for reading datasets on BTS website
    #BorderCross = collections.namedtuple('BorderCross', 'Port_Name, State, Port_Code, Border, Date, Measure, Value')

    # Namedtuple for writing report
    Report = collections.namedtuple('Report', 'Border, Date, Measure, Value, Average')

    # Read Border_Crossing_Entry_Data.csv
    borderCross = read_border_data(input_file)

    # Generate report
    report = border_data_analysis(borderCross)

    # Write report
    write_report(report)
