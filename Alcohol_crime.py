import arcpy
import os
gdp_path = r"C:\Users\shiva\Downloads\ProProject_Selections\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"
histdist_fc_name = "Wilson_Histdist"
crime_fc_name = "Wilson_Crimes96"

restaurant_fc_path = os.path.join(gdp_path,restaurant_fc_name)
histdist_fc_path = os.path.join(gdp_path,histdist_fc_name)
crime_fc_path = os.path.join(gdp_path,crime_fc_name)


arcpy.management.MakeFeatureLayer(restaurant_fc_path,"restaurant_lyr")
arcpy.management.MakeFeatureLayer(histdist_fc_path,"histdist_lyr")
arcpy.management.MakeFeatureLayer(crime_fc_path,"crime_lyr")

# getting count of all the features before selection
pre_count1=arcpy.GetCount_management("restaurant_lyr")
pre_count2=arcpy.GetCount_management("histdist_lyr")
pre_count3=arcpy.GetCount_management("crime_lyr")

print('Total Restaurants before selection = {}'.format(pre_count1[0]))
print('Total historic district before selection = {}'.format(pre_count2[0]))
print('Total crime before selection = {}'.format(pre_count3[0]))



arcpy.management.SelectLayerByAttribute("restaurant_lyr","NEW_SELECTION","ALCOHOL=1")
post_count1 = arcpy.GetCount_management("restaurant_lyr")
print('total restaurants serves alcohol = {}'.format(post_count1))

arcpy.management.SelectLayerByLocation("restaurant_lyr","WITHIN_A_DISTANCE","histdist_lyr","1000 feet","SUBSET_SELECTION")
post_count2 =arcpy.GetCount_management("restaurant_lyr")
print('total restaurants serves alcohol within 1000 feet of histdist = {}'.format(post_count2))

arcpy.management.SelectLayerByLocation("crime_lyr","WITHIN_A_DISTANCE","restaurant_lyr","500 feet")
post_count3 =arcpy.GetCount_management("crime_lyr")
print('crime near 500 feet of restaurant = {}'.format(post_count3))

arcpy.management.SelectLayerByAttribute("crime_lyr","SUBSET_SELECTION","ALCOHOL>0")
post_count4 = arcpy.GetCount_management("crime_lyr")
print('Alcohol related crime = {}'.format(post_count4))

