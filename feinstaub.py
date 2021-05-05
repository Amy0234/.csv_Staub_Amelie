import csv

reader = csv.reader(open("C:\\Users\\Amelie Spichartz\\.csv_Staub_Amelie\\sensor_3660.text"), delimiter = ";")

for row in reader:
    print (f'Zeit: {row [5]} Temperatur: {row [6]} Grad ')