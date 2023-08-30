# doughnut-biotool
A tool to calculate a building project's impacts on biodiversity over the entire life cycle. The tool was developed as part of the "Doughnut for Urban Development" project and manual. For more information, visit https://www.home.earth/doughnut 

The tool calculates the project's impacts on ecosystems as a local loss of species. It takes into account impacts caused by the transformation and occupation of land on the building site (direct impacts), as well as the use of construction materials (indirect impacts).
The tool is best used in combination with the Biodiversity Metric tool from Natural England, which only covers local impacts but provides a more in-depth and comprehensive assessment: https://publications.naturalengland.org.uk/publication/6049804846366720  

This is a first attempt at making LCA-based biodiversity impact assessments more mainstream in the building sector - but it is far from perfect!
We are eagerly waiting for your comments and feedback after you have tried the tool.

Best of luck with your biodiversity impact assessments!

_______________________________________________________

Please note that the values for the environmental impact of various materials included in the tool are dummy values, included for illustration purposes.
They are not accurate values and should not be used to perform actual calculations in a project.
Your first step should be to replace these values with actual data from the Ecoinvent database, if you have an Ecoinvent license, or another reliable database.
You can find the Ecoinvent database at https://ecoinvent.org/
You can use the Python script "biotool_importer.py" to automatically extract all the values you need from the Ecoinvent database:
- First, download the biodiversity tool, preferably the "detailed version" from https://www.home.earth/doughnut
- Download the Ecoinvent Excel file named "Cut-off cumulative LCIA v3.9.1.xlsx" from https://ecoquery.ecoinvent.org
- Make sure you have Python v3.10 or later installed, as well as the Pandas package: https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html
- Edit the "biotool_importer.py" file to replace the file paths with the right paths for the biodiversity tool, the ecoinvent Excel file, and the path where
you want the script to write the data.
- Run the Python script! You should get an Excel file that replicates the table found in the "Background_env_data" tab of the biodiversity tool, but with the 
right values instead of dummy values. The file can be found at the writing location you indicated at the previous step.

_______________________________________________________

CHANGELOG:

v1.1: 
- Corrected wrong Geography value for "market for aluminium, cast alloy" in the background data.
- Corrected wrong or missing density values in the background data (density values in that table are not used in calculations).
- Added two missing products in the simple version of the tool (hard fibreboard and gypsum fibreboard).
- Added the biotool_importer Python script.
