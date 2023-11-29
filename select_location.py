import arcpy
import os
gdp_path = r"C:\Users\shiva\Downloads\ProProject_Selections\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"
histdist_fc_name = "Wilson_Histdist"

restaurant_fc_path = os.path.join(gdp_path,restaurant_fc_name)
histdist_fc_path = os.path.join(gdp_path,histdist_fc_name)
arcpy.management.MakeFeatureLayer(restaurant_fc_path,"restaurant_lyr")
arcpy.management.MakeFeatureLayer(histdist_fc_path,"histdist_lyr")
# getting count of all the features before selection
pre_count=arcpy.GetCount_management("restaurant_lyr")
print('Total Restaurants before selection = {}'.format(pre_count[0]))
pre_count1=arcpy.GetCount_management("histdist_lyr")
print('Total Historical District before selection = {}'.format(pre_count1[0]))

arcpy.management.SelectLayerByLocation("restaurant_lyr","COMPLETELY_WITHIN","histdist_lyr")
post_count = arcpy.GetCount_management("restaurant_lyr")
print('total restaurants completly within a historial district = {}'.format(post_count))

output_restaurant_wintin_histdist = "Wilson_within_histdist_restaurant"
output_restaurant_wintin_histdist_path = os.path.join(gdp_path,output_restaurant_wintin_histdist)
arcpy.management.CopyFeatures("restaurant_lyr",output_restaurant_wintin_histdist_path)