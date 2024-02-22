from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from careers.models import Career
from careers.serializers import CareerSerializer


class CareerViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance.title = serializer.validated_data['title']
            instance.content = serializer.validated_data['content']
            instance.save()

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response({})
