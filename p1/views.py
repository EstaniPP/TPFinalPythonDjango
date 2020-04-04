from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
def saludo(request):
    return render(request,"index.html")

def signup(request):
    if request.method=="POST":
        message = "" + request.POST["text"] + "" + request.POST["email"] + "" + request.POST["tel"] +  "" + request.POST["pass"]
        subject= "Registrado exitosamente"
        emailfrom= settings.EMAIL_HOST_USER
        recipient_list=[request.POST["email"]]

        send_mail(subject,message, emailfrom, recipient_list)
        return render(request,"operacion_finalizada.html", {"operacion":"signup"})

    return render(request,"signup.html")

def frgotpass(request):
    if request.method=="POST":
        message = "Usted ha solicitado un nuevo password ya que perdio el suyo. Lamento informarle que esta funcionalidad no ha sido implementada aun. Saludos"
        subject= "Pedido de password nuevo"
        emailfrom= settings.EMAIL_HOST_USER
        recipient_list=[request.POST["text"]]

        send_mail(subject,message, emailfrom, recipient_list)
        return render(request,"operacion_finalizada.html", {"operacion":"frgotpass"})

    return render(request,"frgotpass.html")

def operacion_finalizada(request,operacion):
    return render(request,"frgotpass.html")