import uuid as uuid
from django.db import models
from django.contrib.auth import models as django_models
from django_extensions.db.models import TimeStampedModel
from rest_framework_simplejwt.tokens import RefreshToken


def generate_default_username(email):
    """Generate username of the from the email."""
    return str(email).split('@')[0]


class UserManager(django_models.BaseUserManager):

    def get_by_natural_key(self, username):
        return self.get(**{'{}__iexact'.format(
            self.model.USERNAME_FIELD): username})

    def create_user(self, email, username=None, password=None,
                    **other_fields):
        if password is None:
            raise TypeError('User must have a password.')
        if not email:
            raise ValueError(_('Please provide an email address'))
        if username is None:
            username = generate_default_username(email)
        email = self.normalize_email(email)
        user = self.model(email=email, password=password,
                          username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username=None,
                         password=None, **other_fields):
        """
        Create and return a `User` with superuser admin rights.
        Superuser admin rights means that this use is an admin that can do
        anything they want.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if username is None:
            username = generate_default_username(email)
        user = self.create_user(email, username, password, **other_fields)
        user.save()
        return user


class User(django_models.AbstractBaseUser, TimeStampedModel):
    """
        User model for the user creation
    """
    email = models.EmailField('Email', db_index=True, unique=True)
    username = models.CharField('Username', max_length=255,
                                blank=True, null=True)
    first_name = models.CharField('First Name', max_length=255,
                                  blank=True, null=True)
    last_name = models.CharField('Last Name', max_length=255,
                                 blank=True, null=True)

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the terminal
         - which is an email for now.
        """
        return f'{self.email}'



