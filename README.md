# Logs Analysis
This project is about to a fictional newspaper. It's an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The tool gives to the team answers for the following questions: 
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors? 

The database includes three tables:
* The **authors** table includes information about the authors of articles.
* The **articles** table includes the articles themselves.
* The **log** table includes one entry for each time a user has accessed the site.

## Instructions
* <h4>**Previous requeriments**</h4>
It is necessary install Python 2.7 and Postgresql to run this project. 
* <h4>**Steps**</h4>
1. Install <a href="https://www.vagrantup.com/">Vagrant</a> and <a href="https://www.virtualbox.org/wiki/Downloads">VirtualBox.</a>
2. **Start the virtual machine.** From your terminal, inside the project directory, run `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. 
3. **Log in the virtual machine.** From your terminal, inside the project directory, run `vagrant ssh`. 
4. **Unzip the database.** Unzip newsdata.zip inside the project directory.
5. **Setup the database.** To load the database use the following command:
  <pre>psql -d news -f newsdata.sql;</pre>
6. **Make views.** Run this queries on the terminal to make views.
```sql
CREATE OR REPLACE VIEW articles_view AS
SELECT title, count(*) AS views
FROM articles, log
WHERE articles.slug=substring(log.path FROM 10)
GROUP BY articles.title
ORDER BY views DESC
```
```sql
CREATE OR REPLACE VIEW authors_articles AS
SELECT authors.name, articles.title 
FROM articles, authors
WHERE articles.author=authors.id
```
```sql
CREATE OR REPLACE VIEW most_pop_author AS
SELECT authors_articles.name, SUM(articles_views.views) AS sum
FROM authors_articles, articles_views
WHERE articles_views.title=authors_articles.title
GROUP BY authors_articles.name
ORDER BY sum DESC
```
```sql
CREATE OR REPLACE VIEW error_requests AS 
SELECT to_char(time, 'Month DD, YYYY') AS date, status, count(*) AS errors
FROM log 
WHERE status!='200 OK'
GROUP BY date, status
ORDER BY date ASC;
```
```sql
CREATE OR REPLACE VIEW total_requests AS
SELECT to_char(time, 'Month DD, YYYY') AS date, count(*) AS total 
FROM log 
GROUP BY date 
ORDER BY date ASC;
```
```sql
CREATE OR REPLACE VIEW log_status AS
SELECT error_requests.date, ROUND(((error_requests.errors*100)/total_requests.total::NUMERIC), 2) AS error_rate 
FROM error_requests, total_requests 
WHERE error_requests.date=total_requests.date 
ORDER BY date ASC;
```
7. **Run the command.**
  <pre>python newsdata.py</pre> 



