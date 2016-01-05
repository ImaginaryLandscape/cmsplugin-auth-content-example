from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from django.utils.translation import ugettext_lazy as _

@toolbar_pool.register
class AuthContentToolbar(CMSToolbar):

    def populate(self):
        menu = self.toolbar.get_or_create_menu('authcontent-app', _('View content as..'))
        menu.add_link_item(_('Unauthenticated'), url='?auth_view=false')
        menu.add_link_item(_('Authenticated'), url='?auth_view=true')
