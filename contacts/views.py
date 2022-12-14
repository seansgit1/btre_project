from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact 

def contact(request):
    if request.method=='POST':
        print('HELLO')
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']

        # check if user has already made an Inquiry
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)

        contact.save()

        # Send Mail
        # send_mail (
            # 'Property listing inquiry',
           #  'There has been an Inquiry for :' + listing + '. Sign into the admin panel fro more info ',
           #  'simon.small141@gmail.com',
          #   [realtor_email,'simon.small141@gmail.com'],
           #  fail_silently=False
       #  )
        
        messages.success(request,'Your request has been submitted, a realtor will get back to your soon')

        return redirect('/listings/' + listing_id)



