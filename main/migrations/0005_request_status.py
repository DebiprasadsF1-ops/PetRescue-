from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_request_message_alter_pet_breed_alter_pet_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', help_text='Current status of the request', max_length=10),
        ),
    ]