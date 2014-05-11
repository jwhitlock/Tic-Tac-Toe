# -*- coding: utf-8 -*-
# flake8: noqa
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table(u'tictactoe_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.IntegerField')()),
            ('player', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('winner', self.gf('django.db.models.fields.IntegerField')()),
            ('strategy_type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'tictactoe', ['Game'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table(u'tictactoe_game')


    models = {
        u'tictactoe.game': {
            'Meta': {'object_name': 'Game'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'state': ('django.db.models.fields.IntegerField', [], {}),
            'strategy_type': ('django.db.models.fields.IntegerField', [], {}),
            'winner': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['tictactoe']
