from django.db import models

# Create your models here.



class user(models.Model):
	Id=models.AutoField(primary_key=True)
	Firstname=models.CharField(max_length=100)
	Lastname=models.CharField(max_length=100)
	Mail=models.CharField(max_length=100)
	Password=models.CharField(max_length=100)
	class Meta:
		db_table="tbluser"



class hallbook(models.Model):
	Id=models.AutoField(primary_key=True)
	Hall=models.CharField(max_length=100)
	Name=models.CharField(max_length=100)
	Mail=models.CharField(max_length=100)
	Mobileno=models.IntegerField()
	Fun=models.CharField(max_length=100)
	Checkin=models.DateField(null=True)
	Checkout=models.DateField(null=True)
		
	class Meta:
		db_table="tblbook"
		

class add(models.Model):
	Id=models.AutoField(primary_key=True)
	HallName=models.CharField(max_length=100)
	Address=models.CharField(max_length=100)
	Mail=models.CharField(max_length=100)
	Cost=models.IntegerField()
	Map=models.CharField(max_length=1000)
	Photo=models.FileField(max_length=300, upload_to='', blank=True, null=True )

	class Meta:
		db_table="tbladd"
			


class msg(models.Model):
	Id=models.AutoField(primary_key=True)
	Name=models.CharField(max_length=100)
	Email=models.CharField(max_length=100)
	Mobileno=models.IntegerField()
	Comment=models.CharField(max_length=500)
	class Meta:
		db_table="tblrequest"
