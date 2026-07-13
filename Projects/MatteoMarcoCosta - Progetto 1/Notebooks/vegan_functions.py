#Vegan functions: this module contains all functions recalled in the main program

# vegan_help
def vegan_help():
    """
    vegan_help: list of all possible program commands
    """
    return print("I comandi disponibili sono i seguenti: \n"
                 "aggiungi: aggiungi un prodotto al magazzino \n"
                 "elenca: elenca i prodotti in magazzino \n"
                 "vendita: registra una vendita effettuata \n"
                 "profitti: mostra i profitti totali \n"
                 "aiuto: mostra i possibili comandi \n"
                 "chiudi: esci dal programma")


# vegan_help_mess
def vegan_help_mess():
    """
    vegan_help_mess: messagge of error that appears in the main 
    programm when the intention is not in vegan_help list
    """
    return print("Comando non valido\n"
                 "I comandi disponibili sono i seguenti: \n"
                 "aggiungi: aggiungi un prodotto al magazzino \n"
                 "elenca: elenca i prodotti in magazzino \n"
                 "vendita: registra una vendita effettuata \n"
                 "profitti: mostra i profitti totali \n"
                 "aiuto: mostra i possibili comandi \n"
                 "chiudi: esci dal programma")


# is_float
def is_float(string):
    """
    is_float: return True if float and False if Error. 
    The function is used in vegan_add function to check if a number is float
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


# vegan_add
def vegan_add(list_mag):
    """
    vegan_add: taking a input dictionary (or empty), the function takes product information. 
    A product is saved as a key dictionary.
    """
    product = str(input("Nome del prodotto: "))
    
    if product not in list_mag.keys():
        
        #quantity
        quantity = input("Quantità: ")

        while quantity.isnumeric() != True or quantity[0 : 1] == "0":#int number control 
            print("La quantità inserita non è valida")
            quantity = input("Reinserire la quantità: ")

        #buy_price
        buy_price = input("Prezzo di acquisto: ")
        
        while is_float(buy_price) != True or float(buy_price) <= 0:#float price control
            print("Il prezzo inserito non è valido")
            buy_price = float(input("Reinserire il prezzo di acquisto: "))
            
        #sell_price
        sell_price = input("Prezzo di vendita: ")
        
        while is_float(sell_price) != True or float(sell_price) <= 0:#float price control
            print("Il prezzo inserito non è valido")
            sell_price = float(input("Reinserire il prezzo di vendita: "))
            
        values = [quantity, buy_price, sell_price]
        list_mag[product] = values
        
        print(f"AGGIUNTO: {int(quantity)} X {product}")
    
    elif product in list_mag.keys():
        quantity = input("Quantità: ")
        
        while quantity.isnumeric() != True or quantity[0 : 1] == "0":
            print("La quantità inserita non è valida")
            quantity = input("Reinserire la quantità: ")
            
        list_mag[product][0] = int(list_mag[product][0]) + int(quantity)#update store quantity
        
        print(f"Prezzo di acquisto: {list_mag[product][1]}\n"
              f"Prezzo di vendita: {list_mag[product][2]}\n"
              f"AGGIUNTO: {int(quantity)} X {product}")
        
    else:
        print("ERROR: la vendita non è stata possibile")
        
        
# vegan_close
def vegan_close():
    """
    vegan_close: when the main program is closed, the function returns "Bye bye"
    """
    return print("Bye bye")
        
    
# vegan_list
def vegan_list(el):
    """
    vegan_list: taking a store dictionary, the function lists products quantities and prices.
    The \u20ac is the unicode Euro rapresentation 
    """
    if len(el) > 0:
        print("PRODOTTO QUANTITA' PREZZO")
        for k in el.keys():
             print(f"{k} {int(el[k][0])} \u20ac{float(el[k][2]):.2f}")
    else:
        print("Il magazzino è vuoto, inserire eventuali articoli")
        
# vegan_gross
def vegan_gross(el):
    """
    vegan_gross: return a sum of a list, it is recalled in vegan_sell to calculated gross value
    """
    s = 0
    if len(el) > 0:
        for k in el.keys():
               s += el[k][0]*el[k][1]
    else:
        return 0
    return s

# vegan_net
def vegan_net(el):
    """
    vegan_net: return a sum of a list, it is recalled in vegan_sell to calculated net value
    """
    s = 0
    if len(el) > 0:
        for k in el.keys():
               s += el[k][0]*el[k][2]
    else:
        return 0
    return s

# vegan_profit
def vegan_profit(a, b):
    """
    vegan_profit: sum of element in a list of numbers. 
    It is recalled in vegan_sell function to calculate gross and net profits.
    The \u20ac is the unicode Euro rapresentation 
    """
    if len(a) > 0 and len(b) > 0:
        a_sum = round(sum(a), 2)
        b_sum = round(sum(b), 2)
        print(f"Profitti: lordo=\u20ac{a_sum:.2f} netto=\u20ac{b_sum:.2f}")
    else:
        print("Vendite non effettuate")
        print(f"Profitti: lordo=\u20ac{0:.2f} netto=\u20ac{0:.2f}")
            
                
# vegan_sell      
def vegan_sell(deposit, story_gross, story_net):
    """
    vegan_sell: taking a store dictionary "deposit", the function stores selling information
    """
    flag = 0
    sell_dict = {} # Sell dictionary
    
    while flag == 0:
        
        prod_name = str(input("Nome del prodotto: ")) # Product name
        
        if prod_name in deposit.keys():
            
            quantity = input("Quantità: ") # Quantity
        
            while quantity.isnumeric() != True or quantity[0 : 1] == "0": # Int number control 
                print("La quantità inserita non è valida")
                quantity = input("Reinserire la quantità: ")
            
            if int(quantity) <= int(deposit[prod_name][0]): # Check store availability
                
                # In case of reinsertion of a same product, the message has to be updated
                if prod_name not in sell_dict.keys():
                    sell_dict[prod_name] = [int(quantity), 
                                            float(deposit[prod_name][2]), 
                                            float(deposit[prod_name][1])]
                else:
                    update_quantity = int(quantity) + sell_dict[prod_name][0]
                    sell_dict[prod_name] = [update_quantity, 
                                            float(deposit[prod_name][2]), 
                                            float(deposit[prod_name][1])]
                
                # Updating the actual store quantity
                deposit[prod_name][0] = int(deposit[prod_name][0]) - int(quantity)
                    
            else:
                print("La quantità richiesta è maggiore a quella presente in magazzino"
                     f"\n {prod_name} in magazzino: {int(deposit[prod_name][0])}")
                
        else:
            print("Il prodotto inserito non c'è in magazzino")
        
        question = str(input("\nAggiungere un altro prodotto? (si/no): ")) # Question
        
        while question not in ("si", "no"):
            print("Il comando inserito non è corretto")
            question = str(input("\nAggiungere un altro prodotto? (si/no): ")) # Question

        # Question if-else flag clauses
        if question == "si":
            flag = 0 # Go to prod_name starting while
            
        elif question == "no":
            flag = 1
            
            if len(sell_dict) > 0:# Sell check
                print("VENDITA REGISTRATA")
                for k in sell_dict.keys():
                    print(f"- {sell_dict[k][0]} X {k}: {deposit[k][2]}") # Price store recall
                    
                #gross and net calculation and append
                sell_tot = vegan_gross(sell_dict)
                sell_net = sell_tot - vegan_net(sell_dict) 
                story_gross.append(sell_tot)
                story_net.append(sell_net)
                print(f"Totale: \u20ac{sell_tot:.2f}")
                
            else:
                print("Nessuna vendita inserita")
                
        else:
            flag = 0# Go to prod_name starting while
            print("Il comando inserito non è corretto")
