from bs4 import BeautifulSoup
import requests, openpyxl

startPage = input('Which page would you like to start the scrape from?')
pages = input('Which page would you like to end your scrape?')

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'hockeyData'
sheet.append(['Team Name','Year','Win %','+/-'])
#print(excel.sheetnames)

#choosing which site to scrape
url = "https://www.scrapethissite.com/pages/forms/"

#this will grab the amount of pages in range worth of data
for page in range(int(startPage),int(pages)+1):

    html = requests.get(url+'?page_num='+str(page))

    soup = BeautifulSoup(html.content, 'html.parser')

    teams = soup.find('table', class_='table').find_all('tr', class_='team')

    for team in teams:

        teamName = team.find('td', class_='name').text
        year = team.find('td', class_='year').text
        winPercent = team.find('td', class_=['pct text-success', 'pct text-danger']).text
        plusMinus = team.find('td', class_=['diff text-success', 'diff text-danger']).text
        #print(year, teamName, winPercent, plusMinus)
        sheet.append([teamName, year, winPercent, plusMinus])

excel.save('HockeyData.xlsx')


    
