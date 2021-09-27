'''
Date: 27/09/2021
Author: Jesús Arellano Usón

Objetive:
Check if the Spanish Fucking Ministry of universities has already published the damn FPU scholarship resolution
whiout lossing my time checking my fuckin mail. If a change in the grant webpage is detected a tkinter
popup will come up. Just launch it at background and relax thinking about your future crying in quiet mode.
'''

import requests
import time
import easygui


ENDPOINT_URL = "https://www.educacionyfp.gob.es/servicios-al-ciudadano/catalogo/general/99/998758/ficha/998758-2020.html"
UPDATE_MSG = "Resolución publicada"
UPDATE_WIN_TITLE = "Warning update"
SLEEP_PARAM = 10

r = requests.get(ENDPOINT_URL)
first_request = r.text
second_request = first_request

while first_request == second_request:
    r = requests.get(ENDPOINT_URL)
    second_request = r.text
    time.sleep(SLEEP_PARAM)

easygui.msgbox(UPDATE_MSG, title=UPDATE_WIN_TITLE)
