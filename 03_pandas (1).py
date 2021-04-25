#!/usr/bin/env python
# coding: utf-8

# # pandas
# Here we will have a quick play with a pandas DataFrame and use what we've learned about accessing them to answer some questions.
# 
# We stopped ten people in the street and asked them what pets they have. We also recorded the person's sex and age.

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


pets = pd.DataFrame({'sex': np.array(['M', 'M', 'F', 'M', 'F', 'F', 'F', 'M', 'F', 'M']),
                   'age': np.array([21, 45, 23, 56, 47, 70, 34, 30, 19, 62]),
                   'pets': np.array([['cat', 'dog'],
                                    ['hamster'],
                                    ['cat', 'gerbil'],
                                    ['fish', 'hamster', 'gerbil'],
                                    ['cat'],
                                    ['dog'],
                                    ['dog'],
                                    ['cat'],
                                    ['rabbit', 'cat'],
                                    ['dog']])})
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)


# We have been asked to analyse the survey responses. In particular, we have been given the questions
# 
# * What sex was the youngest respondent?
# * What age was the person with the most pets?
# * What was the most popular pet?
# * What was the average age of dog owners?
# 

# Firstly, let's just look at the data. It's not very big so we don't actually even need to use head().

# In[4]:


pets


# Notice here, as well, how the notebook has a nice default presentation for DataFrames. And, yes, you can customize this! We won't be going into that here.

# ## What sex was the youngest respondent?
# Hint, you might find the .loc accessor useful here. Think about breaking this task down into creating a boolean index that is True where the value in the age column is equal to the minimum of the age column. Then select the sex column.

# In[5]:


# one line of code
pets.loc[2,'sex']


# We see that the youngest respondent was female (F)

# ## What age was the person with the most pets?
# Hint, you may find _apply_ ing len as a lambda function to the pets column useful here. Remember that calling len on the pets column will just return the length of the series, which is the number of rows in the DataFrame. In fact, adding useful features to your data is a very common thing in data science, so go ahead and create a new column in our pets DataFrame and call it 'num_pets'.

# In[6]:


# task: create new column 'num_pets' which contains the number of pets
# each person had (hint: this is the length of each list in the pets column)
# one line of code here:
pets['num_pets'] = len(pets)


# In[7]:


# view the DataFrame again to check our new column is there
pets


# In[8]:


pets.loc[pets['num_pets'] == max(pets['num_pets']), 'age']


# So we see the person with the most pets was 56 years old.

# ## What was the most popular pet?
# This is a very interesting question, given the data, because the data are arranged by respondent, not by pet. We need to _get into_ the pets column now in order to count each type of animal. To do this, we could perform a list comprehension and iterate over each list element for each Series element. But here we're going to give you a handy way to convert that Series of lists into a (longer) Series. The reason for this is to end up with another Series, which means we still have access to the powerful methods available from pandas.

# In[9]:


pet_series = pets['pets'].apply(pd.Series).stack().reset_index(drop=True)
pet_series


# In[10]:


# task: produce an ordered count of each animal
# one line of code here:
from collections import Counter

def most_popular_pet(pet_series):
    c = Counter(pet_series)
    return c.most_common(1)[0][0]
print(most_popular_pet(pet_series))


# Cat is the most popular pet.

# Note we could also have approached this task by iterating over the original pets column and collecting the animal as the key and the count as the value, but even this requires more explicit iterating and count incrementing, and we still need to iterate over the final result to find the maximum count. With our approach here, we can easily read the most popular pet animal from the top of the result.

# ## What was the average age of dog owners?
# Hint, again here you may find it useful to use a lambda function to create a boolean index which is True if a respondent said they had a dog and False otherwise.

# In[11]:


# example
('dog' in ['dog', 'cat'], 'dog' in ['rabbit'])


# In[44]:


# task: use a lambda function to test whether 'dog' is contained in each list of animals,
# extract the age column and then chain the mean method to calculate the average age.
# one line of code here:
dog_owners = pets['pets'].apply(lambda x: x==['dog'])
dog_owners


# # Conclusion
# You've now seen how pandas holds tabular data, where each column can be a different type (e.g. sex is character and age is a number). Furthermore, pandas provides incredibly powerful methods for slicing and dicing the data to answer some very interesting questions using relatively little code. You're well on your journey to becoming a data ninja!
