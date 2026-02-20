from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import *
from django.contrib.auth import logout as django_logout

# Create your views here.
@login_required
def ticket_list(request):
    tickets= Ticket.objects.filter(user = request.user)

    output = ""
    for ticket in tickets:
        output += ticket.title + "\n"
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets
                                                       })

@login_required
def create_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST, user=request.user)
        if form.is_valid():
            ticket = form.save(commit = False)
            ticket.user = request.user
            ticket.save()
            return redirect('ticket_list')
    else:
        form = TicketForm(user = request.user)


    return render(request, 'tickets/create_ticket.html', {'form': form})    

@login_required
def edit_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id, user= request.user)

    if request.method =="POST":
        form = TicketForm(request.POST, instance=ticket, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
            form = TicketForm(instance=ticket, user=request.user)

    return render(request, 'tickets/create_ticket.html', {'form': form})

@login_required
def delete_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id, user =request.user)
    if request.method =="POST":
        ticket.delete()
        return redirect('ticket_list')

    return render(request, 'tickets/delete_ticket.html', {'ticket': ticket})

@login_required
def detail_ticket(request, id):
    ticket = get_object_or_404(Ticket, id =id, user =request.user)
    return render(request, 'tickets/detail_ticket.html', {'ticket': ticket})


@login_required
def logout_view(request):
    django_logout(request)
    return redirect("login")   
