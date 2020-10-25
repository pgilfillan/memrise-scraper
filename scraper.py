import requests
import os
from bs4 import BeautifulSoup
import argparse

arg_parser = argparse.ArgumentParser(description='Memrise course scraper')
arg_parser.add_argument("course_url", type=str, help="URL of the course to scrape")
args = arg_parser.parse_args()

course_page = requests.get(args.course_url).content
soup = BeautifulSoup(course_page, "html.parser")
level_divs = soup.find_all("div", {"class": "level-index"})

file_string = b""
for level_div in level_divs:
    level_index = level_div.text
    level_page = requests.get(f"{args.course_url}/{level_index}").content
    soup = BeautifulSoup(level_page, "html.parser")
    
    col_a_rows = soup.find_all("div", {"class": "col_a"})
    col_b_rows = soup.find_all("div", {"class": "col_b"})
    for i in range(len(col_a_rows)):
        col_a_word = col_a_rows[i].findChild("div", {"class": "text"}).text
        col_a_word_bytes = col_a_word.encode("utf-8")
        col_b_word = col_b_rows[i].findChild("div", {"class": "text"}).text
        col_b_word_bytes = col_b_word.encode("utf-8")

        print(f"Column A: {col_a_word}. Column B: {col_b_word}")
        file_string = file_string + b"%s,%s\n" % (col_a_word_bytes, col_b_word_bytes)

with open("words.csv", "wb") as words_file:
    words_file.write(file_string)

