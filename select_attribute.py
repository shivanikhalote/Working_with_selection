# commonly used termed when working with  selections

# Feature class: A table containing an attribute field that store geometry that defines shape of a feature.
# Feature Layer: An in-memory representation of the data in a feature class
# Table : A Storage container for rows that contain field to store data
# TableView: An in-memory representation of the datas in a table

import arcpy
import os
gdp_path = r"C:\Users\shiva\Downloads\ProProject_Selections\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"
restaurant_fc_path = os.path.join(gdp_path,restaurant_fc_name)
arcpy.management.MakeFeatureLayer(restaurant_fc_path,"restaurant_lyr")
# getting count of all the features before selection
pre_count=arcpy.GetCount_management("restaurant_lyr")
print('Total Rows in Feature Class = {}'.format(pre_count[0]))

# select by attribute
arcpy.management.SelectLayerByAttribute("restaurant_lyr","NEW_SELECTION","TYPE = 1")
post_count = arcpy.GetCount_management('restaurant_lyr')
print('Number of Family Restaurant = {}'.format(post_count[0]))

output_file_name = "Wilson_Restaurant_Family"
Family_restaurant_fc_path = os.path.join(gdp_path,output_file_name)

arcpy.management.CopyFeatures("restaurant_lyr",Family_restaurant_fc_path)
