import requests
from bs4 import BeautifulSoup

url = 'https://eqtgroup.com/current-portfolio/divestments/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

divestments_list = soup.find_all('li', {'class': 'flex-col'})
divestment_dict = {}

for company in divestments_list:
    company_name = company.find_next('span', {'class': "inline-block"}).text
    company_attributes = company.findAll('span', {'class': 'flex-1'})
    divestment_dict[company_name] = {
        "sector": company_attributes[0].text,
        "country": company_attributes[1].text,
        "fund": company_attributes[2].text,
        "entry": company_attributes[3].text,
        "exit": company_attributes[4].text
    }
    print(company_name)

print(divestment_dict.keys())
