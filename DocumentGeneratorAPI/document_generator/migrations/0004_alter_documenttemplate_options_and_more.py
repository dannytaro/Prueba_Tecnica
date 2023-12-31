# Generated by Django 4.2.4 on 2023-08-25 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_generator', '0003_documenttemplate_template_document'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documenttemplate',
            options={'verbose_name': 'Template', 'verbose_name_plural': 'Templates'},
        ),
        migrations.RemoveField(
            model_name='documenttemplate',
            name='name',
        ),
        migrations.AddField(
            model_name='documenttemplate',
            name='data_document',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='documenttemplate',
            name='data_text',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='documenttemplate',
            name='format',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='documenttemplate',
            name='template_text',
            field=models.TextField(blank=True),
        ),
    ]
