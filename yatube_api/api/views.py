from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework import permissions

from posts.models import Group, Post, User
from .pagination import PostLimOffPagination
from .permissions import OwnerOrReadOnly, ReadOnly
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer
)


class GetInstanceMixin:

    @staticmethod
    def retrieve_post_obj(obj):
        post_id = obj.kwargs.get('post_id')
        return get_object_or_404(Post, id=post_id)

    @staticmethod
    def retrieve_user_obj(obj):
        return get_object_or_404(User, id=obj.request.user.id)


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostLimOffPagination
    permission_classes = (OwnerOrReadOnly, )

    def get_permissions(self):
        if self.action == 'retrieve':
            return ReadOnly(),
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.AllowAny, )


class CommentViewSet(GetInstanceMixin,
                     viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly, )

    def get_queryset(self):
        post = self.retrieve_post_obj(self)
        return post.comments

    def perform_create(self, serializer):
        post = self.retrieve_post_obj(self)
        serializer.save(author=self.request.user,
                        post=post)

    def get_permissions(self):
        if self.action == 'retrieve':
            return ReadOnly(),
        return super().get_permissions()


class FollowViewSet(GetInstanceMixin,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('$following__username',)

    def get_queryset(self):
        user = self.retrieve_user_obj(self)
        return user.follower

    def perform_create(self, serializer):
        serializer.save(user=self.retrieve_user_obj(self))
