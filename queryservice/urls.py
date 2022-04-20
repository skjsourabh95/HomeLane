from django.contrib import admin
from django.urls import path
from queryservice import views
urlpatterns = [
    path('get_budgetHomes/',views.GetBudgetHomesView.as_view()),
    path('get_sqftHomes/',views.GetSqftHomesView.as_view()),
    path('get_ageHomes/',views.GetAgeHomesView.as_view()),
    path('get_standardPrices/',views.GetStandardPrices.as_view())
]