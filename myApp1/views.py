from django.shortcuts import render
from .models import Worker, Department
from django.http import HttpResponse

def index_page(request):

    # new_worker = Worker(
    #     first_name="Alice",
    #     last_name="Johnson",
    #     position="Developer",
    #     salary=25000,
    #     hire_date="2024-01-15"
    # )
    # new_worker.save()

    # worker_to_update = Worker.objects.get(id=2)
    # worker_to_update.first_name = 'Привет'
    # worker_to_update.save() 
 

    all_workers = Worker.objects.all()
    dictionary = {'data': all_workers}
    return render(request, 'index.html', context=dictionary)
    # print(all_workers)

 
    # for i in all_workers:
    #     print(i.first_name, i.last_name, i.salary)

    workers_filtered = Worker.objects.filter(salary=20000)
    # print(workers_filtered)

    low_salary_workers = Worker.objects.filter(salary__lt=19000)
    # print(low_salary_workers)
  
    high_salary_workers = Worker.objects.filter(salary__gt=30000)
    # print(high_salary_workers)

    mid_salary_workers = Worker.objects.filter(salary__gte=20000)
    # print(mid_salary_workers)

    return render(request, 'index.html')


def departments_page(request):
    all_departments = Department.objects.all()
    print(all_departments)
    return HttpResponse("Departments Page")