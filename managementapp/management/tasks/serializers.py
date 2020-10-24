from tasks.models import Tasks                           
from rest_framework import serializers



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

    def create(self, validated_data):
        taskCreated = Tasks.objects.create(**validated_data)
        return taskCreated

    def update(self, instance, validated_data):
        instance.task_name = validated_data.get('task_name',
                                                    instance.task_name)

        instance.description = validated_data.get('description',
                                                instance.description)
        instance.created_at = validated_data.get('created_at',
                                                instance.created_at)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
