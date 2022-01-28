from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import chromedriver_binary
import json, os

os.system("cls")

options = Options()
options.add_argument("--headless")
options.add_argument("--level-log=3")

try:
    browser.quit()
    browser = Chrome(options=options)
except:
    browser = Chrome(options=options)
    
url = "https://www.bhinneka.com/jual-gasoline-generators/v1PzAE7"
browser.get(url)
try:
    xpath = '//*[@id="__next"]/div[3]/div[2]/div[3]/div[2]/div[2]'
    WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.XPATH,xpath))
    )
    page = BeautifulSoup(browser.page_source,"html.parser")
except: pass

product_data = []
context = {
    "class": "product-wrapper",
    "data-testid": "product-click"
}
ref = "https://www.bhinneka.com"
for a in page.find_all("a",context):
    try:
        url = ref+a['href']
        title = a.find("div",{"class":"product-title"}).get_text().strip()
        price = a.find_next("div",{"class":"price"}).get_text().strip()
        product_data.append({
            "nama_barang": title,
            "harga_barang": price,
            "link": url
        })
    except: pass

json.dump(product_data,open("product.json","w"))
browser.quit()