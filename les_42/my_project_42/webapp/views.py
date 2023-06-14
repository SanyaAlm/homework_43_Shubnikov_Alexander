from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request, 'index.html')


def create_calculate(request):
    if request.method == 'GET':
        return render(request, 'calculate_create.html')

    elif request.method == 'POST':
        data = request.POST
        print(data)
        context = {
            'first': data.get('First'),
            'second': data.get('Second'),
            'do': data.get('do'),
            'result': 0,
        }
        try:
            match context['do']:
                case '+':
                    context['result'] += float(context['first']) + float(context['second'])
                case '-':
                    context['result'] += float(context['first']) - float(context['second'])
                case ':':
                    second_num = float(context['second'])
                    if second_num != 0:
                        context['result'] += float(context['first']) / second_num
                    else:
                        context['result'] = "Can't divide by zero"
                case '*':
                    context['result'] += float(context['first']) * float(context['second'])

            if isinstance(context['result'], float):
                context['result'] = round(context['result'], 2)
                if context['result'].is_integer():
                    context['result'] = int(context['result'])
        except ValueError:
            context['result'] = 'You need to enter numbers'
            return render(request, 'index.html', context)

        return render(request, 'calculate_view.html', context)
