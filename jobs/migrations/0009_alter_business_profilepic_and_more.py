# Generated by Django 4.1.7 on 2023-03-26 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_remove_business_email_remove_freelancer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
    ]
