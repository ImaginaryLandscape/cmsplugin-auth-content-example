# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models import CMSPlugin

class AuthContent(CMSPlugin):
    heading = models.CharField(_("Heading"), max_length=255)
    content = models.TextField(_("Content"), blank=True)
    link = models.URLField(_("Link"), blank=True)
    link_text = models.CharField(_("Link text"), blank=True, max_length=255)

    auth_heading = models.CharField(_("Auth Heading"), max_length=255, blank=True)
    auth_content = models.TextField(_("Auth Content"), blank=True)
    auth_link = models.URLField(_("Auth Link"), blank=True)
    auth_link_text = models.CharField(_("Auth Link text"), blank=True, max_length=255)

    def __unicode__(self):
        if self.auth_heading:
            msg = "- HAS AUTH VERSION"
        else:
            msg = ""
        return "%s %s" % (self.heading, msg)
