#!/usr/bin/env python
# coding: utf-8

# In[6]:


import takehomeleft


# In[ ]:


from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/createdb')
def createdb():
    nameofdb = request.args.get('nameofdb')
    #lenth = request.args.get('length')
    #ic.createdbtext(nameofdb)
    takehomeleft.createFoodDB(nameofdb)
    takehomeleft.createUserDB(nameofdb)
    takehomeleft.createReviewDB(nameofdb)

    return('{} database created!'.format(nameofdb))

@app.route('/createuser', methods=['GET', 'POST'])
def createuser():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        image = request.form.get('image')
        location = request.form.get('location')

        takehomeleft.createUser(email, password, image, name, location)
        return('created user {}'.format(email))
    return(render_template('user.html'))

@app.route('/createfood', methods=['GET', 'POST'])
def createfood():
    if request.method == 'POST':
        #name, image, datecooked, expiredate,
                 #ingredients, location, myid)

        name = request.form.get('name')
        image = request.form.get('image')
        datecooked = request.form.get('datecooked')
        expiredate = request.form.get('expiredate')
        ingredients = request.form.get('ingredients')
        location = request.form.get('location')
        myid = request.form.get('myid')


        takehomeleft.makeFoodEntry(name, image, datecooked, 
                                   expiredate, ingredients, location, myid)
        return('food created')
    return(render_template('createfood.html'))

#takehomeleft.createReview(1, 2, 1, 5, 'good foods')
@app.route('/createreview', methods=['GET', 'POST'])
def createreview():
    if request.method == 'POST':
        myid = request.form.get('myid')
        forid = request.form.get('forid')
        idfood = request.form.get('idfood')
        rating = request.form.get('rating')
        comments = request.form.get('comments')
        #def createReview(myid, forid, idfood, rating, comments):

        takehomeleft.createReview(myid, forid, idfood, rating, comments)
        return('review created')
    return(render_template('review.html'))
    
@app.route('/returnfood', methods=['GET'])
def returnfood():
    return(str(takehomeleft.returnFoods()))

@app.route('/returnusers', methods=['GET'])
def returnUsers():
    return(str(takehomeleft.returnUsers()))

@app.route('/returnreviews', methods=['GET'])
def returnReviews():
    return(str(takehomeleft.returnReviews()))
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5556) 


# In[ ]:


makeFoodEntry(name, image, datecooked, expiredate,
                 ingredients, location)


# In[7]:


#takehomeleft.createFoodDB('foodentry')


# In[8]:


#takehomeleft.createUserDB('foodentry')


# In[9]:


#takehomeleft.createReviewDB('foodentry')


# In[16]:



#takehomeleft.createUser('joe@me.com', 'test123', 'me.com/joe.png', 'Joe Mckee', '-33.865143, 151.209900')


# In[17]:


#takehomeleft.makeFoodEntry('chick con cane', 'me.com/pasta.png', '04-12-1999', '06-12-1999', 'chicken', '-33.865143, 151.209900')


# In[ ]:





# In[18]:


#takehomeleft.createReview(1, 2, 1, 5, 'good foods')


# In[ ]:





# In[ ]:





# In[ ]:





# In[19]:


#takehomeleft.returnFoods()


# In[20]:


#takehomeleft.filterFoods(1)


# In[21]:


#takehomeleft.returnFoods()


# In[25]:


takehomeleft.returnUsers()


# In[ ]:





# In[23]:


#takehomeleft.returnReviews()


# In[ ]:




