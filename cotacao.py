import pyautogui 
import time

time.sleep(2) # Define 2 segundo de espera
pyautogui.press('win') # Pressiona a tecla do window uma vez
pyautogui.write('chrome') # Escreve chrome na pesquisa do window
time.sleep(2)
pyautogui.press('enter') #  Aperta o botão enter do teclado
time.sleep(2)
pyautogui.write('Cotacao do Dolar hoje') # Pesquisa a cotação do Dolar hoje e pressiona enter
time.sleep(2)
pyautogui.press('enter')
