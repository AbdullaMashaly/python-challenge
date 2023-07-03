# python-challenge
## PyBank

This project involved creating a Python script to analyze financial records stored in a CSV file. The dataset, named **budget_data.csv**, consisted of two columns: "Date" and "Profit/Losses". The goal was to calculate several key values from the dataset, including the total number of months, the net total amount of "Profit/Losses" over the entire period, the changes in "Profit/Losses" over the period and the average of those changes, as well as the greatest increase and decrease in profits (along with their respective dates).

### To accomplish this, I followed the following steps:

1. Imported the necessary csv module to work with CSV files.
2. Read the budget_data.csv file using the csv.reader() function and stored the data in a list.
3. Calculated the total number of months by counting the rows in the dataset.
4. Calculated the net total amount of "Profit/Losses" by iterating through the dataset and summing the values.
5. Calculated the changes in "Profit/Losses" by iterating through the dataset and calculating the difference between each month's value and the previous month's value. Stored these changes in a list.
6. Calculated the average change by summing the changes and dividing by the number of changes.
7. Found the greatest increase and decrease in profits by using the max() and min() functions on the changes list. Retrieved the corresponding dates for these values.
8. Printed the analysis results, including the total number of months, net total amount, average change, greatest increase in profits (along with its date), and greatest decrease in profits (along with its date).
9. Saved the analysis results to a text file named **analysis.txt**.

###Source code:

- To calculate the number of months using len https://www.w3resource.com/python-exercises/modules/python-module-csv-exercise-2.php
- To refer to a specific field of a CSV file https://stackoverflow.com/questions/5757743/how-can-i-get-a-specific-field-of-a-csv-file
- Sum Comprehension https://docs.sourcery.ai/Reference/Python/Default-Rules/sum-comprehension/
- Save a text file to a certain directory and adding text to it https://stackoverflow.com/questions/8024248/telling-python-to-save-a-txt-file-to-a-certain-directory-on-windows-and-mac