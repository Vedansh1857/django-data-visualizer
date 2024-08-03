from django.urls import path
from .views import upload_file, analyze_file

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('analyze/<int:file_id>/', analyze_file, name='analyze_file'),
]
