from django.views import generic

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import requests
from django.conf import settings
from users.models import Cat, Breed



class IndexView(generic.TemplateView):
    template_name = "common/index.html"


class RestViewSet(viewsets.ViewSet):
    @action(
        detail=False,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="rest-check",
    )
    def rest_check(self, request):
        return Response(
            {
                "result": "This message comes from the backend. "
                "If you're seeing this, the REST API is working!"
            },
            status=status.HTTP_200_OK,
        )

class CatsViewSet(viewsets.ViewSet):
    @action(
        detail=False,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="list-cats",
    )
    def list_cats(self, request):
        return Response(
            {
                "items": [
                    {"name": "Fluffy", "breed": "Siamese"},
                    {"name": "Whiskers", "breed": "Tabby"},
                    {"name": "Socks", "breed": "Calico"},
                ]
            },
            status=status.HTTP_200_OK,
        )
    @action(
        detail=False,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="load-cats",
    )
    def load_initial_cats(self, request):
        url = f"https://api.thecatapi.com/v1/images/search?limit=20&api_key={settings.CAT_API_KEY}"
        response = requests.get(url)
        data = response.json()
        items = []
        for cat in data:
            breeds = []
            for breed in cat["breeds"]:
                breed_data = {
                    "id": breed["id"],
                    "name": breed["name"],
                    "temperament": breed["temperament"],
                    "origin": breed["origin"],
                    "description": breed["description"],
                    "life_span": breed["life_span"],
                }
                breeds.append(breed_data)
                breed_obj = Breed(
                    id=breed["id"],
                    name=breed["name"],
                    temperament=breed["temperament"],
                    origin=breed["origin"],
                    description=breed["description"],
                    life_span=breed["life_span"],
                )
                breed_obj.save()
            items.append({
                "id": cat["id"],
                "url": cat["url"],
                "width": cat["width"],
                "height": cat["height"],
                "name": "",
                "description": "",
                "breeds": breeds,
            })
        return Response(
            {
                "items": items
            },
            status=status.HTTP_200_OK,
        )