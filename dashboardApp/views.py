from django.shortcuts import render, redirect
from examApp.models import User, Job, UserJob
from django.contrib import messages

def dashboard(request):
    request.session['first_name']=User.objects.get(email=request.session['email']).first_name
    id=User.objects.get(email=request.session['email']).id
    context={
        'User':User.objects.all(),
        'Job':Job.objects.filter(posted_by=id),
        'Job2':Job.objects.exclude(posted_by=id),
        'UserJob':UserJob.objects.filter(user_id=id),
    }
    return render(request, 'dashboard.html', context)

def new_job(request):
    context={
        'User':User.objects.get(email=request.session['email']).id,
        'Job':Job.objects.all()
    }
    return render(request, 'new_job.html', context)

def process_new_job(request):
    errors=Job.objects.basic_validator2(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/jobs/new')
    else:
        Job.objects.create(posted_by=User.objects.get(email=request.session['email']), title=request.POST['title'], desc=request.POST['desc'], location=request.POST['location'], category=request.POST['category'])
        return redirect('/dashboard')

def edit_job(request, id):
    context={
        'Job':Job.objects.get(id=id),
    }
    return render(request, 'edit_job.html', context)

def process_edit_job(request, id):
    context={
            'Job':Job.objects.get(id=id)
        }
    errors=Job.objects.basic_validator2(request.POST)
    if len(errors)>0:
        for key, value in errors.items() :
            messages.error(request, value)
        return redirect(f'/jobs/edit/{id}')
    else:
        
        c=Job.objects.get(id=id)
        c.title=request.POST['title']
        c.desc=request.POST['desc']
        c.location=request.POST['location']
        c.save()
        return redirect('/dashboard')

def give_up(request, id):
    c=UserJob.objects.get(id=id)
    c.delete()
    return redirect('/dashboard')

def delete_job(request, id):
    c=Job.objects.get(id=id)
    c.delete()
    return redirect('/dashboard')

def take_on(request, id):
    UserJob.objects.create(job_id=id, user_id=User.objects.get(email=request.session['email']).id)
    return redirect('/dashboard')

def job_info(request, id):
    context={
        'Job':Job.objects.get(id=id),
        'UserJob':UserJob.objects.filter(job_id=id)
    }
    return render(request, 'job_info.html', context)


def logout(request):
    del request.session['userid']
    del request.session['first_name']
    del request.session['email']

    return redirect('/')
# Create your views here.
