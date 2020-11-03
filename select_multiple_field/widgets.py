# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import widgets
from django.utils.safestring import mark_safe

try:
    from django.forms.utils import flatatt
except ImportError:
    from django.forms.util import flatatt

try:
    from django.utils.html import format_html
except ImportError:
    def format_html(format_string, *args, **kwargs):
        return format_string.format(*args, **kwargs)


HTML_ATTR_CLASS = 'select-multiple-field'


class SelectMultipleField(widgets.SelectMultiple):
    """Multiple select widget ready for jQuery multiselect.js"""

    allow_multiple_selected = True

    def render(self, name, value, attrs={}, choices=(), renderer=None):
        rendered_attrs = {'class': HTML_ATTR_CLASS}
        rendered_attrs.update(attrs)

        final_attrs = self.build_attrs(rendered_attrs, dict(name=name))
        s = widgets.SelectMultiple(choices=self.choices)
        select_html = s.render(name=name, value=value, attrs=final_attrs)

        return mark_safe(''.join(select_html))

    def value_from_datadict(self, data, files, name):
        """
        SelectMultipleField widget delegates processing of raw user data to
        Django's SelectMultiple widget

        Returns list or None
        """
        return super(SelectMultipleField, self).value_from_datadict(
            data, files, name)
