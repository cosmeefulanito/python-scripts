from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support	 import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time


driver = webdriver.Chrome()

url = 'https://linkedin.com/uas/login'
driver.get(url)
driver.implicitly_wait(10) #espero que la pagina termine de cargar

# credenciales para el inicio de sesión
email_input = driver.find_element(By.ID, 'username')
email_input.send_keys('tu-usuario')

password_input = driver.find_element(By.ID, 'password')
password_input.send_keys('tu-contrasena')

login_button = driver.find_element(By.XPATH, '//*[@type="submit"]')
login_button.click()

# esperamos que inicie
time.sleep(10)

# driver.get('https://www.linkedin.com/jobs/')
# driver.implicitly_wait(10)

driver.get('https://www.linkedin.com/jobs/collections/recommended?discover=recommended&amp;discoveryOrigin=JOBS_HOME_JYMBII')
driver.implicitly_wait(10)

# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results__list"))
# )

element = WebDriverWait(driver, 20).until(
    # EC.presence_of_element_located((By.XPATH, "(//div[contains(@class, 'jobs-search-results-list')])[2]"))
    EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results-list"))
)

def scroll_and_load(driver, container):
    last_height = 0
    while True:
        container.send_keys(Keys.END)
        time.sleep(2)
        # driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", container)
        # time.sleep(2)
        new_height = driver.execute_script("return arguments[0].scrollHeight", container)
        
        if(new_height == last_height):
            break
        last_height = new_height

inside_container = driver.find_element(By.CLASS_NAME, "jobs-search-results-list")

scroll_and_load(driver, inside_container)
time.sleep(2)
html = driver.page_source



soup = bs(html,'html.parser')

list_jobs = soup.find_all('li', class_="jobs-search-results__list-item")

for job in list_jobs:
    titulo = job.find('div', class_="artdeco-entity-lockup__title").get_text(strip=True)
    print("Titulo" , titulo)

# headline = soup.find_all('a', {'class': 'link-without-hover-visited'})[2]

# nombre = headline.find('h3', {'class' : 'profile-card-name'}).get_text(strip=True)
# profesion = headline.find('p', {'class' : 'profile-card-headline'}).get_text(strip=True)
# origen = headline.find('p', {'class' : 'text-body-xsmall t-black--light mt1'}).get_text(strip=True)




# print("Contenido nombre: ", nombre)
# print("Contenido profesion: ", profesion)
# print("Contenido origen: ", origen)


# Cerrar el navegador
driver.quit()

