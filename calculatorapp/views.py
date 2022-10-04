from operator import eq
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


@require_GET
def calc(request):
    print("In the calculate function")

    # equationArray = request.GET.get('equationArray')
    equationArray = request.GET.getlist('equationArray[]')

    print('Preview Data')
    print(request.GET)
    print(type(equationArray))
    print(equationArray)

    for x in equationArray:
        print(x)

    total = float(equationArray[0])
    operator = ''
    current = 0
    for i in range(1, len(equationArray), 1):
        equationArray[i]
        if(equationArray[i].isnumeric() == False):
            operator = equationArray[i]
        elif (operator != ''):
            
            current = float(equationArray[i])
            print(current)
                

            if (operator == "+"):
                total += current
            elif (operator == "-"):
                total -= current
            elif (operator == "x"):
                total *= current
            elif (operator == "/"):                
                if current == 0: # handle divide by zero
                    total = 0
                else:
                    total /= current
            elif (operator == "FLIP"):
                total *= -1
            operator = ''
            
    


    return HttpResponse(str(total))