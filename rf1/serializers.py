from rest_framework import serializers
from .models import Student


def start_with_z(value):
    if value.startswith('z'):
        raise serializers.ValidationError('Validation error z start')

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    name = serializers.CharField(max_length=255,validators=[start_with_z])
    class Meta:
        model = Student
        # fields = ('id','name')
        fields = ('__all__')

    def create(self,validate_data):
        return Student.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.save()
        return instance
    # def validate_id(self,value):
    #     if value == 3:
    #         raise serializers.ValidationError('Validation error 3')
    #     return value
    def validate(self,data):
        val = data.get('name',None)
        if val == 'may':
            raise serializers.ValidationError('Validation error may')
        return data
class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')