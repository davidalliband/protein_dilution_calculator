# Import packages
import math
import pandas as pd

# Request CSV filename for use in calculations
TP_file = input("Enter your CSV filepath: ")

# Read in CSV and print
TP_data = pd.read_csv(f"{TP_file}")
print(TP_data)

# Request original volume of total protein
TP_data["Total_protein_volume"] = int(input("What is your total protein volume in ul? (e.g. for protein per ml enter 1000 or for per 500ul enter 500) "))

# Request dilution factor for use in calculations
TP_data["Dilution_factor"] = int(input("What is your dilution factor? (e.g. if calculating from protein per ml then use 20000 for 20ug of protein or 15000 for 15ug of protein) "))

# Calculate sample volumes for desired amount of protein and add to dataframe
TP_data["Sample_volume_ul"] = (TP_data["Dilution_factor"] / TP_data["Total_protein"])
print(TP_data)

# Calculate ug of protein and add to dataframe
TP_data["Sample_protein_quantity"] = (TP_data["Dilution_factor"] / TP_data["Total_protein_volume"])
print(TP_data)

# Request total solution quantity required
TP_data["Total_solution_ul"] = int(input("What is your desired total volume in ul? "))

# Request loading dye fraction required
TP_data["Loading_dye_fraction"] = int(input("What is your desired loading dye fraction? (e.g. for a 1 in 5 dilution enter 5) "))

# Calculate loading dye volume and add to dataframe
TP_data["Loading_dye_volume_ul"] = (TP_data["Total_solution_ul"] / TP_data["Loading_dye_fraction"])
print(TP_data)

# Calculate buffer volumes based on total desired volume minus sample and loading dye volumes and add to dataframe
TP_data["Buffer_volume_ul"] = (TP_data["Total_solution_ul"] - (TP_data["Loading_dye_volume_ul"] + TP_data["Sample_volume_ul"]))
print(TP_data)

# Tidy up dataframe by reordering columns
TP_data = TP_data.reindex(columns=["Content", "Total_protein", "Dilution_factor", "Sample_protein_quantity", "Loading_dye_fraction", "Total_solution_ul", "Sample_volume_ul", "Buffer_volume_ul", "Loading_dye_volume_ul"])

# Tidy up dataframe by renaming columns
TP_data.set_axis(["Content", "Total protein", "Dilution factor", "Sample protein quantity", "Loading dye fraction", "Total solution", "Sample volume", "Buffer volume", "Loading dye volume"], axis='columns', inplace=True)

# Tidy up dataframe by adding value measurements
# TP_data = TP_data.reindex(columns=["Content", "Total_protein", "Dilution_factor", "Sample_protein_quantity", "Loading_dye_fraction", "Total_solution_ul", "Sample_volume_ul", "Buffer_volume_ul", "Loading_dye_volume_ul"])

TP_data.to_csv("Export.csv")