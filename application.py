import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

contatos_df = pd.read_excel("Enviar.xlsx")

service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

navegador.get('https://web.whatsapp.com/')

while len(navegador.find_element(By.TAG_NAME, 'side')) < 1:
    sleep(1)

for index, mensage in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[index, "Pessoa"]
    numero = contatos_df.loc[index, "Número"]
    texto = f"Oi {pessoa}! {mensage}"
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)

while len(navegador.find_element(By.ID, 'side')) < 1:
    sleep(1)
navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
sleep(5)