'''
파일명 : urls.py
설 명 :  board url
생성일 : 2023-02-14
생성자 : user
since 2023.01.09 Copyright (C) by KandJang All right reserved.
'''
from django.contrib import admin
from django.urls import path,include
from board.views import base_views
urlpatterns = [
    #bash_view
    path('',base_views.index,name='index'), #view index로 메핑
    #path('<int:question_id>/', base_views.detail, name='detail'),

    #answer
    #path('answer/create/<int:question_id>/',answer_views.answer_create, name='answer_create'),
    #path('answer/modify/<int:answer_id>/',answer_views.answer_modify, name='answer_modify'),
    #path('answer/delete/<int:answer_id>/',answer_views.answer_delete, name='answer_delete'),

]