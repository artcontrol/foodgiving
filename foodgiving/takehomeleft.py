#!/usr/bin/env python
# coding: utf-8

# Take Home Left
# 
# controller for food leftovers. python functions.

# In[54]:


import sqlite3
import arrow
from passlib.apps import custom_app_context as pwd_context


# In[66]:


def createReviewDB(namedb):
    conn = sqlite3.connect('{}.db'.format(namedb))
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE reviews (myid integer, forid integer, foodid integer, rating integer, comments text, datetime text)''')

    


# In[70]:


def createReview(myid, forid, idfood, rating, comments):
    timnow = arrow.utcnow()
    
    #str(timnow.datetime)
    
    conn = sqlite3.connect('foodentry.db')
    c = conn.cursor()
    c.execute("INSERT INTO reviews VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(myid, forid, idfood, rating, 
                                                                              comments, 
                                                                              str(timnow.datetime)))
    
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


# In[75]:


def lookupReviews():
    conn = sqlite3.connect('foodentry.db')
    c = conn.cursor()
    allfod = c.execute('SELECT * FROM reviews')
    return(allfod.fetchall())
    
    


# In[77]:


def lookupMyReviews(myid):
    conn = sqlite3.connect('foodentry.db')
    c = conn.cursor()
    allfod = c.execute('SELECT * FROM reviews WHERE myid OR forid = {}'.format(myid))
    return(allfod.fetchall())


# In[78]:


#LookupMyReviews(1)


# In[ ]:





# In[71]:


#createreviewdb('foodentry')


# In[72]:


#createreview(1, 2, 5, 'super good food')


# In[76]:


#loopupreviews()


# In[ ]:





# In[ ]:


def createUserDB(namedb):
    conn = sqlite3.connect('{}.db'.format(namedb))
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE users
             (email text, password text, userid integer, image text, name text, location text)''')

    


# In[ ]:


def createUser(email, password, image, name, location):
    conn = sqlite3.connect('foodentry.db')
    c = conn.cursor()
    hashpass = pwd_context.hash(password)

    c.execute("INSERT INTO users VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(name, 
                                                                              hashpass, returnCountUsers() + 1, image, 
                                                                              name, 
                                                                              location))
    
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
    returnCountUsers()


# In[35]:


def createFoodDB(namedb):
    conn = sqlite3.connect('{}.db'.format(namedb))
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE foods
             (name text, foodid integer, image text, datecook text, dateexpire text, 
             ingredients text, location text, myid integer)''')

    


# In[36]:


def makeFoodEntry(name, image, datecooked, expiredate,
                 ingredients, location, myid):
    conn = sqlite3.connect('foodentry.db')
    c = conn.cursor()
    c.execute("INSERT INTO foods VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(name, 
                                                                              returnCountFood() + 1, image, 
                                                                              datecooked, 
                                                                              expiredate, ingredients, location, myid))
    
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

    return({'name' : name, 'foodid' : returnCountFood() + 1, 'image' : image, 'datecooked' : datecooked,
           'expiredate' : expiredate, 'ingredients' : ingredients, 'location' : location, 'myid' : myid})


# In[37]:


def returnFoods():
    conn = sqlite3.connect('foodentry.db')
    c = conn.cursor()
    allfod = c.execute('SELECT * FROM foods')
    return(allfod.fetchall())
    


# In[38]:


def returnCountFood():
    conn = sqlite3.connect('foodentry.db')
    c = conn.cursor()
    allfod = c.execute('SELECT count(*) FROM foods')
    return(allfod.fetchall()[0][0])
    


# In[82]:


def returnCountUsers():
    conn = sqlite3.connect('foodentry.db')
    c = conn.cursor()
    allfod = c.execute('SELECT count(*) FROM users')
    return(allfod.fetchall()[0][0])


# In[81]:


#returncountusers()


# In[83]:


def returnUsers():
    conn = sqlite3.connect('foodentry.db')
    c = conn.cursor()
    allfod = c.execute('SELECT * FROM users')
    return(allfod.fetchall())
    


# In[ ]:


def returnReviews():
    conn = sqlite3.connect('foodentry.db')
    c = conn.cursor()
    allfod = c.execute('SELECT * FROM reviews')
    return(allfod.fetchall())
    


# In[ ]:





# In[46]:


#returncountfood()


# In[49]:


def filterFoods(searchfood):
    conn = sqlite3.connect('foodentry.db')
    c = conn.cursor()
    allfod = c.execute('SELECT * FROM foods WHERE foodid = {}'.format(searchfood))
    return(allfod.fetchall())
    


# In[ ]:





# In[52]:


#filterfoods(2)


# In[ ]:





# In[40]:


def makeFoodRequest(whatfood):
    return('you requested {}'.format(whatfood))


# In[41]:


#createfoodb('foodentry')


# In[44]:


#makefoodentry('pasta', 'me.com/img.png', '04/12/1999', '06/12/1999',
#                 'pork, pasta')


# In[45]:


#returnfoods()


# donatefood/
# 
# food info:
# 
# type: 
# 
# classification: 
# 
# quantity
# 
# expiration
# 
# description
# 
# Donate details: 
# 
# name:
# 
# rating: 
# 
# location:
# 
# pickup detail:
# 
# pickupby:
# 
# details:
# 
# pickfood:
# 
# foodtype: (type of food, ie fruit, vege or meat)
# 
# further classification apple, cabbage, meat.
# 
# all food.
# 
# enter location:
# 
# 
# 

# In[ ]:





# In[ ]:




