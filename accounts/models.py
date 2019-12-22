from django.utils import timezone

from django.db import models
from clients.models import Client


class Package(models.Model):
    package_name = models.CharField('Package', max_length=100, default='')
    package_bill = models.FloatField('Per Month Amount', default=0)
    month_cycle = models.IntegerField('Month Cycle', default=30)
    per_day_amount = models.FloatField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.package_name} - {self.package_bill}"

    @property
    def package_details(self):
        return f"{self.package_name} {self.month_cycle}"

    def save(self, *args, **kwargs):
        self.per_day_amount = "{:.2f}".format(self.package_bill / self.month_cycle)
        return super(Package, self).save(*args, **kwargs)


class Account(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    total_balance = models.FloatField("Total Balance", blank=True, default=0)
    total_due = models.FloatField("Total Due", blank=True, default=0)
    ac_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client.name}"


class AccountPackage(models.Model):
    account_holder = models.ForeignKey(Account, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    active_date = models.DateField("Opening Date")
    closed_date = models.DateField("Closed Date", null=True, blank=True)
    total_days = models.PositiveIntegerField(default=0, blank=True)
    due = models.FloatField("Total Due", blank=True, default=0)
    ac_status = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account_holder} - {self.package}"

    def save(self, *args, **kwargs):
        self.total_days = round((timezone.now().date() - self.active_date).days, 1)
        if self.closed_date:
            self.total_days = round((self.closed_date - self.active_date).days, 1)
            self.ac_status = False
        self.due = self.package.per_day_amount * self.total_days

        return super(AccountPackage, self).save(*args, **kwargs)
