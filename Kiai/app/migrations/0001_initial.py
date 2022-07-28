# Generated by Django 3.2.9 on 2022-07-25 03:26

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=100, verbose_name='Tên')),
                ('birthday', models.DateField(null=True, verbose_name='Ngày sinh')),
                ('sex', models.CharField(blank=True, choices=[('Nam', 'Nam'), ('Nữ', 'Nữ'), ('Giới tính khác', 'Giới tính khác')], max_length=20, verbose_name='Giới tính')),
                ('phone', models.CharField(max_length=20, verbose_name='Số điện thoại')),
                ('address', models.CharField(max_length=250, verbose_name='Địa chỉ')),
                ('cmnd', models.CharField(max_length=30, verbose_name='CMND')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(error_messages={'unique': 'Kì thi có mã đã tồn tại'}, max_length=100, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=100, verbose_name='Tên')),
                ('start_date', models.DateField(null=True, verbose_name='Ngày bắt đầu')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(error_messages={'unique': 'Môn học có mã đã tồn tại'}, max_length=50, unique=True, verbose_name='Mã môn học')),
                ('name', models.CharField(max_length=100, verbose_name='Tên môn học')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='Mô tả')),
                ('image', models.ImageField(upload_to='static/images', verbose_name='Ảnh môn học')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.FloatField(verbose_name='Điểm')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.exam', verbose_name='Kì Thi')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Học sinh')),
            ],
        ),
        migrations.CreateModel(
            name='ExamManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, verbose_name='Mã đề thi')),
                ('num_question', models.IntegerField(verbose_name='Số lượng câu hỏi')),
                ('status', models.CharField(blank=True, choices=[('Có', 'Có'), ('Không', 'Không')], max_length=20, verbose_name='Trạng thái xuất bản')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.subject', verbose_name='Môn học')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.subject', verbose_name='Môn học'),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(default='', max_length=200, verbose_name='Ghi chú ')),
                ('subject', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='app.subject', verbose_name='Môn học')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Học sinh')),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(error_messages={'unique': 'Lớp học có mã đã tồn tại'}, max_length=50, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=100, verbose_name='Tên')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.subject', verbose_name='Môn học')),
            ],
        ),
    ]