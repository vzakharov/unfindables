from typing import TYPE_CHECKING
from django.contrib.auth.models import User
from django.db import models


class WithIntId:
    if TYPE_CHECKING:
        id: models.BigAutoField


class BaseModel(models.Model, WithIntId):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True
