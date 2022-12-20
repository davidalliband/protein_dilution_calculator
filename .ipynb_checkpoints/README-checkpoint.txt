PROTEIN DILUTION CALCULATOR FOR WESTERN BLOT

To use this tool you must format your CSV file correctly. Column A should contain your samples (e.g. Sample 1, Sample 2, Sample 3, etc.) and Column B should contain the total protein of the sample. This will be used to calculate the volume of each Sample required to create a final dilution containing your desired quantity of protein. An example CSV file is included with this tool (BCA_example.csv).

To run the script, open the terminal and change directory to the folder in which the script is located. Enter "python western_dilution_calculator.py" in the terminal and hit return.

You will then be prompted to enter a series of values, such as the filepath of your CSV datafile, total protein volume, dilution factor, etc. These will be used to calculate how much of your protein sample, buffer, and loading dye should be combined to create your desired final solution concentration.

Finally, you will be asked to enter the desired filename for your new CSV file containing all the new data which will be exported to the same folder as the script.