from django.db import models

# Create your models here.
class Checkin(models.Model):
    vehicle_num = models.CharField(max_length = 13, blank = True, null = True)
    Driver_name = models.CharField(max_length = 20, blank = True, null = True)

    AIPL1 = 'AIPL-1'
    AIPL2 = 'AIPL-2'
    AIPL6= 'AIPL-6'
    AIPL7 = 'SAMUDRA'
    OUTSOURCE = 'OUTSOURCE'

    BU_CHOICES=(
        (AIPL1,'AIPL-1'),
        (AIPL2,'AIPL-2'),
        (AIPL6,'AIPL-6'),
        (AIPL7,'AIPL-7'),
        (OUTSOURCE,'OUTSOURCE'),
    )

    BusinessUnit = models.CharField(
        max_length = 20,
        choices = BU_CHOICES,
        default = 'AIPL1'
    )

    Loading = 'Loading'
    Unloading = 'Unloading'
    Type_Choices = (
        (Loading,'Loading'),
        (Unloading,'Unloading'),
    )
    Type = models.CharField(
        max_length = 20,
        choices = Type_Choices,
        default = 'Loading'
    )

    CheckinTime = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.vehicle_num
