# PROTEIN DILUTION CALCULATOR FOR WESTERN BLOT
## Created by David Alliband (University of Bristol & UWE Bristol)

*This repository can be found at https://github.com/davidalliband/protein_dilution_calculator*

This tool uses Python to quickly calculate the volumes to be combined from various total protein solutions (such as a BCA assay) to create a solution containing a constant protein quantity with buffer and loading dye.

To use this tool you must format your CSV file correctly. Column A should contain your samples (e.g. Sample 1, Sample 2, Sample 3, etc.) and be entitled "Content". Column B should contain the total protein of the sample in ug and be entitled "Total_protein". This will be used to calculate the volume of each Sample required to create a working solution containing your desired quantity of protein. An example CSV file is included with this tool (BCA_example.csv) with six samples with varying quantities of total protein in mg per ml.

**To use this tool:**

1. Download all the contents of this repository including the script and example data into a single directory.
2. Open the terminal and change directory to the folder in which the script is located.
3. Enter "python western_dilution_calculator.py" in the terminal and hit return.

**The script will then prompt you to enter certain information:**

1. The filepath of your data CSV. If the file is located in the same directory then simply enter the filename. For example, using the example data you would enter "BCA_example.csv".
2. The volume of your total protein value in ul. For example, if your total protein is in mg per ml then enter 1000.
3. Dilution factor of your working solution. For example, if calculating from mg per ml then 20000 would give 20ug of protein and 15000 would give 15ug of protein.
4. Total solution volume in ul per replicate, for example, 35.
5. Desire loading dye fraction. For example, for a 1 in 5 dilution enter "5".
6. How many replicates you wish to create a working solution for.

Finally, you will be asked to enter the a filename for your new CSV file containing all the new data which will be exported to the same folder as the script.

## Calculations performed by the script

This script performs a number of calculations in order to give the required volumes for the working solution. These are as follows:

1. Sample volume to pipette per replicate to give the desired protein quantity = Dilution factor / Total protein
2. Loading dye volume to pipette per replicate = Total solution volume per replicate / Loading dye fraction
3. Buffer volume to pipette per replicate = Total solution volume per replicate / (Loading dye volume per replicate + Sample volume per replicate)
4. Total solution volume = Number of replicates x Total volume per replicate
5. Total sample volume to pipette = Number of replicates x Sample volume per replicate
6. Total buffer volume to pipette = Number of replicates x Buffer volume per replicate
7. Total loading dye volume to pipette = Number of replicates x Loading dye volume per replicate