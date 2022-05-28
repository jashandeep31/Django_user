from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kawrgs):
        if not email:
            raise ValueError("Please Enter the email")
        email = self.normalize_email(email)
        user = self.model(email=email, **kawrgs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **kawrgs):
        kawrgs.setdefault("is_active", True)
        return self._create_user(email, password, **kawrgs)

    def create_superuser(self, email, password=None, **kawrgs):
        kawrgs.setdefault("is_active", True)
        kawrgs.setdefault("is_staff", True)
        kawrgs.setdefault("is_superuser", True)

        if kawrgs.get("is_staff") is not True:
            raise ValueError("Please set staff True")
        if kawrgs.get("is_superuser") is not True:
            raise ValueError("Please create it super user")
        return self._create_user(email, password, **kawrgs)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    object = UserManager()
