import base64


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

@csrf_exempt
@api_view(['POST'])
def account_post(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            # Step 1
            account_name = data.get('accountName')
            account_name = base64.b64decode(account_name).decode("utf-8")
            print("Step 1. Account Name:", account_name)
            # Step 2
            amount = data.get('amount')
            amount = base64.b64decode(amount).decode("utf-8")
            print("Step 2. Amount:", amount)
            # Step 3
            new_amount = ''.join(char for char in amount if char.isalnum())
            print("Step 3. Amount:", new_amount)
            # Step 4
            new_amount = new_amount.upper()
            print("Step 4. Amount:", new_amount)
            # Step 5
            final_amount = 0
            for cha in new_amount:
                final_amount = final_amount + roman_to_number(cha)
            print("Step 5. Amount:", final_amount)
            response_dict = {
                'requestId': data.get('requestId'),
                'accountName': account_name,
                'amount': final_amount,
            }
            return Response(response_dict, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({
                'status': 'failed',
                'status_code': 400,
                'message': 'Wrong inputted information.',
                'data': [{'details': ex.__str__()}]
            }, status=status.HTTP_400_BAD_REQUEST)


def roman_to_number(argument):
    switcher = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    return switcher.get(argument, 0)
