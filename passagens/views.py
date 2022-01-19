from django.shortcuts import render
from passagens.forms import PassagemForms, PessoaForms
# Create your views here.
def index(request):
    form = PassagemForms()
    contexto = {'form':form}
    return render(request, 'index.html',contexto)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        pessoa_forms = PessoaForms(request.POST)
        pessoa_forms = PessoaForms() 
        if form.is_valid(): 
            contexto = {'form':form,'pessoa_form':pessoa_forms}
            return render(request, 'minha_consulta.html', contexto)
        else:
            print('Fomulário inválido')
            contexto = {'form':form,'pessoa_form':pessoa_forms}
            return render(request, 'index.html', contexto)