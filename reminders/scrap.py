import requests
from bs4 import BeautifulSoup


# req=requests.get("https://m.cricbuzz.com/")
req2=requests.get("https://internshala.com/internships/python%2Fdjango-internship/")

# soup=BeautifulSoup(req.content,"html.parser")
soup2=BeautifulSoup(req2.content,"html.parser")
elements1 = soup2.findChild(class_='internship_meta')

# res=soup.title
# print(res.get_text())
# elements = soup.find_all(class_='ui-completed-batteam-scores')

# Process the scraped data as needed
# data = [element.text for element in elements]
datas1 =str ([element.text for element in elements1])
# if datas1 =="Just now":
print(datas1)

# return render(request, 'scraper/result.html', {'data': data}