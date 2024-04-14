lista_zakupów = {
    'piekarnia': ['chleb','pączek','bułki'],
    'warzywniak': ['marchew','seler','rukola']
}

liczba_produktów=0

print ("Lista zakupów")
for sklep,rzeczy in lista_zakupów.items():
    liczba_produktów += len (rzeczy)
    print (f"Idę do {sklep.capitalize()}, kupuję tu następujące rzeczy: {str([produkt.capitalize() for produkt in rzeczy])}.")
    