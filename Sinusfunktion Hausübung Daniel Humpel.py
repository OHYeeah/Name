#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Sinusfunktion plotten
import numpy as np
import matplotlib.pyplot as plt

def plot_sinus(genau):
    grad = np.arange(0, 360, genau)
    sinus = np.sin(np.deg2rad(grad))
    
    return grad, sinus

genau = int(input("Geben Sie die Genauigkeit (Gradintervalle) ein: "))

grad, sinus = plot_sinus(genau)

plt.plot(grad, sinus)
plt.xlabel('Grad')
plt.ylabel('Sinus')
plt.title('Sinus-Funktion')
plt.grid(True)
plt.show()


# In[ ]:




