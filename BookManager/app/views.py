from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Book



#Serve como um protetor no qual nao vai permitir interceptacoes no meio da requisicao do
#usuario
@csrf_exempt
def listar_livros(request):
    livros = Book.objects.all().values()
    if request.method == 'GET':
        return HttpResponse(list(livros) )
    else:
        return JsonResponse({'erro':'requisicao Invalida'}, status = 405)


@require_http_methods(["POST"])       
@csrf_exempt
def adicionar_livro(request):
    if request.method == "POST":

        dados = json.loads(request.body)
        print(dados)
        livro = Book.objects.create(
            titulo = dados.get("titulo"),
            autor = dados.get("autor"),
            data_publicacao = dados.get("data_publicacao"),
            numero_paginas = dados.get("numero_paginas")
        )
        return JsonResponse({"id":livro.id,"mensagem":"Livro adicionado com sucesso ! ! !"})
    


@csrf_exempt
@require_http_methods(["PUT"])       
def atualizar_livro(request,id):
    try:
        if request.method == "PUT":
            livro = Book.objects.get(id = id )
            #carregando os dados do corpo da requisição do json
            dados = json.loads(request.body)
            
            livro.titulo = dados.get("titulo",livro.titulo)
            livro.autor = dados.get("autor",livro.autor)
            livro.data_publicacao = dados.get("data_publicacao",livro.data_publicacao)
            livro.numero_paginas = dados.get("numero_paginas",livro.numero_paginas)

            # para salvar as alterações no nosso banco de dados precisamos dar o comando save

            livro.save()
            return JsonResponse({"mensagem":"Livro atualizado com sucesso"})
    except Book.DoesNotExist:
        return JsonResponse({"erros":"Id do livro não encontrado"},status=404)


@csrf_exempt
@require_http_methods(["DELETE"])    

def deletar_livro(request,id):
    try:
        if request.method == "DELETE":
            livro = Book.objects.get(id = id )
            #carregando os dados do corpo da requisição do json
            
            livro.delete()
            
            
            return redirect('listar_livros')

    except Book.DoesNotExist:
        return JsonResponse({"error":"Id do livro não encontrado"},status=404)
        

