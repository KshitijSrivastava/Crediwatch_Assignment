
from django.db import models


class CompressionTable(models.Model):
    string = models.TextField()
    compressed_string = models.TextField()