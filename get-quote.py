import random

def primary():
 #print("Keep it logically awesome.")

  ############## Eliminar espacios #########################
  
  f = open("quotes.txt",'r',encoding='utf-8')
  quotes = f.readlines()
  f.close()
  qty = int(input("Ingresar cantidad de frases: "))
  for i in range(0,qty):
    rnd=random.randint(0, len(quotes)-1)
    rnd_quote=quotes[rnd]
    print(rnd_quote,end='')


  ############### Cantidad de frases aleatorias ############
  #f = open("quotes.txt",'r',encoding='utf-8')
  #quotes = f.readlines()
  #f.close()
  #qty = int(input("Ingresar cantidad de frases: "))
  #for i in range(0,qty):
  #  rnd=random.randint(0, len(quotes)-1)
  #  rnd_quote=quotes[rnd]
  #  print(rnd_quote)

  ############## Agregar frases ############################

  #f = open("quotes.txt",'a+')
  #new_quote = input("Ingresar frase: ")
  #f.write(new_quote + '\n')
  #f.close()
   
  ############# Leer frases random ########################
  #f = open("quotes.txt")
  #quotes = f.readlines()
  #f.close()
  #last=13
  #rnd=random.randint(0, last)
  #print(quotes[rnd])

if __name__== "__main__":
  primary()
