# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post, Visual
from django.http import HttpResponse
import json
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

def post_list(request):
    posts = Post.objects.filter(published_date__gte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def chart(request):
    if request.method == 'GET':
        vis = Visual.objects.all()

        vis_list = []

        for v in vis:
            vis_dict = dict()
            vis_dict['name'] = v.name
            vis_dict['age'] = v.age
            vis_list.append(vis_dict)

        return HttpResponse(json.dumps(vis_list), content_type='application/json')

    return HttpResponse("Not Working")   

@csrf_exempt
def register(request):
    return render(request, "blog/chart_list.html") 