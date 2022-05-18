from django.shortcuts import redirect, render
from myapp.models import Enquiry
from myapp.models import Complaint
from myapp.models import Feedback
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def products(request):
    return render(request, "products.html")

def services(request):
    return render(request, "services.html")

def videos(request):
    return render(request, "videos.html")

def gallery(request):
    return render(request, "gallery.html")

def contact(request):
    return render(request, "contact.html")

def enquiry(request):
    if request.method=="POST":
        pro_code=request.POST.get("pro_code")
        name=request.POST.get("name")
        email=request.POST.get("email")
        number=request.POST.get("number")
        address=request.POST.get("address")
        city=request.POST.get("city")
        state=request.POST.get("state")
        p_code=request.POST.get("p_code")
        company=request.POST.get("company")
        query=request.POST.get("query")
        file=request.FILES['file']
        data=Enquiry(productCode=pro_code, name=name, email=email, mobile=number, address=address, city=city, state=state, postalCode=p_code, company=company, query=query, file=file)
        data.save()
        messages.success(request, "Your Enquiry has been sent.")
    return render(request, "enquiry.html")

def complaint(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        number=request.POST.get("number")
        company=request.POST.get("company")
        address=request.POST.get("address")
        city=request.POST.get("city")
        state=request.POST.get("state")
        p_code=request.POST.get("p_code")
        i_name=request.POST.get("i_name")
        i_code=request.POST.get("i_code")
        file=request.FILES['file']
        data=Complaint(name=name, email=email, mobile=number,company=company, address=address, city=city, state=state, postalCode=p_code, itemName=i_name, itemCode=i_code ,file=file)
        data.save()
        messages.success(request, "Your Complaint has been sent.")
    return render(request, "complaint.html")

def feedback(request):
    if request.method=="POST":
        p_quality=request.POST.get("p_quality")
        p_delivery=request.POST.get("p_delivery")
        p_communication=request.POST.get("p_communication")
        p_behaviour=request.POST.get("p_behaviour")
        p_paperwork=request.POST.get("p_paperwork")
        p_inner=request.POST.get("p_inner")
        p_outer=request.POST.get("p_outer")
        p_c=request.POST.get("p_c")
        comment=request.POST.get("comment")
        company=request.POST.get("company")
        email=request.POST.get("email")
        number=request.POST.get("number")
        dealer=request.POST.get("dealer")
        goods=request.POST.get("goods")
        data=Feedback(productQuality=p_quality, productDelivery=p_delivery, communication=p_communication, behaviour=p_behaviour, paperwork=p_paperwork, packingInnerQuality= p_inner, packingOuterQuality=p_outer, presentationAndCatalogues=p_c, comment=comment, company=company,email=email, mobile=number, dealerName=dealer, goods=goods)
        data.save()
        messages.success(request, "Your Feedback has been sent.")
    return render(request, "feedback.html")


def replytoclient(request):
    if request.user.is_anonymous:
        return redirect("/")
    else:
        if request.method=="POST":
            object=request.POST.get("object")
            model_name=object[0:object.find(" ")]
            reply=request.POST.get("reply")
            msg_title=request.POST.get("msg_title")
            def mail(email):
                send_mail(
                            msg_title,
                            reply,
                            settings.EMAIL_HOST_USER,
                            [email],
                            fail_silently=False,
                        )
            if model_name=="Enquiry":
                enq=Enquiry.objects.all()
                for e in enq:
                    if str(e)==object:
                        ema=e.email
                        mail(ema)
                        e.replyMailSent="done"
                        e.save()
            if model_name=="Complaint":
                com=Complaint.objects.all()
                for c in com:
                    if str(c)==object:
                        ema=c.email
                        mail(ema)
                        c.replyMailSent="done"
                        c.save()
            if model_name=="Feedback":
                feed=Feedback.objects.all()
                for f in feed:
                    if str(f)==object:
                        ema=f.email
                        mail(ema)
                        f.replyMailSent="done"
                        f.save()
            messages.success(request, f"Your mail has been sent to the client of email id : {ema}")
        return render(request, "replytoclient.html")