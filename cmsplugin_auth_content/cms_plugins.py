# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import AuthContent

class AuthContentPlugin(CMSPluginBase):
    module = 'Custom'
    model = AuthContent
    name = _('Auth Content')
    render_template = 'cmsplugin_auth_content/auth_content.html'
    cache = False
    fieldsets = (
        ("Default Content", {
            'fields': ('heading', 'content', 'link', 'link_text')
        }),
        ('Authenticated Content', {
            'description': "Add an optional authenticated user version of this content.",
            'fields': ('auth_heading', 'auth_content', 'auth_link', 'auth_link_text')
        })
    )

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(AuthContentPlugin)
