#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import pandas as pd
import numpy as np
import sqlalchemy
import sqlite3
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser


# In[34]:

def scrape():
    scrape_info = {
        "TITLE": title,
        "PARAGRAPH": para,
        "_image": featured_image_url,
        "hemispheres": hemisphere_url,
        "WEATHER": mars_weather,
        "facts": mars_facts(),
    }

   
    return scrape_info



executable_path = {'executable_path': '/Users/users/opt/chromedriver_1'}


# In[36]:


browser = Browser('chrome', **executable_path, headless=False)


# In[28]:


url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"


# In[29]:


link_soup = bs(link_response.text, 'html.parser')


# In[30]:


link_response = requests.get(url)


# In[14]:


driver = webdriver.Chrome('/Users/users/opt/chromedriver_1')


# In[31]:


browser = driver.get('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')


# In[18]:


url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"


# In[41]:


img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"


# In[42]:


browser.visit(img_url)


# In[43]:


html = browser.html
browse_soup = bs(html, 'html.parser')


# In[44]:


img_response = requests.get(img_url)


# In[45]:


img_soup = bs(img_response.text, 'html.parser')


# In[58]:


print(img_soup.prettify())


# In[68]:


img_find = img_soup.find_all('a', class_= '')


# In[69]:


print(img_find)


# In[19]:


link_response = requests.get(url)


# In[5]:


"https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA18289_ip.jpg"


# In[20]:


link_soup = bs(link_response.text, 'html.parser')


# In[21]:


print(link_soup.prettify())


# In[22]:


title = link_soup.title.text


# In[24]:


para = link_soup.p.text


# In[23]:


TITLE = print(title)


# In[25]:


PARAGRAPH = print(para)


# In[ ]:


featured_image_url = "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA23929_hires.jpg"


# In[70]:


twitter = "https://twitter.com/marswxreport?lang=en"


# In[71]:


twitter_response = requests.get(twitter)


# In[72]:


twitter_soup = bs(twitter_response.text, 'html.parser')


# In[73]:


print(twitter_soup.prettify())


# In[1]:


mars_weather = 'sol 530 (2020-05-23) low -92.6ºC (-134.7ºF) high 0.4ºC (32.7ºF) winds from the SW at 4.7 m/s (10.6 mph) gusting to 17.4 m/s (38.9 mph)pressure at 7.10 hPa'


# In[4]:


mars_facts_url = "https://space-facts.com/mars/"
pandas_table = pd.read_html(mars_facts_url)
pandas_table


# In[9]:


clean_pandas = pandas_table[0]
clean_pandas.columns = ['Mars','Earth']
clean_pandas.head()


# In[13]:


pandashtml = clean_pandas.to_html()
pandashtml


# In[1]:
hemisphere_url = [
    {"title": "Cerberus Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Valles Marineris Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
]


browser.quit()



get_ipython().system('jupyter nbconvert --to script mission_to_mars.ipynb')


# In[ ]:





# In[ ]:




