import socket

from django.contrib import admin

from . import models


class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip', 'port', 'status')
    list_filter = ('status',)

    def status(self, obj):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((obj.ip, obj.port))
            s.close()
            return '<span style="color:green;">Online</span>'
        except socket.error:
            return '<span style="color:red;">Offline</span>'

    status.allow_tags = True


admin.site.register(models.Server, ServerAdmin)
