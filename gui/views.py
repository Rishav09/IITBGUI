from django.shortcuts import render
import csv
import json
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer=SentimentIntensityAnalyzer()

data={}
with open('today_5th_oct_new.csv','r',newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
         data[row[0]]=float(row[1])


analyzer.lexicon.update(data)



def index(request):
    return render(request, "gui/index.html")

@csrf_exempt
def output(request):
    sentences = request.POST.get('name',None)
    senti = analyzer.polarity_scores(sentences)
    print(senti)
    context_dict = {'sentiment': senti}
    return JsonResponse({'sentiment': senti})
    #return render(request, "gui/index.html", context = context_dict)