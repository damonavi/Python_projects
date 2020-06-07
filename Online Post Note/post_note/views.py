from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegisterForm, LoginForm, PatchCard
from .models import Users, Desc
from django.core.mail import send_mail

# Create your views here.
# Create your views here.

def cards(request, my_id):
    if request.method == "POST":
        my_user = Users.objects.get(id=my_id)
        form = PatchCard(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = my_user
            form_obj.save()
            return redirect(user_home,my_id=my_user.id)

    else:
        my_user = Users.objects.get(id=my_id)
        form = PatchCard()
    return render(request, 'post_note/add_desc.html', {'form': form, 'user': my_user})

def register(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            u = form.save()
            return redirect(login)
    else:
        form = RegisterForm()
    return render(request, 'post_note/register.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            p = Users.objects.get(username = form.cleaned_data.get('my_username'))
            return redirect(user_home,my_id=p.id)
    else:
        form = LoginForm()
    return render(request,'post_note/login.html',{'form': form})


def home_page(request):
    return render(request,'post_note/home_page.html')

def user_home(request,my_id):
    op = Users.objects.get(id=my_id)
    total = Desc.objects.filter(user=op)
    return render(request, 'post_note/user_page.html', {'user': op, 'tot': total})

def card_desc(request,my_id,card_id):
    op = Users.objects.get(id=my_id)
    total = Desc.objects.filter(user=op)
    cd = total.get(id=card_id)
    return render(request,'post_note/card_desc.html',{'user': op, 'obj': cd})

def card_delete(request,my_id,card_id):
    op = Users.objects.get(id=my_id)
    total = Desc.objects.filter(user=op)
    cd = total.get(id=card_id).delete()
    return redirect(user_home,my_id=my_id)

def send_mail(request, my_id, card_id):
    op = Users.objects.get(id=my_id)
    total = Desc.objects.filter(user=op)
    cd = total.get(id=card_id)

    send_mail(
        cd.title,
        cd.description,
        'jhacoolabhishek@gmail.com',
        [op.email],
    )

    return redirect(user_home, my_id=my_id)

def user_info(request,my_id):
    x = Users.objects.get(id=my_id)
    return render(request, 'post_note/user_info.html', {'user': x})
