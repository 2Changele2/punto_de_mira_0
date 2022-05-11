import matplotlib.pyplot as plt





def punto_de_mira(lista_de_coordenadas):
    for coordenadas in lista_de_coordenadas:
        plt.plot ([2, 2, 0, 4], [1, 16, 9, 9],'bo')

        
    
    plt.plot(2, 9, 'k+')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.show()


if __name__ == '__main__':
    lista_de_coordenadas = [ 0, 1 ]
    punto_de_mira(lista_de_coordenadas)
