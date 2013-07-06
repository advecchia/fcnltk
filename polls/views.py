from django.http import HttpResponse
from django.shortcuts import render
import nltk

#    Classe Dispatcher: responsavel pela escolha de qual caminho sera 
# seguido pela requisicao do usuario.
class Dispatcher(object):
    def __init__(self, request, path, text):
        self._request = request
        self._path = path
        self._text = text
        self._view = ""

    # dispatch: metodo que seleciona um dos caminhos possiveis para a visao.
    def dispatch(self):
        if (self._path == "lista"):
            self._text = nltk.word_tokenize(self._text)
            return render(self._request, 'polls/lista.html', {'view': self._text})
        elif (self._path == "ngramas"):
            self._text = nltk.ngrams(nltk.word_tokenize(self._text), 3)
            return render(self._request, 'polls/ngramas.html', {'view': self._text})
        else:
            return render(self._request, 'polls/default.html', {'view': self._text})

#    Classe FrontController: fica responsavel por receber as requisicoes e fazer 
# verificacoes, como senhas, sessao, etc. No exemplo ela nao faz nada disso,
# porem gera a chamada para a classe Dispatcher que ira direcionar o usuario 
# para a pagina desejada.
class FrontController(object):
    def __init__(self, request, path, text):
        self._request = request
        self._path = path
        self._text = text
        self._dispatcher = Dispatcher(self._request, self._path, self._text)

    def dispatcher_request(self):
        return self._dispatcher.dispatch()

def front_controller(request, called_path):
    #verifica por exemplo questoes de seguranca, sessao, etc
    # ...
    # chama o dispatcher, que ira fazer o acesso a visao desejada:

    text = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Typi non habent claritatem insitam; est usus legentis in iis qui facit eorum claritatem. Investigationes demonstraverunt lectores legere me lius quod ii legunt saepius. Claritas est etiam processus dynamicus, qui sequitur mutationem consuetudium lectorum. Mirum est notare quam littera gothica, quam nunc putamus parum claram, anteposuerit litterarum formas humanitatis per seacula quarta decima et quinta decima. Eodem modo typi, qui nunc nobis videntur parum clari, fiant sollemnes in futurum."
    fc = FrontController(request, called_path, text)
    return fc.dispatcher_request()

#    Visao inicial do sistema com escolhas entre usar os links em modo padrao ou
# utilizando o FrontController.
def index(request):
    return render(request, 'polls/index.html')

#    Visao que apresenta uma lista de palavras extraidas de um texto.
def lista(request):
    text = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Typi non habent claritatem insitam; est usus legentis in iis qui facit eorum claritatem. Investigationes demonstraverunt lectores legere me lius quod ii legunt saepius. Claritas est etiam processus dynamicus, qui sequitur mutationem consuetudium lectorum. Mirum est notare quam littera gothica, quam nunc putamus parum claram, anteposuerit litterarum formas humanitatis per seacula quarta decima et quinta decima. Eodem modo typi, qui nunc nobis videntur parum clari, fiant sollemnes in futurum."
    text = nltk.word_tokenize(text)
    return render(request, 'polls/lista.html', {'view': text})

#    Visao que apresenta um conjunto de n-gramas de tamanho 3.
def ngramas(request):
    text = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Typi non habent claritatem insitam; est usus legentis in iis qui facit eorum claritatem. Investigationes demonstraverunt lectores legere me lius quod ii legunt saepius. Claritas est etiam processus dynamicus, qui sequitur mutationem consuetudium lectorum. Mirum est notare quam littera gothica, quam nunc putamus parum claram, anteposuerit litterarum formas humanitatis per seacula quarta decima et quinta decima. Eodem modo typi, qui nunc nobis videntur parum clari, fiant sollemnes in futurum."
    text = nltk.ngrams(nltk.word_tokenize(text), 3)
    return render(request, 'polls/ngramas.html', {'view': text})
