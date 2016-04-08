from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SalesActivityPlan(models.Model):
	activity_id = models.IntegerField()
	not_planned_actual = models.BooleanField()
	year_p = models.IntegerField()
	week_no = models.IntegerField()
	user_id = models.IntegerField()
	begin = models.DateField()
	end = models.DateField()
	the_date = models.DateField()
	plan_id = models.IntegerField()
	name = models.TextField()
	partner_id = models.IntegerField()
	location = models.CharField(max_length=200)
	actual_partner_id = models.IntegerField()
	actual_location = models.CharField(max_length=200)
	actual_result = models.TextField()
	canceled_plan = models.BooleanField()
	daylight = models.IntegerField()
	dow = models.IntegerField()
	id = models.BigIntegerField(primary_key=True)




	class Meta:
		managed = False
		db_table = 'sales_activity_plan'