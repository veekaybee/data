#!/usr/bin/python

from sys import argv
import time
from datetime import date
from subprocess import call

#input variable is the table name to be partitioned
script_name, table_name= argv

#date, month, and year are all dynamically-generated; schema is manual input
curr_year=date.today().year
curr_month=date.today().month
curr_day=date.today().day
days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
schema="schemaname"

#partition creation goes to end of current year and calls hive in the program
for year in range(curr_year,curr_year+1):
        for month in range(curr_month,13):
                for day in range(2,days_in_month[month-1]+1):
                        for hour in range (24):
                                hive_string ="""-e use %s; ALTER TABLE %s ADD PARTITION (date_key=%s%02d%02d, hour=%02d) location '/hdfs/directory/%s/%s%02d%02d/%02d'"""  % (schema,table_name,year,month,day,hour,table_name,year,month,day,hour)
                                print hive_string
                                call(["hive",hive_string])