from django.shortcuts import render

# Create your views here.


def test(request):

    data = {'name': 'dewei', 'age': 19}

    return render(request, 'test.html', data)