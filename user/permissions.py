from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        method = request.method
        if request.user and request.user.is_authenticated:
            return True

        elif method == 'GET':
            return True
