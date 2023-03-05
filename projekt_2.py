'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Radka Matouchová
email: radka.matouchova@seznam.cz
discord: Amrita#9069
'''
nadpis = f"{'':🐂^10} Vítej {'':🐄^10}"
uvodni_text = '''-------------------------------------------------
Zahrajme si hru Bulls & Cows.
Náhodně jsem ti vygeneroval 4-ciferné číslo.'''
import random

def generovani_cisla():
	while True:
		tajenka = str(random.randint(1000, 9999))
		if len(set(tajenka)) == 4:
			break
	return tajenka
	
def vyhodnoceni():
	byci = []
	kravy = []
	byci_emoji = '🐂'
	kravy_emoji = '🐄'
	for index, cifra in enumerate(tip):
		if cifra in tajenka and tajenka[index] == tip[index]:
			byci.append(cifra)
		if cifra in tajenka and tajenka[index] != tip[index]:
			kravy.append(cifra)
	if len(byci) == 1:
		byci_pocet = 'býk'
	else:
		byci_pocet = 'býci'
	if len(kravy) == 1:
		kravy_pocet = 'kráva'
	else:
		kravy_pocet = 'krávy'
	return f"{len(byci)} {byci_pocet} {byci_emoji*len(byci)}, {len(kravy)} {kravy_pocet} {kravy_emoji*len(kravy)}"

def kontrola_cisla(tip, pocet_pokusu):
	if not tip.isnumeric():
		return 'Nezadaj jsi číslo.'
	elif tip[0] == '0':
		return 'Číslo nesmí začínat nulou.'
	elif len(tip) != 4:
		return 'Zadal jsi příliš dlouhé nebo krátké číslo.'
	elif len(set(tip)) != 4:
		return 'Zadaj jsi duplicitní cifru/y.'
	else:
		return vyhodnoceni()
		
def hra():
	global tajenka
	tajenka = generovani_cisla()
	print('-' * 49)
	print(nadpis)
	print(uvodni_text)
	pocet_pokusu = 0
	while True:
		print('-' * 49)
		global tip
		tip = input('Hádej číslo: ')
		print(kontrola_cisla(tip, pocet_pokusu))
		pocet_pokusu += 1
		if tip == tajenka:
			print(f"Gratuji! Vyhrál/a jsi na {pocet_pokusu}. pokus!")
			break

hra()
