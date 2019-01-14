# pdf to csv
# save as a csv consisting of 3 fields:

# 1) building numbers "FACNO/LD"

# 2) building ownership type "Interest Type"
# [ONST=state, FEE=federal, LEAS=lease]

# 3) and building name "RPA Description"


# path to text
# C:\Users\Buffie\Documents\DEMA\DEMA_FMO_pdf_to_csv\AZ_FISP_2018_11_16_building_data_FMO.txt

# path to pdf
# C:\Users\Buffie\Documents\DEMA\DEMA_FMO_pdf_to_csv\AZ_FISP_2018_11_16_building_data_FMO.pdf

# read documment ???


# use regular expression to find pattern



# regex rough draft
import re

# slicing rough draft
mySubString_1 = FMO_text[FMO_text.find("FACNO/LD"):FMO_text.find("RPA Name")]  
mySubString_2 = FMO_text[FMO_text.find("Interest Type"):FMO_text.find("Placed")]
mySubString_3 = FMO_text[FMO_text.find("RPA Description"):FMO_text.find("Design FAC")]

# compile pattern
pattern = re.compile(r'#slicing_variables_here')

#for match in matches:
#    print(match)

with open('.txt', 'r') as f:
    contents = f.read()

matches = pattern.finditer(contents)

for match in matches:
    print(match)


#print(mySubString_1[:500])
#print(mySubString_2[:500]) changed from "Placed in Service Date" to "Placed"
#print(mySubString_3[:500])