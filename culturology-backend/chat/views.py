from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
class ChatBotAPIView(APIView):
    def post(self, request):
        user_message = request.data.get('message', '')

        # Простая логика ответов
        bot_replies = [
            'Наш народ чтит природу и предков.',
            'Охота с орлом — наша гордость.',
            'Мы верим в силу традиций и единство семьи.',
            'Путешествие по степям всегда было частью нашей жизни.',
            'Наши обряды передаются из поколения в поколение.'
        ]

        import random
        bot_reply = random.choice(bot_replies)

        return Response({'reply': bot_reply}, status=status.HTTP_200_OK)
    def chat_api_view(request):
        return JsonResponse({'message': 'Привет из API чата!'})
