from django.db import models


class UserFile(models.Model):
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    html_file = models.FileField(upload_to='media/', verbose_name="فایل html")
    code = models.IntegerField(verbose_name="کد کاربر")
    title = models.CharField(max_length=50, verbose_name="نام کاربر")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="تاریخ ایجاد")
