from django.urls import path
from . import views

urlpatterns=[
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('jobs/new', views.new_job),
    path('process_new_job', views.process_new_job),
    path('jobs/edit/<int:id>', views.edit_job),
    path('process_edit_job/<int:id>', views.process_edit_job),
    path('jobs/<int:id>', views.job_info),
    path('give_up/<int:id>', views.give_up),
    path('jobs/take_on/<int:id>', views.take_on),
    path('delete_job/<int:id>', views.delete_job),
    # path('books/<title>', views.book_reviews),
]