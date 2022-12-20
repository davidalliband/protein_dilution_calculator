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
TP_data["Sample_volume_replicate"] = (TP_data["Dilution_factor"] / TP_data["Total_protein"])
print(TP_data)

# Calculate ug of protein and add to dataframe
TP_data["Sample_protein_quantity"] = (TP_data["Dilution_factor"] / TP_data["Total_protein_volume"])
print(TP_data)

# Request total solution quantity required
TP_data["Total_solution_replicate"] = int(input("What is your desired total volume per replicate in ul? "))

# Request loading dye fraction required
TP_data["Loading_dye_fraction"] = int(input("What is your desired loading dye fraction? (e.g. for a 1 in 5 dilution enter 5) "))

# Calculate loading dye volume and add to dataframe
TP_data["Loading_dye_volume_replicate"] = (TP_data["Total_solution_replicate"] / TP_data["Loading_dye_fraction"])
print(TP_data)

# Calculate buffer volumes based on total desired volume minus sample and loading dye volumes and add to dataframe
TP_data["Buffer_volume_replicate"] = (TP_data["Total_solution_replicate"] - (TP_data["Loading_dye_volume_replicate"] + TP_data["Sample_volume_replicate"]))
print(TP_data)

# Request number of replicates required
TP_data["Replicates"] = int(input("What is your desired number of replicates? "))

# Calculate total solution volume for number of replicates
TP_data["Total_solution_total"] = (TP_data["Total_solution_replicate"] * TP_data["Replicates"])
print(TP_data)

# Calculate total sample volume for number of replicates
TP_data["Sample_volume_total"] = (TP_data["Sample_volume_replicate"] * TP_data["Replicates"])
print(TP_data)

# Calculate total buffer volume for number of replicates
TP_data["Buffer_volume_total"] = (TP_data["Buffer_volume_replicate"] * TP_data["Replicates"])
print(TP_data)

# Calculate total sample volume for number of replicates
TP_data["Loading_dye_volume_total"] = (TP_data["Loading_dye_volume_replicate"] * TP_data["Replicates"])
print(TP_data)

# Tidy up dataframe by reordering columns
TP_data = TP_data.reindex(columns=["Content", "Total_protein", "Total_protein_volume", "Dilution_factor", "Sample_protein_quantity", "Loading_dye_fraction", "Total_solution_replicate", "Sample_volume_replicate", "Buffer_volume_replicate", "Loading_dye_volume_replicate", "Replicates", "Total_solution_total", "Sample_volume_total", "Buffer_volume_total", "Loading_dye_volume_total"])

# Tidy up dataframe by renaming columns
TP_data.set_axis(["Content", "Total protein", "Total protein volume (ul)", "Dilution factor", "Sample protein quantity per replicate (ug)", "Loading dye fraction", "Total solution per replicate (ul)", "Sample per replicate (ul)", "Buffer volume per replicate (ul)", "Loading dye per replicate (ul)", "Number of replicates", "Total solution volume (ul)", "Total sample volume (ul)", "Total buffer volume (ul)", "Total loading dye volume (ul)"], axis='columns', inplace=True)

# Request name for CSV export
CSV_export = input("Name your CSV file export (do not include .csv in filename): ")

# Export dataframe as a CSV
TP_data.to_csv(f"{CSV_export}.csv")