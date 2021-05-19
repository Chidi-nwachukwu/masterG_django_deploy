from django.shortcuts import render

# Create your views here.



from pillars.models import Question


def index(request):
    questions = Question.objects.all()


    context = {
        "questions": questions
    }


    return render(request, "pillars/index.html", context)

