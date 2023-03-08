from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import UserForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import logging
import qrcode
from django.core.files.storage import FileSystemStorage
import os
from django.http import FileResponse
# Create your views here.



def download(request):
    logging.info('1. download')

    param_file =request.GET['file_name']
    logging.info('2. param_file:{}'.format(param_file))

    file_path = os.path.abspath("C:/projects/mysite/media/")
    file_name = os.path.basename("C:/projects/mysite/media/"+param_file)
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_name, 'rb'),
                            content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = "attachment; filename="+param_file

    return response


def upload(request):
    logging.info('1. upload')
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)


        file_url = fss.url(file)
        logging.info('2. file_url:{}'.format(file_url))

        return render(request, 'common/upload.html', {'file_url': upload})
    return render(request, 'common/upload.html')

def sendmail_param(request):
    '''naver smtp attach'''
    logging.info('1. sendmail_attach')

    logging.info('2. file_path')


    flag = 0 #
    context ={}

    if request.method == "POST":  # 수정

        subject_text = request.POST['subject']
        content_text = request.POST['content']
        to_text = request.POST['to']

        logging.info('3.1 subject_text{}:'.format(subject_text))
        logging.info('3.1 content_text{}:'.format(content_text))
        logging.info('3.1 to_text{}:'.format(to_text))


        email = EmailMessage(
            subject = subject_text,
            body    = content_text,
            from_email="jamesol@naver.com",
            to=["jamesol@paran.com", to_text]
        )

        flag = email.send()
        logging.info('3. sendmail_attach flag{}:'.format(flag))
    else:
        flag = 0

    context = {'flag': flag}

    return render(request, 'common/mail_form.html',context)


def sendmail_attach(request):
    '''naver smtp attach'''
    logging.info('1. sendmail_attach')

    img_url = qrcode.make("https://cafe.daum.net/pcwk")
    file_path = "C:/projects/mysite/static/images/pcwk99.png"
    img_url.save(file_path)
    logging.info('2. file_path')



    email = EmailMessage(
        subject="첨부파일 테스트",
        body="내용",
        from_email="jamesol@naver.com",
        to=["jamesol@paran.com","hykim22@gmail.com"]
    )
    email.attach_file(file_path,'image/png')
    flag = email.send()
    logging.info('3. sendmail_attach flag{}:'.format(flag))
    return HttpResponse('sendmail_attach flag:'+str(flag))

def sendmail(request):
    '''naver smtp사용'''
    logging.info('1. sendmail')

    flag = send_mail(
        'Subject:제목',
        'Here is the message.',
        'jamesol@naver.com',
        ['jamesol@paran.com'],
        fail_silently=False
    )
    logging.info('2. flag:{}'.format(flag))
    return HttpResponse('send_email flag:'+str(flag))



def signup(request):
    '''회원가입'''

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid(): #post방식에서 form이 유효한 경우
           #회원가입
           form.save()
           #form username, password1
           username = form.cleaned_data.get('username')
           logging.info('username:{}'.format(username))

           password1 = form.cleaned_data.get('password1')
           logging.info('password1:{}'.format(password1))

           user = authenticate(username=username, password=password1)
           #로그인
           login(request,user)

           return redirect('index')
    else:
        form = UserForm()
    return render(request,'common/signup.html',{'form':form})
