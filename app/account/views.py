from django.http import JsonResponse
from django.http import HttpResponse
from .models import Account
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
import decimal
from decimal import Decimal
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_GET, require_POST

@require_GET
def ping(request):
    """
    ping method for api
    """
    response = JsonResponse({'status': '200', 'description': 'service working', 'result': True})
    return response

@require_GET
def status(request, uuid):
    account = get_object_or_404(Account, pk=uuid)
    response = JsonResponse({'uuid': account.id, 'balance': account.balance, 'hold': account.hold, 'status': account.status})
    return response

@require_POST
@csrf_exempt
def add(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode, parse_float=decimal.Decimal)
    uuid = body['uuid']
    amount = Decimal(body['amount'])
    if Account.objects.filter(pk=uuid).filter(status='Open').exists():
        account = Account.objects.get(pk=uuid)
        if amount > 0:
            account.add(amount)
            response = JsonResponse({'status': '200', 'description': 'Add successfull', 'result': True })
        else:
            response = JsonResponse({'status': '400', 'description': 'Amount is negative', 'result': False})
    else:
        response = JsonResponse({'status': '404', 'description': 'Account not found or closed', 'result': False})
    return response

@require_POST
@csrf_exempt
def substract(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode, parse_float=decimal.Decimal)
    uuid = body['uuid']
    amount = Decimal(body['amount'])
    if Account.objects.filter(pk=uuid).filter(status='Open').exists():
        account = Account.objects.get(pk=uuid)
        if amount > 0:
            if account.substract(amount):
                response = JsonResponse({'status': '200', 'description': 'Substract successfull', 'result': True })
            else:
                response = JsonResponse({'status': '200', 'description': 'Substract error', 'result': False })
        else:
            response = JsonResponse({'status': '400', 'description': 'Amount is negative', 'result': False})
    else:
        response = JsonResponse({'status': '404', 'description': 'Account not found or closed', 'result': False})
    return response