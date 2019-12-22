from django.db import models
from django.conf import settings
from django.utils import timezone

MALE = 'M'
FEMALE = 'F'

GENDER = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
]


class Union(models.Model):
    union_name = models.CharField(max_length=100)
    union_number = models.IntegerField()
    help_info = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.union_name} - {self.union_number} "

    @property
    def union_info(self):
        return f"{self.union_name} - {self.union_number} "


class Word(models.Model):
    union = models.OneToOneField(Union, on_delete=models.SET_NULL, null=True)
    word_name = models.CharField(max_length=100)
    word_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.union.union_name} - {self.word_name} -{self.word_number}"

    @property
    def word_info(self):
        return f"{self.union.union_name} - {self.word_name} - {self.word_number}"


def create_client_id():
    tz = str(timezone.now().year)[2:4]
    last_client = Client.objects.all().order_by('id').last()
    if not last_client:
        return 'FCV' + str(tz) + '1001'
    client_no = last_client.client_id
    new_client_int = int(client_no.split('FCV' + str(tz))[-1]) + 1
    new_client_id = 'FCV' + str(tz) + str(new_client_int)
    return new_client_id


class Client(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    client_id = models.CharField(
        "Client ID",
        max_length=10,
        unique=True,
        default=create_client_id,
        blank=True,
    )
    name = models.CharField("Name", max_length=200)
    mobile_number = models.PositiveIntegerField("Mobile Number", unique=True)
    others_number = models.PositiveIntegerField("Other's Number", blank=True, null=True)
    gender = models.CharField("Gender", choices=GENDER, default=MALE, max_length=10)
    address = models.TextField(null=True, blank=True)
    word_union = models.ForeignKey(Word, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.mobile_number}"
