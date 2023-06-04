from rest_framework.permissions import BasePermission

class IsActive(BasePermission):

    def has_permission(self, request, view):
        return request.user.status == 'active'
    