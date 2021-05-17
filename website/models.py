from django.db import models
from django.urls import reverse
import uuid

class Loans(models.Model):

    loan_type = models.CharField(max_length=150, verbose_name="Loan Type", null=False)
    percentage = models.IntegerField(verbose_name="Percentage", null=False)

    class Meta:
        db_table = "loan_types"
        verbose_name = "Loan"
        verbose_name_plural = "Loans"

    def __str__(self):
        return self.loan_type

    def get_absolute_url(self):
        return reverse("loans_detail", kwargs={"id": self.id})
    
    
class News(models.Model):

    public_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    headline = models.CharField(max_length=550, verbose_name="Headline", null=False)
    body = models.TextField(verbose_name="Body", null=False)
    new_image = models.ImageField(upload_to='img_uploads/')
    date_created = models.DateField(verbose_name= "Date Created", auto_now=True)

    class Meta:
        db_table = "news"
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"public_id": self.public_id})

