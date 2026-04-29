import pytest
from domain.produto import Produto
from domain.pedido import Pedido
from domain.cliente import Cliente
def test_produto_valor_negativo():
    with pytest.raises(ValueError):
        Produto(codigo=1, valor=-5, tipo=1)

def test_qtd_max_produtos():
    produtoTest=Produto(codigo=2,valor=20,tipo=1,desconto_percentual=15.0)
    clienteTest=Cliente(cpf=12345678910,nome="Jurema")
    pedidoTest=Pedido(cliente=clienteTest,qtd_max_produtos=2)
