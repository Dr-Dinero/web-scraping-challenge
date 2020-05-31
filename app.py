#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template
from flask_pymongo import PyMongo
import mission_to_mars


# In[3]:


app = Flask(__name__)


# In[4]:


app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# In[ ]:


@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("my_index.html", mars=mars)


@app.route("/mars_scrape")
def run():
    find = mongo.db.find
    data = mission_to_mars.scrape()
    return "Scraping Successful!"


if __name__ == "__main__":
    app.run()






