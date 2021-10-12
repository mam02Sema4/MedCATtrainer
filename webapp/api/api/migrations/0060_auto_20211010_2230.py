# Generated by Django 2.2.9 on 2021-10-10 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('api', '0059_auto_20211008_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000)),
                ('start_ind', models.IntegerField()),
                ('end_ind', models.IntegerField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annotation', to='api.Document')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentAnnotationClassLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField(verbose_name='label')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentAnnotationTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='name')),
                ('description', models.TextField(blank=True, default=None, verbose_name='desc')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_api.documentannotationtask_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='DocumentAnnotationValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc', models.FloatField(default=1)),
                ('annotations', models.ManyToManyField(blank=True, default=None, to='api.Annotation')),
                ('doc_anno_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DocumentAnnotationTask')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Document')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_api.documentannotationvalue_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.RemoveField(
            model_name='project',
            name='cuis',
        ),
        migrations.RemoveField(
            model_name='project',
            name='cuis_file',
        ),
        migrations.AddField(
            model_name='projectannotateentities',
            name='cuis',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='projectannotateentities',
            name='cuis_file',
            field=models.FileField(blank=True, help_text='A file containing a JSON formatted list of CUI code strings, i.e. ["1234567","7654321"]', null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='DocumentAnnotationRegressionTask',
            fields=[
                ('documentannotationtask_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.DocumentAnnotationTask')),
                ('minimum', models.FloatField(blank=True, help_text='minimum value enterable for this task', null=True)),
                ('maximum', models.FloatField(blank=True, help_text='maximum value enterable for this task', null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('api.documentannotationtask',),
        ),
        migrations.CreateModel(
            name='DocumentAnnotationRegValue',
            fields=[
                ('documentannotationvalue_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.DocumentAnnotationValue')),
                ('doc_anno_value', models.FloatField(blank=True, default=None)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('api.documentannotationvalue',),
        ),
        migrations.CreateModel(
            name='ProjectAnnotateDocuments',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Project')),
                ('doc_annotations', models.ManyToManyField(to='api.DocumentAnnotationTask')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('api.project',),
        ),
        migrations.AddField(
            model_name='documentannotationvalue',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Project'),
        ),
        migrations.AddField(
            model_name='documentannotationvalue',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='annotation',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Project'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DocumentAnnotationClfValue',
            fields=[
                ('documentannotationvalue_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.DocumentAnnotationValue')),
                ('doc_anno_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DocumentAnnotationClassLabel')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('api.documentannotationvalue',),
        ),
        migrations.CreateModel(
            name='DocumentAnnotationClassificationTask',
            fields=[
                ('documentannotationtask_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.DocumentAnnotationTask')),
                ('multi_label', models.BooleanField(default=False, help_text='is this task multi or single label. I.e. can annotators pick multiple classes simultaneously')),
                ('labels', models.ManyToManyField(to='api.DocumentAnnotationClassLabel')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('api.documentannotationtask',),
        ),
    ]