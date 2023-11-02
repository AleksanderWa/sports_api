from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0',
    # 'From': 'youremail@domain.example'  # This is another valid field
}

url = "https://www.nba.com/stats/players/traditional?SeasonType=Regular+Season"

options = Options()
options.add_experimental_option('detach', True)
with webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
) as driver:
    driver.get(url)
    # crom_container = driver.find_element(By.CLASS_NAME, "crom-container")#.get_attribute("innerHTML")
    soup = BeautifulSoup(driver.page_source)
    # reviews_selector = crom_container.find_all('div', class_='reviewSelector')
    # tbody =  crom_container.find_element(By.TAG_NAME, "tbody")
    tbody = soup.select_one('.Crom_body__UYOcU')
    for tr in tbody.find_all('tr'):
        for td in tr.find_all('td'):
            print(td)
        name = tr[1].get_text()
        team_code = tr[2].get_text()
        age = tr[3].get_text()
        print(f'name {name} \t team code {team_code} \t age {age}')
