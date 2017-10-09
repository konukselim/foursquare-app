# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import History
from models import TableData
import json
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from foursquare_api import FoursquareSearchRequest
from django.views import generic, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.serializers.json import DjangoJSONEncoder

class IndexView(View):
    def __init__(self):
        self.template_name = '../templates/mat.html'
        self.response_elements = {}
        
    def get(self, request):
        print request.GET
        self.histories = History.objects.order_by('-search_date').values_list('id','item', 'location')[:20]
        self.response_elements['histories'] = json.dumps(list(self.histories), cls=DjangoJSONEncoder)
        return render(request, self.template_name, self.response_elements)

    def post(self, request):
        if request.method == "POST":
            if 'search_btn' in request.POST:
                look_for = request.POST.get('look_for' , None)
                location = request.POST.get('location', None)
                resp = FoursquareSearchRequest().getVenuesInfo(look_for, location)
                f = self.fill_table(resp)
                if f:
                    a = History(item = look_for, location = location, search_date = timezone.now())
                    a.save()
                    for h in f:
                        b = TableData(venue_name=h['name'], url=h['url'], phone_number=h['phoneNumber'], checkin_count=h['checkinCount'], history_id=a.pk)
                        b.save()
                self.histories = History.objects.order_by('-search_date').values_list('id','item', 'location')[:20]
                self.response_elements['tableData'] = f
                self.response_elements['histories'] = json.dumps(list(self.histories), cls=DjangoJSONEncoder)
            elif 'get_history_btn' in request.POST:
                h_id= request.POST.get('history_id', None)
                self.histories = History.objects.order_by('-search_date').values_list('id', 'item', 'location')[:20]
                print self.histories
                a = 0
                for history in self.histories:
                    print h_id, history[0]
                    if int(h_id) == int(history[0]):
                        print "aaaaaa"
                        break
                    a = a + 1

                page_number = (a / 10) + 1
                print page_number

                db_histories = TableData.objects.filter(history_id=h_id)
                f = self.fill_table_db(db_histories)
                self.histories = History.objects.order_by('-search_date').values_list('id','item', 'location')[:20]
                self.response_elements['histories'] = json.dumps(list(self.histories), cls=DjangoJSONEncoder)
                self.response_elements['tableData'] = f
                self.response_elements['page_number'] = page_number
        else:
            print "404"

        return render(request, self.template_name, self.response_elements)

    def fill_table(self, resp):
        datas = []
        api_response = resp['response'].get('venues', '')
        if api_response:
            for venue in api_response:
                data = {}
                data['name'] = venue.get('name', '-')
                data['phoneNumber'] = venue['contact'].get('formattedPhone', "-")
                data['checkinCount'] = venue['stats'].get('checkinsCount' , "-")
                data['url'] = venue.get('url' , '')    
                datas.append(data)

        return datas

    def fill_table_db(self, db_data):
        datas = []
        for d in db_data:
            data = {}
            data['name'] = d.venue_name
            data['phoneNumber'] = d.phone_number
            data['checkinCount'] = d.checkin_count
            data['url'] = d.url
            datas.append(data)
        
        return datas
