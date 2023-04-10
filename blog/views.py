import openai
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .forms import ChatForm

# Create your views here.

openai.api_key = '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'


def post_list(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        messagem = "preciso que responda a mensagem do cliente em português (brasileiro) e apenas se estiver relacionada com estatística ou delineamento de experimentos; caso a pergunta não esteja relacionada com esses tópicos, responda apenas: A pergunta não está relacionada com planejamento de delineamento amostral ou ocorreu um erro. A seguir, mensagem do cliente: " + message
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=messagem,
                max_tokens=400,
                temperature=0.5,
            )
            reply = response.choices[0].text.strip()
            return JsonResponse({'message': reply})
        except openai.error.OpenAIError as e:
            error_message = str(e)
            return JsonResponse({'message': f'Error: {error_message}'}, status=400)

    form = ChatForm()
    return render(request, 'blog/post_list.html', {'form': form})
