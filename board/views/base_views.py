'''
파일명 : base_views.py
설 명 :
생성일 : 2023-02-14
생성자 : user
since 2023.01.09 Copyright (C) by KandJang All right reserved.
'''


import logging

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from ..models import Board


def index(request):
    board_list = Board.objects.order_by('-create_date')  # order_by('-필드') desc, asc order_by('필드')
    context = {'board_list': board_list}
    logging.info('board_list:{}'.format(board_list))

    return render(request, 'board/board_list.html', context)
