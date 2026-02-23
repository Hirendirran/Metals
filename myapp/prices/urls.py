from django.urls import path
from .views import home, all_prices, price_by_date, prices_by_year

urlpatterns = [
    path('', home),                              # HTML page
    path('prices/', all_prices),                 # all prices (10 years)
    path('prices/<date>/', price_by_date),       # date-wise
    path('prices/year/<int:year>/', prices_by_year),  # year-wise
]
