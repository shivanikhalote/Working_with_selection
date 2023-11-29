import arcpy
import os
gdp_path = r"C:\Users\shiva\Downloads\ProProject_Selections\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"

restaurant_fc_path = os.path.join(gdp_path,restaurant_fc_name)

# making feature class to feature layer
arcpy.management.MakeFeatureLayer(restaurant_fc_path,"restaurant_lyr")

# getting count of all the features before selection
pre_count1=arcpy.GetCount_management("restaurant_lyr")

print("Total number of restaurans = {}".format(pre_count1))







