# Memrise Course Scraper

Python script for scraping all words from a Memrise course and writing them to a CSV file. 

## Usage

With Python installed:

```
pip install -r requirements.txt
python scraper.py <Course URL>
```

You can copy the course URL after selecting the course on [https://app.memrise.com]. Example: [https://app.memrise.com/course/150816/howtostudykoreancom-unit-1-2/].

## Planned Additions

* Output the list to a more readable web-app rather than a CSV file
* Extra features on the web-app, e.g. search, sorting, practice features
* Use session cookies from the web browser to obtain user specific information (so that for example you can filter for words you've learned, rather than all words in the course)