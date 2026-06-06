from django.shortcuts import render
from django.http import JsonResponse
from .services import get_weather


def dashboard_view(request):
    return render(request, "dashboard/index.html")


def weather_view(request):
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")

    if not lat or not lon:
        return JsonResponse({"error": "lat and lon required"}, status=400)

    data = get_weather(
        lat=lat,
        lon=lon,
        days=int(request.GET.get("days", 7)),
        ai=request.GET.get("ai", "true").lower() == "true"
    )

    return JsonResponse(data)