import pandas as pd # To run this script, you first need to install the "pandas" Python package, which is used to manipulate tabular data. Try the command "pip install pandas" if you don't already have it.

# Write the full file path to the ecoinvent LCIA file, which might be named something like "Cut-off Cumulative LCIA v3.9.1.xlsx"
ecoinvent_path = "C:/Users/write-your-path-here/Cut-off Cumulative LCIA v3.9.1.xlsx"
# Write the file paths to the biodiversity tool (preferably the detailed version), and to the location where you want the results to be exported.
tool_path = 'C:/Users/write-your-path-here/Biodiversity tool_detailed_v1.1.xlsm'
output_path = 'C:/Users/write-your-path-here/results.xlsx'

print('Reading ecoinvent...') # Reading the ecoinvent file - this can take a long time!
ecoinvent=pd.read_excel(ecoinvent_path,sheet_name='LCIA')

# Due to the way the ecoinvent Excel file is formatted, the columns have weird names. We will rename them, and only select the columns relevant for ecosystem quality.
activity_name='Unnamed: 1'
geography='Unnamed: 2'
ref_product='Unnamed: 3'
unit='Unnamed: 4'
total_eco_qual='ReCiPe 2016 v1.03, endpoint (H).22'
relevant_columns=[activity_name,geography,ref_product,unit,total_eco_qual]
rename_dict={activity_name:'Activity Name', geography:'Geography', ref_product:'Reference Product Name', unit:'Reference Product Unit'}

ecoinvent_redux=ecoinvent[relevant_columns].rename(columns=rename_dict)

print('Reading biodiversity tool...') # Reading the background data sheet in the biodiversity tool. Please note that the sheet name is different if you're using the simple version of the tool - it should be "Data_materials".
background_data_sheet=pd.read_excel(tool_path,sheet_name='Background_env_data')

# Again the data does not start from the top of the sheet so we need to rename columns and delete empty rows.
rename_dict2=dict()
for c in background_data_sheet.columns:
    rename_dict2[c] = background_data_sheet[c].iloc[5]
background_data_sheet=background_data_sheet.rename(columns=rename_dict2).iloc[6:]

activity_name2=background_data_sheet.columns[0]
geography2=background_data_sheet.columns[1]
ref_product2=background_data_sheet.columns[2]
unit2=background_data_sheet.columns[3]
total_eco_qual2=background_data_sheet.columns[5]

# Now we merge the ecoinvent table with the background data table, matching rows with the same activity name, geography, product and unit (and ignoring ecoinvent rows that do not match anything)
print('Matching data...')
merged=pd.merge(left=background_data_sheet,right=ecoinvent_redux,how='inner',left_on=[activity_name2,geography2,ref_product2,unit2],right_on=['Activity Name','Geography','Reference Product Name','Reference Product Unit'])

# We remove duplicate columns, and rename the new column with data on ecosystem quality (coming from ecoinvent). It replaces the "old" data column in the tool, which held dummy data.
merged.pop('Activity Name')
merged.pop('Reference Product Name')
merged.pop('Reference Product Unit')
merged.pop(total_eco_qual2)
merged=merged.rename(columns={total_eco_qual:total_eco_qual2})

# Finally, we export the results into a separate spreadsheet. You can open it and copy the data you need into the spreadsheet tool.
print ('Exporting results...')
merged.to_excel(output_path,encoding='utf-8-sig')
print('Done!')
