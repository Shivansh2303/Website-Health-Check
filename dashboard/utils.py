from django.core.mail import send_mail

def statusMail(data):
    send_mail(subject="Website Health Status",
              message="The website having some issue, Please contact the site administrator", 
              from_email='shivash@mail.com', 
              recipient_list=[data['to_email'],],
              fail_silently=False
              )