from classes.restaurante import Restaurante
from classes.cardapio.bebida import Bebida
from classes.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melância', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_pao = Prato('Paozinho', 2.00, 'O Melhor Pão da Cidade')
prato_pao.aplicar_desconto()

restaurante_praca.adicionar_carpadio(bebida_suco)
restaurante_praca.adicionar_carpadio(prato_pao)


def main():
    restaurante_praca.exibir_cardapio
if __name__ == '__main__':
    main()