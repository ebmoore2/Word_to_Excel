#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pdf to csv
# save as a csv consisting of 3 fields:

# 1) building numbers "FACNO/LD"

# 2) building ownership type "Interest Type"
# [ONST=state, FEE=federal, LEAS=lease]

# 3) and building name "RPA Description"


# In[2]:


#have to put r before path name string, or else get unicode error, or write as "filename.txt" without full path

# path to text
# C:\Users\Buffie\Documents\DEMA\DEMA_FMO_pdf_to_csv\AZ_FISP_2018_11_16_building_data_FMO.txt

# path to pdf
# C:\Users\Buffie\Documents\DEMA\DEMA_FMO_pdf_to_csv\AZ_FISP_2018_11_16_building_data_FMO.pdf

# read documment from path into list or tuple


####### attempt 0 #######
#f = open('.txt', 'r')

#print(f.mode)

#f.close


####### attempt 1 #######
#with open("", "r") as f:
#    for line in f:
#        print(line, end='')
    
#    size_to_read = 50
    
#    f_contents = f.read(size_to_read)
    
#    while len(f_contents) > 0
#    print(f_contents, end='')
    
#    f_contents = f.readline()
#    print(f_contents, end='')


####### attempt 2 #######
#FMO_text = list(open(r"C:\Users\intern\Documents\ArcGIS\Projects\Facilities Maintenance Office\Interest_Type_Word_conversion_table.txt", 'r'))

#print(FMO_text[:10])

####### attempt 3 #######
FMO_text = "Interest_Type_Word_conversion_table.txt"


# In[3]:


# slicing rough draft

# LET:
# building_number = substring_0
# building_ownership_type = substring_1
# building_name = substring_2

####### slicing attempt 0 #######
#substring_0 = FMO_text[FMO_text.find("FACNO/LD"):FMO_text.find("RPA Name")]  
#substring_1 = FMO_text[FMO_text.find("Interest Type"):FMO_text.find("Placed")]
#substring_2 = FMO_text[FMO_text.find("RPA Description"):FMO_text.find("Design FAC")]



#print(substring_0)
#print(substring_1)
#print(substring_2)
# seems to only return the first match only


# In[4]:


# use regular expression to find pattern

# regex rough draft
import re

####### compile pattern attempt 0 #######
#pattern_0 = re.compile(substring_0)
#pattern_1 = re.compile(substring_1)
#pattern_2 = re.compile(substring_2)

####### compile pattern attempt 1 #######
#pattern_0 = re.compile([\n\r].*FACNO/LD:\s*([^\n\r]*))
#pattern_1 = re.compile(substring_1)
#pattern_2 = re.compile(substring_2)


####### compile pattern attempt 2 #######
#substring_0 = (?<="FACNO/LD").*?(?="RPA Name")
#substring_1 = (?<="Interest Type").*?(?="Placed")
#substring_2 = (?<="RPA Description").*?(?="Design FAC")

####### compile pattern attempt 3 #######
pattern_0 = re.search(r'FACNO/LD\.(.*?)RPA Name', FMO_text)
pattern_1 = re.search(r'Interest Type\.(.*?)Placed', FMO_text)
pattern_2 = re.search(r'RPA Description\.(.*?)Design FAC', FMO_text)


# In[6]:


# print out test

print(pattern_0)


#for match in matches:
#    print(match)

#with open('.txt', 'r') as f:
#    contents = f.read()
#matches = pattern.finditer(contents)

#matches_0 = pattern_0.finditer(FMO_text)
#matches_1 = pattern_1.finditer(FMO_text)
#matches_2 = pattern_2.finditer(FMO_text)

#for match in matches_0:
#    print(match)
    
#for match in matches_1:
#    print(match)
    
#for match in matches_2:
#    print(match)


# In[ ]:




