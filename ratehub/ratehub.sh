#!/usr/bin/sh

rm output.csv # Remove old output
scrapy crawl mortgage-rate -o output.csv > /dev/null 2>&1 # Generate csv, hide all the scrapy messages
python clean.py # Run the pandas python script
