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

## Pypoll

The goal was to analyze a given set of poll data and calculate various values related to the election. The dataset provided was in **election_data.csv**, containing three columns: "Ballot ID", "County", and "Candidate". The Python script performs the following analysis on the dataset:

1. Total number of votes cast: The script counts the number of rows in the dataset to determine the total number of votes.

2. Complete list of candidates who received votes: The script extracts the unique candidate names from the dataset and stores them in a list.

3. Total number of votes each candidate won: The script counts the votes received by each candidate.

4. Percentage of votes each candidate won: The script calculates the percentage of votes won by each candidate by dividing their votes by the total number of votes and multiplying by 100.

5. Winner of the election based on popular vote: The script determines the candidate with the highest number of votes and declares them as the winner.

6. The analysis results, including the total votes, percentage of votes, and the winner, are printed in the terminal and was saved to a text file named **analysis.txt** 

### Source code:

- To calculate the number of months using len https://www.w3resource.com/python-exercises/modules/python-module-csv-exercise-2.php
- To refer to a specific field of a CSV file https://stackoverflow.com/questions/5757743/how-can-i-get-a-specific-field-of-a-csv-file
- Sum Comprehension https://docs.sourcery.ai/Reference/Python/Default-Rules/sum-comprehension/
- Save a text file to a certain directory and adding text to it https://stackoverflow.com/questions/8024248/telling-python-to-save-a-txt-file-to-a-certain-directory-on-windows-and-mac
- Python Dictionary Comprehension https://rowannicholls.github.io/python/advanced/dictionaries.html
- Finding the Key of Max Value in a Nested Dictionary https://www.javatpoint.com/find-key-with-maximum-value-in-dictionary#:~:text=Using%20max()%20Function,it%20functions%20with%20a%20list.
- How to Add New Line in Python f-strings https://towardsdatascience.com/how-to-add-new-line-in-python-f-strings-7b4ccc605f4a#:~:text=Instead%2C%20you%20have%20to%20use,corresponds%20to%20a%20Unicode%20character.
