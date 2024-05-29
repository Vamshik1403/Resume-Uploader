from django.db import models

STATE_CHOICE = (
('Andhra Pradesh','Andhra Pradesh'),
('Arunachal Pradesh','Arunachal Pradesh'),
('Assam','Assam'),	
('Bihar','Bihar'),	
('Chhattisgarh','Chhattisgarh'),
('Goa','Goa'),      
('Gujarat','Gujarat'),
('Haryana','Haryana'),
('Himachal Pradesh','Himachal Pradesh'),	
('Jharkhand','Jharkhand'),	
('Karnataka','Karnataka'),	
('Kerala','Kerala'),	
('Madhya Pradesh','Madhya Pradesh'),	
('Maharashtra','Maharashtra'),
('Manipur','Manipur'),	
('Meghalaya','Meghalaya'),	
('Mizoram','Mizoram'),
('Nagaland','Nagaland'),
('Odisha','Odisha'),	
('Punjab','Punjab'),	
('Rajasthan','Rajasthan'),
('Sikkim','Sikkim'),
('Tamil Nadu','Tamil Nadu'),
('Telangana','Telangana'),	
('Uttar Pradesh','Uttar Pradesh'),	
('Uttarakhand','Uttarakhand'),
('West Bengal','West Bengal'),
('Andaman & Nicobar Island','Andaman & Nicobar Island'),
('Chandigarh','Chandigarh'),
('Dadra & Nagar Haveli & Daman & Diu','Dadra & Nagar Haveli & Daman & Diu'),	
('Delhi','Delhi'),
('Jammu & Kashmir','Jammu & Kashmir'),
('Lakshadweep','Lakshadweep'),	
('Puducherry','Puducherry'),	
('Ladakh','Ladakh')
)

class Resume(models.Model):
 name = models.CharField(max_length=100)
 dob = models.DateField(auto_now=False, auto_now_add=False)
 gender = models.CharField(max_length=100)
 locality = models.CharField(max_length=100)
 city = models.CharField(max_length=100)
 pin = models.PositiveIntegerField()
 state = models.CharField(choices=STATE_CHOICE,max_length=50)
 mobile = models.PositiveBigIntegerField()
 email = models.EmailField()
 job_city = models.CharField(max_length=50)
 profile_image = models.ImageField(upload_to='profileimg',blank=True)
 my_file = models.FileField(upload_to='doc',blank=True)