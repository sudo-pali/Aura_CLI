import time

    
def main():

    aura = 0

    user = input('Pressione "Enter" e veja sua aura: ')



    aura_mais = 'Parabéns sua aura é de:'

    aura_menos = 'Aura negativa, eu disse pressione "Enter"'



    if user == "":

        contagem = 1

    else:

        contagem = -1




    while True:

        if user == "":
    
            print(f'{aura_mais} {aura:+}', end='\r')

        else:
        
            print(f'L sua aura é de:{aura}', end='\r')
        


        aura += contagem

        time.sleep(0.0001)

        if aura == 10000 or aura == -10000:

            break



    print()



    if user != "":


        print(f'{aura_menos}')



    print()

if __name__ == "__main__":
    main()