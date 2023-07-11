from django.contrib.auth.models import (
    BaseUserManager
)

class UserRoles:
    USER = "user"
    ADMIN = "admin"
    ROLES = [
        (USER, "Пользователь"),
        (ADMIN, "Администратор")
    ]

class UserManager(BaseUserManager):
    """
        функция создания пользователя — в нее мы передаем обязательные поля
        """

    def create_user(self, email, first_name, last_name, phone, password=None, role=UserRoles.USER):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None, role=UserRoles.ADMIN):
        """
        функция для создания суперпользователя — с ее помощью мы создаем админинстратора
        это можно сделать с помощью команды createsuperuser
        """

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role=role,
        )

        user.save(using=self._db)
        return user
