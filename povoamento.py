from cliente.models import *
from pedido.models import *
from produto.models import *
from random import randrange
from datetime import timedelta
from random import randint
from datetime import datetime
from ecrawler.models import *
from ecrawler.views import crawl

def random_date(start, end):
    return start + timedelta(
        seconds=randint(0, int((end - start).total_seconds())))

def random_photo():

	drafts = Draft.objects.all()
	random_index = randint(0, int((len(drafts) - 1)))

	return drafts[random_index].photo

#para rodar, abra python manage.py shell, e digite execfile('povoamento.py')

Endereco.objects.all().delete()
Cliente.objects.all().delete()
Produto.objects.all().delete()
Despesa.objects.all().delete()
Pedido.objects.all().delete()
Draft.objects.all().delete()

#Forcing download of all images from botmail.
crawl(True)


startDate = datetime.strptime('20/08/2013 1:30 PM', '%d/%m/%Y %I:%M %p')
endDate = datetime.strptime('28/09/2013 1:30 PM', '%d/%m/%Y %I:%M %p')

nomes = ['Nicolle Chaves Cysneiros', 'Rafael Lucena de Oliveira', 'Roberta Cabral', 'Joao Lucas de Miranda', 'Ermano Ardiles Arruda', 'Jose Luiz Correa', 'Fanny Chien', 'Mariama Oliveira', 'Luiz Vasconcelos', 'Brunete Soares']
for i in range(0,10):
	#Endereco(logradouro, complemento, bairro, cidade, cep)
	e = Endereco(logradouro='logradouro%d'%i, complemento='complemento%d'%i, bairro='bairro%d'%i, cidade='cidade%d'%i, cep='cep%d'%i)
	e.save()

	#Cliente (cpf, nome, email, Endereco, telResidencial, telCelular, juridico)
	c = Cliente(id=i, nome=nomes[i], email='email@email.com%d'%i, endereco=e, telResidencial='3333-3333', telCelular='8888-8888', juridico=False)
	c.save()

	#Produto (valor, descricao, Cliente, data, tamanho, categoria, foto, titulo, portfolio)
	if (i%2 == 0):
		dataProduto = random_date(startDate,datetime.now())
		p = Produto(valor=randint(10,200), descricao='descProduto%d'%i, cliente=c, data=dataProduto, tamanho='mm', categoria='categoria', titulo='tituloProduto%d'%i, portfolio=False, foto = random_photo())
		p.save()
	else:
		p = Produto(valor=randint(10,200), descricao='descProduto%d'%i, cliente=None, data=None, tamanho='mm', categoria='categoria', titulo='tituloProduto%d'%i, portfolio=True, foto = random_photo())
		p.save()
	
	
	#Pedido (valor, descricao, Cliente, data, prazo, desenho)
	dataPrazo = random_date(startDate,endDate)
	dataPedido = random_date(startDate,datetime.now())
	pe = Pedido(valor=randint(10,500), descricao='descPedido', cliente=c, data=dataPedido, prazo=dataPrazo, desenho = random_photo())
	pe.save()

	#Despesa (valor, fornecedor, descricao, Servico, data)
	for j in range(0,5):
		dataDespesa1 = random_date(startDate,datetime.now())
		d1 = Despesa(valor=randint(5,50), fornecedor='fornecedor%d'%i, descricao='descDespesaProduto%d'%i, servico=p, data=dataDespesa1)
		d1.save()

		dataDespesa2 = random_date(startDate,datetime.now())
		d2 = Despesa(valor=randint(5,50), fornecedor='fornecedor%d'%i, descricao='descDespesaPedido%d'%i, servico=pe, data=dataDespesa2)
		d2.save()
	
