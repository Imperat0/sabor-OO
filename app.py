from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Daniel', 10)
restaurante_praca.receber_avaliacao('Paulo', 8)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
