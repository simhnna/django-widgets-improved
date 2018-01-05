# Changelog

## 1.4.1 (2015-06-29)
------------------

* fixed a regression in django-widget-tweaks v1.4
  (the field is no longer deep copied).

## 1.4 (2015-06-27)

* Django 1.7, 1.8 and 1.9 support;
* setup.py is switched to setuptools;
* testing improvements;
* Python 3.4 support is added;
* Python 2.5 is not longer supported;
* bitbucket repository is no longer supported (development is moved to github).

## 1.3 (2013-04-05)

* added support for ``WIDGET_ERROR_CLASS`` and  ``WIDGET_REQUIRED_CLASS``
  template variables that affect ``{% render_field %}``.

## 1.2 (2013-03-23)

* new ``add_error_attr`` template filter;
* testing improvements.

## 1.1.2 (2012-06-06)

* support for template variables is added to ``render_field`` tag;
* new ``field_type`` and ``widget_type`` filters.

## 1.1.1 (2012-03-22)

* some issues with ``render_field`` tag are fixed.

## 1.1 (2012-03-22)

* ``render_field`` template tag.

## 1.0 (2012-02-06)

* filters return empty strings instead of raising exceptions if field is missing;
* test running improvements;
* python 3 support;
* undocumented 'behave' filter is removed.

## 0.3 (2011-03-04)

* ``add_error_class`` filter.

## 0.2.1 (2011-02-03)

* Attributes customized in widgets are preserved;
* no more extra whitespaces;
* tests;

## 0.1 (2011-01-12)

Initial release.
