# Full path and name to your csv file
csv_filepathname="/Users/skj/Interviews/homelane bckend /homelane/data.csv"

# Full path to the directory immediately above your django project directory
djangoproject_home="/Users/skj/Interviews/homelane bckend /homelane"
############ All you need to modify is above ############

import sys,os
sys.path.append(djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] ='homelane.settings'
import django
django.setup()

from dataservice.models import Data

import csv
with open(csv_filepathname) as file:

    csvreaded = csv.reader(file)
    header = next(csvreaded)

    for row in csvreaded:
        data=Data()
        data.date = row[0]
        data.price = row[1]
        data.bedrooms = row[2]
        data.bathrooms = row[3]
        data.sqft_living = row[4]
        data.sqft_lot = row[5]
        data.floors = row[6]
        data.waterfront = row[7]
        data.view = row[8]
        data.condition = row[9]
        data.sqft_above = row[10]
        data.sqft_basement = row[11]
        data.yr_built = row[12]
        data.yr_renovated = row[13]
        data.street = row[14]
        data.city = row[15]
        data.statezip = row[16]
        data.country = row[17]
        data.save()