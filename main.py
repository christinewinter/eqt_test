import csv
from datetime import datetime
import json
import requests
from bs4 import BeautifulSoup
import uuid

DIVESTMENT_URL = 'https://eqtgroup.com/current-portfolio/divestments/'
PORTFOLIO_URL = 'https://eqtgroup.com/current-portfolio/'
FUND_URL = 'https://eqtgroup.com/current-portfolio/funds'


def get_divestment_list_from_url(url:str) -> list:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    list_elements = soup.find_all('li', {'class': 'flex-col'})
    company_list = []

    for company in list_elements:
        company_attributes = company.findAll('span', {'class': 'flex-1'})
        company_page_element = company.find('a')
        company_page = company_page_element['href'] if company_page_element else ""
        company_dict = {
            "id": str(uuid.uuid1()),
            "company_name": company.find_next('span', {'class': "inline-block"}).text,
            "sector": company_attributes[0].text,
            "country": company_attributes[1].text,
            "fund": company_attributes[2].text,
            "entry_year": company_attributes[3].text,
            "exit_year": company_attributes[4].text,  # gives error for portfolio since there is no exit defined
            "company_page_path": company_page,
            "timestamp": datetime.now().isoformat()
        }
        company_list.append(company_dict)

    return company_list


def get_portfolio_list_from_url(url:str) -> list:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    list_elements = soup.find_all('li', {'class': 'flex-col'})
    company_list = []

    for company in list_elements:
        company_attributes = company.findAll('span', {'class': 'flex-1'})
        company_page_element = company.find('a')
        company_page = company_page_element['href'] if company_page_element else ""
        company_dict = {
            "id": str(uuid.uuid1()),
            "company_name": company.find_next('span', {'class': "inline-block"}).text,
            "sector": company_attributes[0].text,
            "country": company_attributes[1].text,
            "fund": company_attributes[2].text,
            "entry_year": company_attributes[3].text,
            "company_page_path": company_page,
            "timestamp": datetime.now().isoformat()
        }
        company_list.append(company_dict)

    return company_list


def get_funds_list_from_url(url: str) -> list:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    list_elements = soup.find_all('li', {'class': 'flex-col'})
    fund_list = []

    for fund in list_elements:
        fund_attributes = fund.findAll('span', {'class': 'flex-1'})
        fund_page_element = fund.find('a')
        fund_page = fund_page_element['href'] if fund_page_element else ""
        company_dict = {
            "id": str(uuid.uuid1()),
            "fund_name": fund.find_next('span', {'class': "inline-block"}).text,
            "launch": fund_attributes[0].text,
            "size": fund_attributes[1].text,
            "status": fund_attributes[2].text,
            "sfdr_classification": fund_attributes[3].text,
            "fund_page": fund_page,
            "timestamp": datetime.now().isoformat()
        }
        fund_list.append(company_dict)

    return fund_list


def write_list_to_json(filename: str, company_list: list):
    with open(filename, "w") as output_file:
        json.dump(company_list, output_file, indent=2)


divestment_list = get_divestment_list_from_url(DIVESTMENT_URL)
write_list_to_json("data/divestments.json", divestment_list)

portfolio_list = get_portfolio_list_from_url(PORTFOLIO_URL)
write_list_to_json("data/portfolio.json", portfolio_list)

fund_list = get_funds_list_from_url(FUND_URL)
write_list_to_json("data/fund.json", fund_list)
