from rest_framework.viewsets import ModelViewSet
from students.models import Students
from .serializers import StudentSerializer
from rest_framework.permissions import IsAdminUser

class StudentViews(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]