from django.db import models

# Create your models here.

class Account(models.Model):
    AccountStatus = models.TextChoices('AccountStatus', 'Open Closed')
    id = models.CharField(max_length=36, primary_key=True)
    name = models.CharField(max_length=300)
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    hold = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=6, choices=AccountStatus.choices)

    def is_substraction_posible(self, substraction):
        result = self.balance - self.hold - substraction
        if result > 0:
            return True
        return False

    def substract(self, substraction):
        if substraction > 0 and self.is_substraction_posible(substraction) and self.status == 'Open':
            self.balance = self.balance - self.hold - substraction
            self.hold = 0
            self.save()
            return True
        return False

    def add(self, amount):
        if amount > 0 and self.status == 'Open':
            self.balance += amount
            self.save()
            return True
        return False

    def fix_hold(self):
        if self.hold > 0 and self.status == 'Open' and self.balance >= self.hold:
            self.balance -= self.hold
            self.hold = 0
            self.save()

