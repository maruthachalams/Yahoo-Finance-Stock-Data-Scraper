from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import re

def data_clean(data):
    data = re.sub('&amp;','&',str(data))
    data = re.sub('&quot;',"'",str(data))
    data = re.sub('&nbsp;','',str(data))
    data = re.sub('&#39;;',"';",str(data))
    data = re.sub('&#39;',"';",str(data))
    data = re.sub('&#xD;&#xA;',' ',str(data))
    data = re.sub('#x27;',"'",str(data))
    data = re.sub(r'\s+',' ',str(data))
    data = re.sub('<[^>]&?>','',str(data))
    return data

def single_regex(pattern, target_string):
    data = re.findall(pattern, target_string)
    if data:
        data = data[0]
    else:
        data = ''
    return data

def block_loop(loop_block):
    symbol = single_regex(r'class\=\"symbol[\w\W]*?>([^>]*?)<',str(loop_block))
    name = single_regex(r'class\=\"longName[\w\W]*?>([^>]*?)<',str(loop_block))
    last_traded_price = single_regex(r'class\=\"last\-price[\w\W]*?>([^>]*?)<',str(loop_block))
    change_of_price = single_regex(r'data-field\=\"regularMarketChange\"[\w\W]*?data-value\=\"([^>]*?)"',str(loop_block))
    percentage_of_change = single_regex(r'data-field\=\"regularMarketChangePercent\"[\w\W]*?data-value\=\"([^>]*?)"',str(loop_block))
    return symbol,name,last_traded_price,change_of_price,percentage_of_change
    
Gainer_output_data = "Symbol\tName\tLast Traded Price\tChange Of Price\tPercentage Of Change\n"
with open ("Gainer_Output.txt",'w') as OP:
    OP.write(Gainer_output_data)

Loser_output_data = "Symbol\tName\tLast Traded Price\tChange Of Price\tPercentage Of Change\n"
with open ("Loser_Output.txt",'w') as OP:
    OP.write(Loser_output_data)

Most_active_output_data = "Symbol\tName\tLast Traded Price\tChange Of Price\tPercentage Of Change\n"
with open ("Most_active_Output.txt",'w') as OP:
    OP.write(Most_active_output_data)

Trending_output_data = "Symbol\tName\tLast Traded Price\tChange Of Price\tPercentage Of Change\n"
with open ("Trending_Output.txt",'w') as OP:
    OP.write(Trending_output_data)

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

main_url = "https://finance.yahoo.com/"
driver.get(main_url)

content = driver.page_source

# Write the content to a file
with open("content.html", 'w', encoding="utf-8") as PC:
    PC.write(content)
    time.sleep(5)
content = data_clean(content)

blocks = re.findall(r'class\=\"dock\-item\s*primary\s*([\w\W]*?)\/a>', str(content))
gainer_blocks = blocks[0:5]
loser_blocks = blocks[5:10]
most_active_blocks = blocks[10:15]
trending_blocks = blocks[15:20]
for gainer_block in gainer_blocks:
    gainer_block1 = block_loop(gainer_block)
    symbol = list(gainer_block1)[0]
    name = list(gainer_block1)[1]
    last_traded_price = list(gainer_block1)[2]
    change_of_price = list(gainer_block1)[3]
    percentage_of_change = list(gainer_block1)[4]
    
    Gainer_output_data = f"{symbol}\t{name}\t{last_traded_price}\t{change_of_price}\t{percentage_of_change}\n"
    with open ("Gainer_Output.txt",'a') as OP:
        OP.write(Gainer_output_data)
print("Gainer Block Completed") 

for loser_block in loser_blocks: 
    loser_block1 = block_loop(loser_block)
    symbol = list(loser_block1)[0]
    name = list(loser_block1)[1]
    last_traded_price = list(loser_block1)[2]
    change_of_price = list(loser_block1)[3]
    percentage_of_change = list(loser_block1)[4]
      
    Loser_output_data = f"{symbol}\t{name}\t{last_traded_price}\t{change_of_price}\t{percentage_of_change}\n"
    with open ("Loser_Output.txt",'a') as OP:
        OP.write(Loser_output_data)

print("Loser Block Completed")
    
for most_active_block in most_active_blocks:    
    most_active_block1 = block_loop(most_active_block)
    symbol = list(most_active_block1)[0]
    name = list(most_active_block1)[1]
    last_traded_price = list(most_active_block1)[2]
    change_of_price = list(most_active_block1)[3]
    percentage_of_change = list(most_active_block1)[4]
    
    Most_active_output_data = f"{symbol}\t{name}\t{last_traded_price}\t{change_of_price}\t{percentage_of_change}\n"
    with open ("Most_active_Output.txt",'a') as OP:
        OP.write(Most_active_output_data)

print("Most Active Block Completed")

for trending_block in trending_blocks:     
    trending_block1 = block_loop(trending_block)
    symbol = list(trending_block1)[0]
    name = list(trending_block1)[1]
    last_traded_price = list(trending_block1)[2]
    change_of_price = list(trending_block1)[3]
    percentage_of_change = list(trending_block1)[4]
    
    Trending_output_data = f"{symbol}\t{name}\t{last_traded_price}\t{change_of_price}\t{percentage_of_change}\n"
    with open ("Trending_Output.txt",'a') as OP:
        OP.write(Trending_output_data)

print("Trending Block Completed")

print("Completed")   

    
    

