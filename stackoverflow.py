import requests
from bs4 import BeautifulSoup

SEARCH_TARGET = "python"
URL = f"https://stackoverflow.com/jobs?q={SEARCH_TARGET}&sort=i"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
  last_page = pages[-2]
  return int(last_page.get_text(strip=True))

def extract_job(html):
  title = html.find("h2", {"class": "fs-body3"}).find("a", title=True)["title"]
  company_information = html.find("h3", {"class":"fc-black-700"})
  company = company_information.find("span", {"class": None}).text.strip()
  location = company_information.find("span", {"class": "fc-black-500"}).text.strip()
  return {'title': title, 'company': company, 'location': location}


def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs