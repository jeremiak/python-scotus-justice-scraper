# Quick Python -> JSON scraper for SCOTUS Justices

## Because doing it in R is super hard


This is a pretty simple script, it just takes the tabular data for (SCOTUS Justices from the Wikipedia page)[http://en.wikipedia.org/wiki/List_of_Justices_of_the_Supreme_Court_of_the_United_States] and generates a `justices.json` representation of the same data for use with other scripts

### Usage

This is a python script but comes with a make file so all you *should* have to do to generate a file is:
`make scrape`

`make scrape` should install the dependencies using `pip` and then run the script