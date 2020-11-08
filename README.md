# Rocket Regression: Exploratory and Predictive Analysis of Rocket Launch Success

## Overview

In this project, I am looking at rocket launches and how primarily non-technical factors correlate with mission outcome. I scrape data from nextspaceflight.com and analyze variables to determine which have correlations with success. I then implement a logistic regression model to try and predict future launches, and I test the accuracy and reliability of such a model. To get started, open **analysis.ipynb** and follow along!

## Files

**webscraper.py** Contains functions for scraping data off nextspaceflight.com
**processing.py** Contains functions for formatting and visualizing the data
**launches.csv** Contains the data from nextspaceflight.com as a csv 
**analysis.ipynb** Contains the computational essay, integrating functions from previous files
**test_processing.py** Runs pytests on processing.py to make sure all functions work properly

## Dependencies

**Conda Python**
Conda is the only required install for this project, and you can find it here:
https://docs.conda.io/projects/conda/en/latest/user-guide/install/ 

**All other dependencies come with conda python, but are also listed below**

numpy  
copy  
pandas  
BeautifulSoup (from bs4)  
requests  
Pyplot (from Matplotlib)  
lxml  
scikit  
seaborn

## Reproducibility

This code is designed specifically to scrape data from nextspaceflight.com, and so will not immediately work with other sites. The main hardcoded portions are the beautifulsoup extraction, and the dataframe headers and formatting. However, is it entirely possible to modify this code for use with other sites.
