from rest_framework.permissions import BasePermission


class OnlyForAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_staff)


class ForAllUsersPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
