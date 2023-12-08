# Python_Project_Group10



# DAB 111 - Python Final Project

### Group Members:

Group No. 10

Muhammad Usman 0825421
 
### Project Objective:

This project contains the usage of Python, Pandas, SQLite3, and Flask. Using Pandas, we are scarapping the data from website and stored in database using SQLite3 package. Flask is used to present stored data of database on web.
Website contains mainly 3 pages, Home, About Us, and Data. About Us page shows the details about dataset and defination of each variable. Movies page shows the data stored in database using SQLite3.


### Overview

This project aims to extract data from ESPNcricinfo's website utilizing Pandas for web scraping. The gathered data will be integrated into an SQLite database via the SQLite3 package. The resulting table will be visualized and categorized into two main sections: Batting Records and Bowling Records.

Batting Records: Includes statistics related to player performances while batting, such as runs scored, strike rates, centuries, and other relevant metrics.

Bowling Records: Encompasses statistics linked to bowlers' performances, including wickets taken, economy rates, bowling averages, and other pertinent data.

Utilizing Python's Pandas for web scraping, SQLite3 for database integration, and visualization tools to categorize, display the data by creating a website using HTML, CSS and FLASK. This project will facilitate a comprehensive understanding of cricketing data, specifically focusing on batting and bowling records.


### Source of Data

The dataset is sourced from Cricinfo Website and is named "Batting Records", "Bowling Records"

*Link to Source:*  [Batting Records]('https://www.espncricinfo.com/records/tournament/batting-most-runs-career/icc-cricket-world-cup-2023-24-15338')
				   [Bowling Records]('https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/icc-cricket-world-cup-2023-24-15338')

### Data Variables

## Example Usage
 ### Download required modules first:

 - Run command "pip install -r requirements.txt"
 - This will install all required packages for this project

 ### Run app Locally:

Step 1:
- Clone the project first or download zip of project and extract it
- Our 'cricket_records.db' file in Database Folder
Step 2:
 - If you not see 'cricket_records.db' file in Database directory, then open new terminal in 'Database' folder
 - Run "python_project.py" command, this will create new database file, create a table and insert data from The links provided for Cricinfo Website

Step 3:
 - Open 'terminal' or 'cmd' in root directory of the project
 - Run "python app.py" command
 - Go to http://127.0.0.1:5000
 - And explore the website