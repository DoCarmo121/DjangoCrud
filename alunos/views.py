from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno

#CREATE and READ
def criar_aluno(request):
    if request.method == 'GET':
        alunos = Aluno.objects.all()
        return render(request, 'criar_alunos.html', {'alunos': alunos})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        aluno = Aluno(nome=nome, email=email)
        aluno.save()
        return redirect('criar_aluno')

#DELETE
def deletar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect('criar_aluno')

def atualizar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.nome = request.POST.get('nome')
    aluno.email = request.POST.get('email')
    aluno.save()
    return redirect('criar_aluno')
