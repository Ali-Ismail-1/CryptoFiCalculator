from operator import eq
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

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
        #equationArray[i]
        if (is_number(equationArray[i]) == False):
            operator = equationArray[i]
        elif (operator != ''):
            
            print("The Current Number is: " + str(current))            
            current = float(equationArray[i])
            print("The Current Number is: " + str(current))            
                

            if (operator == "+"):
                total += current
            elif (operator == "-"):
                total -= current
            elif (operator == "x"):                
                print(total)
                print(current)
                print(total * current)
                total *= current
            elif (operator == "/"):                
                if current == 0: # handle divide by zero
                    total = 0
                else:
                    total /= current            
            operator = ''
            
    


    return HttpResponse(str(total))