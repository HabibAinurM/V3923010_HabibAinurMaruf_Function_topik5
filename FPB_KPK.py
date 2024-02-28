#!/usr/bin/env python
# coding: utf-8

# In[7]:


def hitung_fpb(x, y):
    if y == 0:
        return x
    else:
        return hitung_fpb(y, x % y)

def hitung_kpk(x, y):
    kpk = max(x, y)
    while True:
        if kpk % x == 0 and kpk % y == 0:
            return kpk
        else:
            kpk += 1

while True:
    print("Pilihan:")
    print("1. Hitung FPB")
    print("2. Hitung KPK")
    print("3. Keluar")
    
    pilihan = int(input("Masukkan pilihan Anda[1,2,3]: "))
    
    if pilihan == 1:
        x = int(input("Masukkan bilangan pertama: "))
        y = int(input("Masukkan bilangan kedua: "))
        fpb = hitung_fpb(x, y)
        print(f"FPB dari {x} dan {y} adalah {fpb}")
    elif pilihan == 2:
        x = int(input("Masukkan bilangan pertama: "))
        y = int(input("Masukkan bilangan kedua: "))
        kpk = hitung_kpk(x, y)
        print(f"KPK dari {x} dan {y} adalah {kpk}")
    elif pilihan == 3:
        print("Selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




