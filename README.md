## Log Analysis Project

## Udacity Full Stack Nanodegree

###      Introduction


This is a python module that uses information of large database of a web server and draw business conclusions from that information. The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. The database includes three tables:

The **authors table** includes information about the authors of articles.

The **articles** table includes the articles themselves.

The **log table** includes one entry for each time a user has accessed the site.


### Assignment

1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3.  On which days did more than 1% of requests lead to errors? 



### How to run

change directory to vagrant directory then

**vagrant up** command to run the vagrant on vm

**vagrant ssh** to login into vm

change directory to vagrant

use command **psql -d news -f newsdata.sql** to load database

-use **\c** to connect to database="news"

-use **\dt** to see the tables in database

-use **\dv** to see the views in database

-use **\q** to quit the database

use command python **log_analysis.py** to run the program


### RESULT:

**THE TOP POPULAR ARTICLES ARE:**

Candidate is jerk, alleges rival--338647

Bears love berries, alleges bear--253801

Bad things gone, say good people--170098


**THE TOP POPULAR AUTHORS ARE:**

Ursula La Multa--507594

Rudolf von Treppenwitz--423457

Anonymous Contributor--170098

Markoff Chaney--84557


**DATE WHERE ERR_PERC MORE THAN 1.0 IS:**

2016-07-17--2.3 %     
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
