from time import sleep
import httpx
from django.http import HttpResponse


# Synchronous Function
def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org/")
    print(r)


# Synchronous Request
def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")