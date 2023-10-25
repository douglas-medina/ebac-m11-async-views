'''
////////////////////////////////////////////////////////////||
ASGI:                                                       ||
- pip install uvicorn                                       ||
- cli: uvicorn --reload {applicatio_name}.asgi:application  ||
////////////////////////////////////////////////////////////||
'''

import time
from django.http import JsonResponse

def api(request):
    time.sleep(1)
    payload = {'message': 'Hello from Crowdbotics!'}
    if 'task_id' in request.GET:
        payload['task_id'] = request.GET['task_id']
    return JsonResponse(payload)


'''
////////////////////////////////////////////////////////////||
HTTPX:                                                      ||
- pip install httpx                                         ||
- cli: uvicorn --reload {applicatio_name}.asgi:application  ||
////////////////////////////////////////////////////////////||
'''
import asyncio
import httpx
from time import sleep
from django.http import HttpResponse

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)
    
def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    r = httpx.get('https://httpbin.org')
    print(r)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('Non-blocking HTTP request')

def sync_view(request):
    http_call_sync()
    return HttpResponse('Blocking HTTP Request')

'''
////////////////////////////////////////////////////////////||
Exercício:                                                  ||
criar uma view assincrona utilizando asyncio.sleep()        ||
////////////////////////////////////////////////////////////||
'''

async def http_async_exercise():
    for num in range(1, 5):
        await asyncio.sleep(1)
        print(f'Tempo em espera: {num} segundos.')
    async with httpx.AsyncClient() as client:
        r = await client.get('https://httpbin.org')
        print(r)

async def async_exercise(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_async_exercise())
    return HttpResponse(f'Você nem notou, mas a contagem não precisou finalizar para esta mensagem aparecer! Exercício concluído.')