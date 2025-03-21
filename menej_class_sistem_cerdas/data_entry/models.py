from django.db import models
from datetime import date

# Create your models here.
class Pengguna(models.Model):
    email = models.EmailField(unique=True)  # Menambahkan unique=True agar tidak ada duplikasi email
    password = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=255)  # Menggunakan CharField dengan batasan panjang
    address_2 = models.CharField(max_length=255, null=True, blank=True)  # Sama seperti address_1
    city = models.CharField(max_length=50, help_text='Enter your city')
    state = models.CharField(max_length=50, verbose_name="State")  # Menggunakan CharField dengan batasan panjang
    zip_code = models.CharField(max_length=10)  # Memperbesar max_length agar fleksibel
    tanggal_join = models.DateField(default=date.today)  # Menggunakan default agar bisa diedit nanti

    def _str_(self):
        return self.email  # Menampilkan email sebagai representasi objek