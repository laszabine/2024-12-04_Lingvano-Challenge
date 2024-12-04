# 3-hour take-home challenge for my job application to Lingvano as data analyst

## Task 1: Ingestion

Start up a Postgres Docker container with `start-db.sh`. 
I have put a random password in plaintext in multiple locations: in the interest of time, and because credential management was not asked for this challenge. 

Execute `init.sql` to set up the tables. 

Then run the script `01-ingestion.py` to fill the tables with data from the CSV file. 

I have decided to work with 4 tables: `customers`, `products`, `orders`, and `subscriptions`.
I'm unsure about how to handle subscriptions from the given data alone. 
I have tentatively assumed that subscriptions are their own entity, with a given ID, and that they are associated with an email address. 

It has taken me 2 hours already to set up docker, the database, and get the data from the CSV into Postgres. 

## Task 2: Clean up

I am deciding to skip this step, in the interest of time. 
You're welcome to ask me about it. 

## Task 3: Insights 

See `03-insights.ipynb`. 

## Task 4: Visualization

## Task 5: Additional questions



