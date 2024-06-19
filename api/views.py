# views.py

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import pipeline

@api_view(['POST'])
def interpret_query_api(request):
    query = request.data.get('query')
    answer = interpret_query(query)
    return Response({'answer': answer})

def interpret_query(query):
    nlp = pipeline("question-answering", model="deepset/bert-large-uncased-whole-word-masking-squad2", tokenizer="deepset/bert-large-uncased-whole-word-masking-squad2")
    result = nlp(question=query, context="Provide a relevant context for your health monitoring application.")
    return result['answer']

def index(request):
    return render(request, 'index.html')

def response(request):
    if request.method == 'POST':
        query = request.POST.get('health-query')
        answer = interpret_query(query)
        return render(request, 'response.html', {'answer': answer})
    return render(request, 'response.html')
