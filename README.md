# Sequencing Data Extract

## Here are the steps to use this code:

* Copy the attached Data_Extract.py to a folder.
* Download the summary.json file from read_aligner folder and move it to the same folder as the python code.
* Download the  Active_sensors_boxplot_stats.csv from sign_filter folder, rename it to SNR.csv and move it to the same folder as the python code.
* Run the python code by executing > python Data_Extract.py
* It will generate a csv file named seq_stats.csv in the same folder.
* Open the csv file and copy all the data and paste as value only in the desired row of the G4 Optimization results (I rearranged the columns to make this process easier).

*summary.json, SNR.csv, & seq_stats.csv have been provided as an example for what the files should look like*


## Potential Errors:
### Make sure you close seq_stats.csv - Python cannot write to a file that is open/being used
### Make sure you downloaded the correct CSV file. If you get a list index error, you may be using the wrong CSV file
### Make sure csv is renamed to SNR.csv, NOT SNR.csv.csv. A name of SNR is ok if the filetype is .csv
### When you copy the summary.json to save locally make sure you ONLY copy the JSON portion and NOT HTML from the web browser
### Always download the most up to date code from Github