
# coding: utf-8

# # Week 3 Assessment - Habiba Sarhan

# # User Case story (Customer)
# ### The system should welcome me as a user
# ### The system should ask me to submit a complaint
# ### The system should tell me when my complain is submitted

# In[1]:


complaint_bank = {}

def submit_complaints():
    runtime = True 
    print("Welcome to our customer satisfaction Unit!")
    while runtime:
        checker = int(input("Welcome to our customer satisfaction Unit! Press 0 to submit a complaint and 1 to exit:"))
        if checker == 0:
            name = input("Please enter your name:  ")
            complaint = input("Please submit your complaint:")
            print("Thank you, your complaint has been submitted successfully and our team will process it within three working days! ")
            print('==========================')
            complaint_bank[name] = {complaint}

        else:
            runtime = False 
            print("Thank you for visiting our website. Have a wonderful day!")
            
            print("Complaint submiited sofar")
            print(complaint_bank)
            
submit_complaints()


# ## User Case Story (Team) 

# ### List and pick Complaints

# In[2]:


print(complaint_bank)


# In[3]:


name = input("Please enter the complaint name:")
if name in complaint_bank:
    print(complaint_bank[name])
else: 
    print("Not found")


# ### Detect Complaint

# In[4]:


import requests
from urllib.parse import quote

def detect_langauge(text):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"
    payload = "q=" + quote(text)
    
    headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "6464df7f3dmsh79109d96d292f30p1d2e4cjsn32767b241ca1",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    
    return(response.text)


name = input("Please enter the complaint name:")
if name in complaint_bank:
    complain_string = list(complaint_bank[name])[0]
    print(complain_string)
    print(detect_langauge(complain_string))
else:
    print("Not found")


# ### Convert the string into json and get only the language as the output

# In[62]:


import json


# In[63]:


complaints_json = json.loads('{"data":{"detections":[[{"language":"en","isReliable":false,"confidence":0.8180167078971863}]]}}')


# In[64]:


complaints_json


# In[65]:


complaints_json["data"]


# In[66]:


complaints_json["data"]["detections"]


# In[67]:


complaints_json["data"]["detections"][0]


# In[68]:


complaints_json["data"]["detections"][0][0]


# In[69]:


complaints_json["data"]["detections"][0][0]["language"]


# ### Enhanced version of language detection
# 

# In[22]:


import requests
import json 
from urllib.parse import quote

def detect_langauge(text):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"
    payload = "q=" + quote(text)
    
    headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "6464df7f3dmsh79109d96d292f30p1d2e4cjsn32767b241ca1",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    response_text = response.text
    complaints_json = json.loads(response_text)
    detected_language = complaints_json["data"]["detections"][0][0]["language"]
    return(detected_language)


name = input("Please enter the complaint name:")
if name in complaint_bank:
    complain_string = list(complaint_bank[name])[0]
    #print(complain_string)
    #complaints_json = json.loads(detect_langauge(complain_string))
    #print(complaints_json)
    # print(detect_langauge(complaints_json))
    #print("The language detected is.....")
    #print(complaints_json["data"]["detections"][0][0]["language"])
    #print(detect_langauge(complain_string))
else:
    print("Not found")


# ### Translate Complaint 

# In[29]:


import requests
from urllib.parse import quote

def translate_langauge(text, target_language):
    
    source_language = detect_langauge(text)
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    # payload = "q=Hello%2C%20world!&target=es&source=en"
    payload = "q=" + quote(text) + "&target=" + target_language + "&source=" + source_language
    
    headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "6464df7f3dmsh79109d96d292f30p1d2e4cjsn32767b241ca1",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text


# result = translate_langauge("good morning", "es")


name = input("Please enter the complaint name:")
if name in complaint_bank:
    complain_string = list(complaint_bank[name])[0]
    translated_object = json.loads(translate_langauge(complain_string, "de"))
    translation = translated_object["data"]["translations"][0]["translatedText"]
    print(translation)
else:
    print("Not found")

