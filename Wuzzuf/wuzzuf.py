from bs4 import BeautifulSoup
import requests
import csv
import time
import pandas as pd

response = requests.get('https://wuzzuf.net/a/IT-Software-Development-Jobs-in-Egypt?ref=browse-jobs')
response.status_code
src = response.text
soup = BeautifulSoup(src, 'lxml')

companyNames = []
companyLocations = []
jobLinks = []
jobTitles = []
jobDescriptions = []
totalJobs = []

for page in range(50):
    response = requests.get(f'https://wuzzuf.net/a/IT-Software-Development-Jobs-in-Egypt?ref=browse-jobs&start= {page}')
    # time.sleep(1)
    soup = BeautifulSoup(response.content, 'lxml')
    allJobs = soup.find_all('div', class_ = 'css-pkv5jc')
    for job in allJobs:
        names = job.find('a', class_='css-17s97q8').text
        companyNames.append(names)

        locations = job.find('span', class_='css-5wys0k').text
        companyLocations.append(locations)

        titles = job.find('a', class_='css-o171kl').text
        jobTitles.append(titles)

        descriptions = job.find('div', class_='css-y4udm8').text
        jobDescriptions.append(descriptions)

        links = job.find('a', class_='css-o171kl').get('href')
        jobLinks.append(links)

for title, description, company, location, link in zip(jobTitles, jobDescriptions, companyNames, companyLocations, jobLinks):
    totalJobs.append(
        {'Title': title, 'Description': description, 'Company': company, 'Location': location, 'Link': link})

with open('wuzzufJobs.csv','w',newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=['Title', 'Description', 'Company', 'Location', 'Link'])
    writer.writeheader()
    writer.writerows(totalJobs)

    # for i in range(len(jobLinks)):
    #     writer.writerow({'Title':jobTitles[i], 'Description':jobDescriptions[i], 'Company':companyNames[i], 'Location':companyLocations[i], 'Link':jobLinks[i]})

df = pd.read_csv('wuzzufJobs.csv')
print(df)