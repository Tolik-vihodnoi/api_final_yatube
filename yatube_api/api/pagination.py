from rest_framework import pagination


class PostLimOffPagination(pagination.LimitOffsetPagination):

    PAGE_SIZE = 100
