
from .serializers import AccountSerializers, BuySerializers, ChatGSerializers, ChatOSerializers, ProductSerializers, ComentariyaSerializers
from rest_framework import viewsets
from .models import Buy, ChatGlobal, ChatOnly, Comentariya, Product, Account
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.response import Response

class AccountView(viewsets.ModelViewSet):
    serializer_class = AccountSerializers
    queryset = Account.objects.all()

class BuyView(viewsets.ModelViewSet):
    serializer_class = BuySerializers
    queryset = Buy.objects.all()
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    

    def create(self, request, *args, **kwargs):
        buy_data = request.data 

        print(buy_data)
        new_buy = Buy.objects.create(product = Product.objects.get(id = buy_data['product']), user = Account.objects.get(id = buy_data['user']), max_num = buy_data['max_num'])
        new_buy.save()
        serializer = BuySerializers(new_buy)
        return Response(serializer.data)


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()

class ComentariyaView(viewsets.ModelViewSet):
    serializer_class = ComentariyaSerializers
    queryset = Comentariya.objects.all()

class ChatOView(viewsets.ModelViewSet):
    serializer_class = ChatOSerializers
    queryset = ChatOnly.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ChatGView(viewsets.ModelViewSet):
    serializer_class = ChatGSerializers
    queryset = ChatGlobal.objects.all()