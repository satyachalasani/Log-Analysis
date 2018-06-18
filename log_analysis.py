##! /usr/bin/env
"""PROJECT:-LOG ANALYSIS"""
import psycopg2
from datetime import date


def connect():
    return psycopg2.connect("dbname=news")


def executeQuery(query):
    """executeQuery takes a string as a parameter.  It executes the query
    and returns the results as a list of tuples."""
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


query1 = """
select title, count(*) as views from articles inner join
log on concat('/article/', articles.slug) = log.path
where log.status = '200 OK'
group by log.path, articles.title order by views desc limit 3
"""


query2 = """
select authors.name, count(*) as views from articles inner join
authors on articles.author = authors.id inner join
log on concat('/article/', articles.slug) = log.path where
log.status = '200 OK' group by authors.name order by views desc
"""


query3 = """
select Date,(Error::float*100)/Total::float as Percent from
(select time::timestamp::date as Date, count(status) as Total,
sum(case when status = '404 NOT FOUND' then 1 else 0 end) as Error from log
group by time::timestamp::date) as result
where (Error::float*100)/Total::float > 1.0 order by Percent desc;
"""


def popular_article(query1):
    db = connect()
    c = db.cursor()
    c.execute(query1)
    results = c.fetchall()
    for i in range(len(results)):
        title = results[i][0]
        views = results[i][1]
        print("%s--%d" % (title, views))
    db.close()


def popular_authors(query2):
    db = connect()
    c = db.cursor()
    c.execute(query2)
    results = c.fetchall()
    for i in range(len(results)):
        name = results[i][0]
        views = results[i][1]
        print("%s--%d" % (name, views))
    db.close()


def error_percent(query3):
    db = connect()
    c = db.cursor()
    c.execute(query3)
    results = c.fetchall()
    for i in range(len(results)):
        date = results[i][0]
        percent = results[i][1]
        print ("%s--%.1f %%" % (date, percent))


if __name__ == "__main__":
    print("THE TOP POPULAR ARTICLES ARE:")
    popular_article(query1)
    print("\n")
    print("THE TOP POPULAR AUTHORS ARE:")
    popular_authors(query2)
    print("\n")
    print("DATE WHERE ERR_PERC MORE THAN 1.0 IS:")
    error_percent(query3)
