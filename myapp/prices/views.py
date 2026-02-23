from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from prices.models import MetalPrice


# Frontend HTML
def home(request):
    return render(request, "prices/index.html")


# API: All prices (10 years)

def all_prices(request):
    prices = MetalPrice.objects.all().order_by('date')

    data = []
    for p in prices:
        data.append({
            "date": p.date.strftime("%Y-%m-%d"),
            "gold": float(p.gold),
            "silver": float(p.silver),
            "platinum": float(p.platinum),
            "diamond": float(p.diamond)
        })

    return JsonResponse(data, safe=False)



# API: Price by specific date

def price_by_date(request, date):
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
        price = MetalPrice.objects.get(date=parsed_date)

        return JsonResponse({
            "date": price.date.strftime("%Y-%m-%d"),
            "gold": float(price.gold),
            "silver": float(price.silver),
            "platinum": float(price.platinum),
            "diamond": float(price.diamond)
        })

    except MetalPrice.DoesNotExist:
        return JsonResponse(
            {"error": "No data found for selected date"},
            status=404
        )

    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=500
        )



# API: Prices by year (NEW – 10 years support)

def prices_by_year(request, year):
    prices = MetalPrice.objects.filter(date__year=year).order_by('date')

    data = []
    for p in prices:
        data.append({
            "date": p.date.strftime("%Y-%m-%d"),
            "gold": float(p.gold),
            "silver": float(p.silver),
            "platinum": float(p.platinum),
            "diamond": float(p.diamond)
        })

    def price_by_date(request, date):
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d").date()

            price = MetalPrice.objects.filter(date=parsed_date).first()

            if not price:
                return JsonResponse(
                    {"error": f"No data found for {parsed_date}"},
                    status=404
                )

            return JsonResponse({
                "date": price.date.strftime("%Y-%m-%d"),
                "gold": float(price.gold),
                "silver": float(price.silver),
                "platinum": float(price.platinum),
                "diamond": float(price.diamond)
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

