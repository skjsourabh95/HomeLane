from rest_framework.views import APIView
from rest_framework.response import Response
import json
from dataservice import views
# Create your views here.

class GetBudgetHomesView(APIView):
    def get(self,request):
        file_obj = request.FILES['json_file']  # fetch json input file
        data = json.loads(file_obj.read())
        response = views.db_search(data) # call data service
        return response

class GetSqftHomesView(APIView):
    def get(self,request):
        file_obj = request.FILES['json_file']  # fetch json input file
        data = json.loads(file_obj.read())
        response = views.db_search(data) # call data service
        return response

class GetAgeHomesView(APIView):
    def get(self,request):
        file_obj = request.FILES['json_file']  # fetch json input file
        data = json.loads(file_obj.read())
        response = views.db_search(data) # call data service
        return response


class GetStandardPrices(APIView):
    def get(self,request):  
        response = views.db_search({}) # call data service
        return response