from django.urls import path 
from . import views

urlpatterns = [
    path("listar_livros/",views.listar_livros,name="listar_livros" ),
    path("adicionar_livro/",views.adicionar_livro,name="adicionar_livro"),
    path("atualizar_livro/<int:id>",views.atualizar_livro,name="atualizar_livro"),
    path("deletar_livro/<int:id>",views.deletar_livro)
]