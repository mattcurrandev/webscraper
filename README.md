## Table of contents

- [Overview](#overview)
- [My process](#my-process)
- [Author](#author)

## Overview
This project is a a webscraper that scrapes a table from the test 
website https://www.scrapethissite.com/pages/forms/. The program 
asks the user how many pages of the table they would like to scrape then 
in another for loop it puts the data into a excel sheet.

## My process
First I began with installing the necessary modules BeautifulSoup and os,
the next thing I did was assigned values to the variables html, soup, and teams.
The teams variable points to the table with all the teams using that I made a for loop
that goes through and only take the team name, year, win percent and plus minus from each
team. After that was done I realized that I would have to modify the url and html variables in
order to scrape from multiple pages. When that was done I added a prompt the takes the input 
of the number of pages the user would like to scrape. I took that number and used another for 
loop to take data from the pages requested. Once that was done I added it into an excel sheet
that gets all the data asked added to it. When openieng the excel sheet it may look like the 
first few fields are empty but they just need to be expanded.

## Author
Matt Curran