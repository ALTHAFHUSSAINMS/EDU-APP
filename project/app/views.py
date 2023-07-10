from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import student, college, ADMIN, science, commerce, literature, humanities, finearts, journalism, \
    engineering, law


# Create your views here.
def display(request):
    return render(request, 'register.html')


def display1(request):
    return render(request, 'studentreg.html')


def display2(request):
    return render(request, 'collegereg.html')


def display3(request):
    return render(request, 'login.html')


# def display4(request):
#     return render(request, 'admincreate.html')


def edit(request):
    if 'id' in request.session:
        a = request.session['id']
        if request.method == 'GET':
            data = student.objects.filter(username=a).all()
            return render(request, 'student edit.html', {'r': data})
    else:
        return redirect(log)


def edit1(request):
    if 'id' in request.session:
        a = request.session['id']
        if request.method == 'GET':
            data = college.objects.filter(username=a).all()
            return render(request, 'college edit.html', {'r': data})
    else:
        return redirect(log)


def create(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        c = int(request.POST['n3'])
        d = request.POST['n4']
        e = request.POST['n5']
        f = request.POST['n6']
        g = request.POST['n7']
        h = request.POST['n8']
        if student.objects.filter(username=g):
            return HttpResponse('pls try another username')
        elif college.objects.filter(username=g):
            return HttpResponse('pls try another username')
        elif student.objects.filter(password=h):
            return HttpResponse('pls try another password')
        elif college.objects.filter(password=h):
            return HttpResponse('pls try another password')
        data = student.objects.create(name=a, date_of_birth=b, mobile=c, email_id=d, course_name=e, mark=f, username=g,
                                      password=h)
        data.save()
        return render(request, 'login.html')
    else:
        return render(request, 'studentreg.html')


def create1(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        if student.objects.filter(username=b):
            return HttpResponse('pls try another username')
        elif college.objects.filter(username=b):
            return HttpResponse('pls try another username')
        elif student.objects.filter(password=c):
            return HttpResponse('pls try another password')
        elif college.objects.filter(password=c):
            return HttpResponse('pls try another password')
        data = college.objects.create(college_name=a, username=b, password=c)
        data.save()
        return render(request, 'login.html')
    else:
        return render(request, 'collegereg.html')


def log(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        check = student.objects.filter(username=a, password=b)
        if check:
            request.session['id'] = a
            dict_student = {'student': student.objects.filter(username=a, password=b)}
            return render(request, 'student1.html', dict_student)
        elif college.objects.filter(username=a, password=b):
            request.session['id'] = a
            dict_college = {'college': college.objects.filter(username=a, password=b)}
            return render(request, 'college1.html', dict_college)
        elif ADMIN.objects.filter(username=a, password=b):
            dict_ADMIN = {'ADMIN': ADMIN.objects.filter(username=a, password=b)}
            return render(request, 'admincreate.html', dict_ADMIN)
        else:
            return HttpResponse('ENTER VALID USERNAME OR PASSWORD')
    return render(request, 'login.html')


def logout(request):
    if "id" in request.session:
        request.session.flush()
        return redirect(log)


def profile(request):
    if 'id' in request.session:
        a = request.session['id']
        if request.method == 'GET':
            data = student.objects.filter(username=a).all()
            return render(request, 'student display.html', {'r': data})
    else:
        return redirect(log)


def profile1(request):
    if 'id' in request.session:
        a = request.session['id']
        if request.method == 'GET':
            data = college.objects.filter(username=a).all()
            return render(request, 'college display.html', {'r': data})
    else:
        return redirect(log)


def find(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        data = student.objects.filter(course_name=a, mark=b)
        return render(request, 'college1.html', {'r': data})


def science1(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        if science.objects.filter(course=a, college=b):
            return HttpResponse('DATA ALREADY EXIST')
        data = science.objects.create(course=a, college=b)
        data.save()
        return render(request, 'admincreate.html')


def commerce1(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        if commerce.objects.filter(course=a, college=b):
            return HttpResponse('DATA ALREADY EXIST')
        data = commerce.objects.create(course=a, college=b)
        data.save()
        return render(request, 'admincreate.html')


def literature1(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        if literature.objects.filter(course=a, college=b):
            return HttpResponse('DATA ALREADY EXIST')
        data = literature.objects.create(course=a, college=b)
        data.save()
        return render(request, 'admincreate.html')


def humanities1(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        if humanities.objects.filter(course=a, college=b):
            return HttpResponse('DATA ALREADY EXIST')
        data = humanities.objects.create(course=a, college=b)
        data.save()
        return render(request, 'admincreate.html')


def finearts1(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        if finearts.objects.filter(course=a, college=b):
            return HttpResponse('DATA ALREADY EXIST')
        data = finearts.objects.create(course=a, college=b)
        data.save()
        return render(request, 'admincreate.html')


def journalism1(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        if journalism.objects.filter(course=a, college=b):
            return HttpResponse('DATA ALREADY EXIST')
        data = journalism.objects.create(course=a, college=b)
        data.save()
        return render(request, 'admincreate.html')


def engineering1(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        if engineering.objects.filter(course=a, college=b):
            return HttpResponse('DATA ALREADY EXIST')
        data = engineering.objects.create(course=a, college=b)
        data.save()
        return render(request, 'admincreate.html')


def law1(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        if law.objects.filter(course=a, college=b):
            return HttpResponse('DATA ALREADY EXIST')
        data = law.objects.create(course=a, college=b)
        data.save()
        return render(request, 'admincreate.html')


def sub1(request):
    data = science.objects.all()
    return render(request, 'index.html', {'r': data})


def sub2(request):
    data = commerce.objects.all()
    return render(request, 'index.html', {'r': data})


def sub3(request):
    data = literature.objects.all()
    return render(request, 'index.html', {'r': data})


def sub4(request):
    data = humanities.objects.all()
    return render(request, 'index.html', {'r': data})


def sub5(request):
    data = finearts.objects.all()
    return render(request, 'index.html', {'r': data})


def sub6(request):
    data = journalism.objects.all()
    return render(request, 'index.html', {'r': data})


def sub7(request):
    data = engineering.objects.all()
    return render(request, 'index.html', {'r': data})


def sub8(request):
    data = law.objects.all()
    return render(request, 'index.html', {'r': data})


def update(request):
    if 'id' in request.session:
        x = request.session['id']
        if request.method == 'POST':
            a = request.POST['n1']
            b = request.POST['n2']
            c = int(request.POST['n3'])
            d = request.POST['n4']
            e = request.POST['n5']
            f = request.POST['n6']
            g = request.POST['n7']
            h = request.POST['n8']
            student.objects.filter(username=x).update(name=a, date_of_birth=b, mobile=c, email_id=d, course_name=e,
                                                      mark=f, username=g, password=h)
            return render(request, 'login.html')


def update1(request):
    if 'id' in request.session:
        x = request.session['id']
        if request.method == 'POST':
            a = request.POST['n1']
            b = request.POST['n2']
            c = request.POST['n3']
            college.objects.filter(username=x).update(college_name=a, username=b, password=c)
        return render(request, 'login.html')


def delete(request):
    if 'id' in request.session:
        x = request.session['id']
        if student.objects.filter(username=x):
            data = student.objects.filter(username=x).all()
            data.delete()
            return render(request, 'register.html')
        elif college.objects.filter(username=x):
            data = college.objects.filter(username=x).all()
            data.delete()
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def SUB1(request):
        data = science.objects.all()
        return render(request, 'sub1.html', {'r': data})


def SUB2(request):
    data = commerce.objects.all()
    return render(request, 'sub2.html', {'r': data})


def SUB3(request):
    data = literature.objects.all()
    return render(request, 'sub3.html', {'r': data})


def SUB4(request):
    data = humanities.objects.all()
    return render(request, 'sub4.html', {'r': data})


def SUB5(request):
    data = finearts.objects.all()
    return render(request, 'sub5.html', {'r': data})


def SUB6(request):
    data = journalism.objects.all()
    return render(request, 'sub6.html', {'r': data})


def SUB7(request):
    data = engineering.objects.all()
    return render(request, 'sub7.html', {'r': data})


def SUB8(request):
    data = law.objects.all()
    return render(request, 'sub8.html', {'r': data})



def s1delete(request):
    if request.method == 'POST':
        x = request.POST['n1']
        d = science.objects.filter(id=x)
        d.delete()
        return HttpResponse("Deleted")

