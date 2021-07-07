import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/b?node=26297682031&pf_rd_r=7GE1JEZKJRM79S5JRMW9&pf_rd_p=64f36d70-0b17-4d16-b155-a8167dc13269&pd_rd_r=011faac1-c687-484a-a77e-165b0c8de4e7&pd_rd_w=UpqNW&pd_rd_wg=6V4J6&ref_=pd_gw_unk'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

#productlinks = []

#for x in range(1,6):
r = requests.get('https://www.amazon.in/s?i=specialty-aps&rh=n%3A26297662031&fs=true&ref=lp_26297662031_sar')
soup = BeautifulSoup(r.content, 'lxml')
productlist = soup.find_all('div', class_='a-column a-span4')
    #for item in productlist:
     #   for link in item.find_all('a', href = True):
      #      productlinks.append(url = link['href'])

print(productlist)
