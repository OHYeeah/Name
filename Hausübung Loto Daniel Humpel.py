#!/usr/bin/env python
# coding: utf-8

# In[13]:


import random

anzahl_tipps = int(input("Anzahl der Lottotipps eingeben: "))

lotto_tipps = []
while len(lotto_tipps) < anzahl_tipps:
    tipp = random.sample(range(1, 46), 6)
    
    if tipp not in lotto_tipps:
        lotto_tipps.append(tipp)

print(lotto_tipps)

print("Viel Glück")


# In[ ]:




