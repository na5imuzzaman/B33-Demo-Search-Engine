import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from b33_core.models import SearchHistory


@login_required()
def search_view(request):
    """

    This view has processed user's search keyword.
    Store the value to database along with current date + user.
    this view is also restricted to anonymous user


    """
    data = ""
    if request.method == "GET":
        data = request.GET.get('searchText')
        if data != "" and data != None:
            keyword = data.lower()
            SearchHistory.objects.create(user=request.user, keyword=keyword)

    if data == None:
        return render(request, 'search_page.html', {})
    else:
        return render(request, 'search_page.html', {'data': data})


@staff_member_required
def insight_view(request):

    """

    this view holds & process search data of every user, only allows to Staff & admin members.


    """

    users = User.objects.all()
    datas = SearchHistory.objects.all()

    data = {}
    for d in datas:
        val = SearchHistory.objects.filter(keyword__exact=d.keyword).count()
        data[d.keyword] = val

    return render(request, 'insights/insights.html', {
        'users': users,
        'history': data,
    })


@staff_member_required
def table_view(request):
    if request.is_ajax() or request.GET:

        """"

        Handle and process ajax call. Stablish a asynchronous connection between  frontend to backend.

        """

        found = request.GET.get('found', 0)
        time_range = request.GET.get('timeRange', 201)
        user_string = request.GET.get('user')
        user_list = []
        user_list = user_string.split(',')

        cal_date = datetime.now() - timedelta(days=int(time_range))
        print(user_string, found, time_range)

        # print(user_string)
        datas = SearchHistory.objects.filter(user__username__in=user_list,
                                             searched_date__gt=cal_date)

        data = {}
        for d in datas:
            val = SearchHistory.objects.filter(
                keyword__exact=d.keyword,user__username__in=user_list).count()
            if val >= int(found):
                data[d.keyword] = val
        data = json.dumps(data, indent=4)
        data = json.loads(data)
        return JsonResponse(data)
