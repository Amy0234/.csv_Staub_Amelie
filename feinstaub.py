import csv
csv.list_dialects()
['excel', 'excel-tab', 'unix']
reader = csv.reader(open("sensor_3660.text"), delimiter = ";")
