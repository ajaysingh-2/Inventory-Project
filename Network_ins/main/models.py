from django.db import models

# Create your models here.

#Server
class Server(models.Model):
    id = models.AutoField(primary_key=True)
    make=models.CharField(max_length=20)
    modelName=models.CharField(max_length=20)
    type_of_port=models.CharField(max_length=20)
    type_of_part=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    ip_address=models.GenericIPAddressField()
    vlan_id=models.GenericIPAddressField()
    date_purchase=models.DateField(null=True)
    purchase_cost=models.CharField(max_length=50)
    date_of_entry=models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.make
    class Meta:
        verbose_name_plural='Servers'

#Switch
class Switch(models.Model):
    id = models.AutoField(primary_key=True)
    make=models.CharField(max_length=20)
    modelName=models.CharField(max_length=20)
    type_of_port=models.CharField(max_length=20)
    type_of_part=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    ip_address=models.GenericIPAddressField()
    vlan_id=models.GenericIPAddressField()
    date_purchase=models.DateField(null=True)
    purchase_cost=models.CharField(max_length=50)
    date_of_entry=models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.make
    class Meta:
        verbose_name_plural='Switches'
#Wifi


class Wifi(models.Model):
    id = models.AutoField(primary_key=True)
    make=models.CharField(max_length=20)
    modelName=models.CharField(max_length=20)
    type_of_port=models.CharField(max_length=20)
    type_of_part=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    ip_address=models.GenericIPAddressField()
    vlan_id=models.GenericIPAddressField()
    date_purchase=models.DateField(null=True)
    purchase_cost=models.CharField(max_length=50)
    date_of_entry=models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.make
    class Meta:
        verbose_name_plural='Wifi'
#Vlan

class Vlan(models.Model):
    id = models.AutoField(primary_key=True)
    make=models.CharField(max_length=20)
    modelName=models.CharField(max_length=20)
    type_of_port=models.CharField(max_length=20)
    type_of_part=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    ip_address=models.GenericIPAddressField()
    vlan_id=models.GenericIPAddressField()
    date_purchase=models.DateField(null=True)
    purchase_cost=models.CharField(max_length=50)
    date_of_entry=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.make
    class Meta:
        verbose_name_plural='Vlans'


#cameras
class Cameras(models.Model):
    id = models.AutoField(primary_key=True)
    make=models.CharField(max_length=20)
    modelName=models.CharField(max_length=20)
    type_of_port=models.CharField(max_length=20)
    type_of_part=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    ip_address=models.GenericIPAddressField()
    date_purchase=models.DateField(null=True)
    purchase_cost=models.CharField(max_length=50)
    date_of_entry=models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.make
    class Meta:
        verbose_name_plural='cameras'
#Biometric Machine
class Biometric(models.Model):
    make=models.CharField(max_length=20)
    modelName=models.CharField(max_length=20)
    type_of_port=models.CharField(max_length=20)
    type_of_part=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    ip_address=models.GenericIPAddressField()
    date_purchase=models.DateField(null=True)
    purchase_cost=models.CharField(max_length=50)
    date_of_entry=models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.make
    class Meta:
        verbose_name_plural='Biometrics'










