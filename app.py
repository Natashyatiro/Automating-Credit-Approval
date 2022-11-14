#!/usr/bin/env python
# coding: utf-8

# In[33]:


from flask import Flask, render_template, request


# In[34]:


import joblib


# In[39]:


app = Flask(__name__) 


# In[40]:


@app.route("/", methods = ["GET", "POST"])

def index():
    if request.method == "POST":
        income = float(request.form.get("income"))
        age = float(request.form.get("age"))
        data = [income, age]
        model1 = joblib.load("rf") 
        pred1 = model1.predict([data])
        print(data)
        print(pred1)
        data.append(pred1[0])
        model2 = joblib.load("gboost") 
        pred2 = model2.predict([data])
        
        print(pred2)
        
        return(render_template("index.html", result1 = pred1, result2 = pred2))
    else:
        return(render_template("index.html", result1 = "Waiting", result2 = "Waiting"))


# In[41]:


if __name__ == "__main__":
    app.run()

