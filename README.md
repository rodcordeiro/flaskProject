## PROJETO FLASK ##

O projeto trata-se de um miniblog para estudo do Flask, Webframework do python.

Para trabalhar com o Flask, criamos um app, que nos permite através de pacotes e classes
Criamos a página microblog, que serve para iniciar o app
--------------------------------------
 1. #### **app** - Pasta que contém o pacote contendo a aplicação

   1. **templates** - Pasta contendo os templates das páginas exibidas;

   1. *\_\_init\_\_.py*:
    Inicia o pacote. Sempre que trabalhamos com pacotes, existe a possibilidade de deixar o script \_\_init\_\_.py, pois o python por padrão irá buscar ele.Nele está criado nosso app.

   1. *forms.py*
    Nele estão as classes utilizadas para gerar os formulários através do WTForms.
    Cada formulário está em uma classe.

  1. *routes.py*
    O flask trabalha por rotas, ou seja, quando você digita a url localhost.com/index, o /index é a rota.

 1. #### *config.py*:
 1. #### *microblog.py*:
