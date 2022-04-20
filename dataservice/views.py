from dataservice.models import Data
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
def calculate_sp(res):
    """Caculating the Standard Prices"""
    new_price = (((res.bedrooms * res.bathrooms * (res.sqft_living / res.sqft_lot) * res.floors)+ res.waterfront + res.view) * res.condition * ( res.sqft_above + res.sqft_basement) - 10 * (2022 - max(res.yr_built,res.yr_renovated))) * 100
    return new_price

def create_output_json(results,standard=False):
    """Creating output json"""
    output = []
    for res in results:
        response = {}
        if standard:
            # if standrd prices are fetched
            response['price'] = calculate_sp(res)
        else:
            response['price'] = res.price
        response['date'] = res.date
        response['bedrooms'] = res.bedrooms
        response['bathrooms'] = res.bathrooms
        response['sqft_living'] = res.sqft_living
        response['sqft_lot'] = res.sqft_lot
        response['floors'] = res.floors
        response['waterfront'] = res.waterfront
        response['view'] = res.view
        response['condition'] = res.condition
        response['sqft_above'] = res.sqft_above
        response['sqft_basement'] = res.sqft_basement
        response['yr_built'] = res.yr_built
        response['yr_renovated'] = res.yr_renovated
        response['street'] = res.street
        response['city'] = res.city
        response['statezip'] = res.statezip
        response['country'] = res.country
        
        output.append(response)

    return output

# Create your views here.
def db_search(request):   
    """Common Db Search function based on request arguments""" 

    if 'maxPrice' in request and 'minPrice' in request:
        # fetching Budget Homes
        criterion1 = Q(price__lte=float(request['maxPrice']))
        criterion2 = Q(price__gte=float(request['minPrice']))
        results = Data.objects.filter(criterion1 & criterion2)
        resp = create_output_json(results)
    elif 'minSqft' in request:
        # Fetching Sqft Homes
        criterion = Q(sqft_living__gte=float(request['minSqft']))
        results = Data.objects.filter(criterion)
        resp = create_output_json(results)
    elif 'year' in request:
        # Fetching Age Homes
        criterion1 = Q(yr_built__gt=request['year'])
        criterion2 = Q(yr_renovated__gt=request['year'])
        results = Data.objects.filter(criterion1 | criterion2)
        resp = create_output_json(results)
    else:
        # Fetching Standard prices
        results = Data.objects.all()
        resp = create_output_json(results,True)

    return Response({"response":resp}, status = status.HTTP_200_OK)
