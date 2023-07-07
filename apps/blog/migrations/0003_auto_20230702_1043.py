# Generated by Django 2.2.28 on 2023-07-02 10:43

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_is_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendlink',
            name='logo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='friend/default.png', upload_to='friend/%Y/%m/%d', verbose_name='网站LOGO'),
        ),
    ]