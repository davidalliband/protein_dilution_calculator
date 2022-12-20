# Import packages
import math
import pandas as pd

# Request CSV filename for use in calculations
TP_file = input("What is your CSV filename? ")

# Read in CSV and print
TP_data = pd.read_csv(f"{TP_file}")
print(TP_data)

# Calculate sample volumes for 20ug of protein and add to dataframe
TP_data["Sample_volume_ul"] = ([20000] / TP_data["Total_protein"])
print(TP_data)

# Calculate buffer volumes based on highest sample volume and add to dataframe
TP_data["Buffer_volume_ul"] = ([20000] / TP_data["Total_protein"])
print(TP_data)

# Calculate loading dye volume and add to dataframe
TP_data["Buffer_volume_ul"] = ([20000] / TP_data["Total_protein"])
print(TP_data)

# dilutions = list(dilutionsList)
# dilutionsDF = pd.DataFrame.from_dict(dilutions)
# display(dilutionsDF)
# dilutionsDF.to_csv("Export.csv")