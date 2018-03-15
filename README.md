
# Introduction
In this project we analyse a big database with a lot of data and output som useful information from it. Here we output the following 3 statistics.
- Top 3 articles.
- Author popularity.
- Days with more than 1% of errors..

This is all done with the use of views for simplifying our queries in our python file. \
An example of the programs output can be found in `output_example.txt`.

# Requirements
- Vagrant
- Download the sql data and unzip it into the project folder. [download link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

# Installment and running
- For running this project simply run the `vagrantfile` with `vagrant up`. 
- Then SSH into the vagrant box `vagrant ssh` and run `psql -d news -f /vagrant/newsdata.sql` for migrating and seeding the database. 
- Now we need to add our view which can be found in section views.
- Lastly we need to run the `analysis.py` file. In our ssh connecting to the vagrant box run `python /vagrant/analysis.py` and you should see the output. (You might have to change the password and username for the postgres database in the `analysis.py` file.)

# Views
The project uses views for the statistical data, these are the 3 views it requires.

The first view is for getting articles with page views ordered by how popular they are.

```
CREATE VIEW articles_popularity AS
  SELECT
    title,
    count(*) as views
  FROM
    articles
  JOIN log ON path = '/article/' || articles.slug
  GROUP BY articles.id
  ORDER BY views DESC;
```

The second view is for getting authors with how many views they have gotten, also ordered by the most popular author first.

```
CREATE VIEW author_popularity AS
  SELECT
    name,
    count(*) as views
  FROM
    authors
  JOIN articles a ON authors.id = a.author
  JOIN log l ON l.path = '/article/' || a.slug
  GROUP BY authors.id
  ORDER BY views DESC;
```

The last view is for seeing the percentage of request errors grouped by days. This is also ordered so the day with most errors is first.

```
CREATE VIEW errors_by_day AS
  SELECT
    to_char(DATE(log.time), 'FMMonth DD, YYYY') as date,
    round( count(*) FILTER (WHERE log.status != '200 OK') / count(*)::DECIMAL * 100, 2) as error_percentage
  FROM log
  GROUP BY DATE(log.time)
  ORDER BY error_percentage DESC;
```