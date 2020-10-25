import urllib
import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import json
import os


with open("converted_data.json") as f:
    data = json.load(f)

for i in data:
    url = data[i]["jobLink"]
    url = url.strip("\"")

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    description_soup = soup.find(id="jobDescriptionText")

print(url)
