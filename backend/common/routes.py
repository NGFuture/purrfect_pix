from .views import RestViewSet, CatsViewSet


routes = [
    {"regex": r"rest", "viewset": RestViewSet, "basename": "Rest"},
    {"regex": r"cats", "viewset": CatsViewSet, "basename": "Cats"},
]
