from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from contas.models import Perfil
from .models import Nota, Disciplina

@login_required
def dashboard(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)
    context = {'perfil': perfil}
    
    if perfil.tipo == 'ADMIN':
        return render(request, 'portal/admin_dash.html', context)
    elif perfil.tipo == 'PROF':
        return render(request, 'portal/prof_dash.html', context)
    else:
        context['notas'] = Nota.objects.filter(estudante=request.user).order_by('-data_lancamento')
        return render(request, 'portal/estudante_dash.html', context)

@login_required
def cadastrar_estudante(request):
    if request.user.perfil.tipo != 'ADMIN':
        return redirect('dashboard')
    if request.method == 'POST':
        u = request.POST.get('username')
        e = request.POST.get('email')
        p = request.POST.get('password')
        user = User.objects.create_user(username=u, email=e, password=p)
        Perfil.objects.create(user=user, tipo='ESTUDANTE')
        return redirect('dashboard')
    return render(request, 'portal/cadastrar_estudante.html')

@login_required
def lancar_nota(request):
    if request.user.perfil.tipo != 'PROF':
        return redirect('dashboard')
    if request.method == 'POST':
        est_id = request.POST.get('estudante')
        disc_id = request.POST.get('disciplina')
        val = request.POST.get('valor')
        Nota.objects.create(estudante_id=est_id, disciplina_id=disc_id, valor=val)
        return redirect('dashboard')
    
    context = {
        'estudantes': User.objects.filter(perfil__tipo='ESTUDANTE'),
        'disciplinas': Disciplina.objects.all(),
        'perfil': request.user.perfil
    }
    return render(request, 'portal/lancar_nota.html', context)



