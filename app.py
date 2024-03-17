# Importar a bibliotecas
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import coletaplanilha as plan


# Navegar até o whatsapp web
class WhatsappBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)

        # Definir contatos e grupos e mensagem a ser enviada
        self.total = plan.total_list
        self.contatos = plan.contatos_list
        self.mensagens = plan.mensagens_list
        self.nomes = plan.nomes_list

        for contato, mensagem, nomes, total in zip(self.contatos, self.mensagens, self.nomes, self.total):
            self.buscar_contato(contato)
            self.enviar_mensagem(mensagem, nomes, total)

            if contato == self.contatos[-1]:
                break

    # Buscar contatos/grupos'
    def buscar_contato(self, contato):

        campo_pesquisa = self.driver.find_element(By.XPATH,
                                                  '//div[contains(@class, "to2l77zo gfz4du6o ag5g9lrv bze30y65 '
                                                  'kao4egtt qh0vvdkp")]')

        campo_pesquisa.click()

        campo_pesquisa.send_keys(contato)

        campo_pesquisa.send_keys(Keys.ENTER)

    def enviar_mensagem(self, mensagem, nomes, total):

        campo_mensagem = self.driver.find_element(By.CLASS_NAME, "_3Uu1_")

        campo_mensagem.click()

        campo_mensagem.send_keys(f"Boa tarde {nomes}, total consumido,")

        campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)

        campo_mensagem.send_keys(f'{total} bolos,')

        campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)

        campo_mensagem.send_keys(f' valor de R${mensagem},00 bolos no pote')

        campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)

        campo_mensagem.send_keys('chave pix: 62998225591')

        botao_enviar = self.driver.find_element(By.XPATH, '//span[@data-icon="send"]')

        botao_enviar.click()

        # Apagar o primeiro item da lista
        # campo_pesquisa.send_keys(Keys.BACKSPACE)
        # time.sleep(5)

        # enviar_mensagem(mensagem)
        # Campo de pesquisa selectable-text copyable-text iq0m558w g0rxnol2
        # Campo de mensagem <div tabindex="-1" class="_3Uu1_ class="selectable-text copyable-text iq0m558w g0rxnol2">
        # Enviar mensagens para o contato/grupo


bot = WhatsappBot()
bot.buscar_contato()
