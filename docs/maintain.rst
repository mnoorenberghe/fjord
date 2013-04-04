=============================
 Maintaining Fjord and Input
=============================

Adding a new locale
===================

To add a new locale so that ``https://input.mozilla.org/%NEWLOCALE%`` works
and so that people can submit feedback:

1. in your local repository, run::

       $ ./manage.py update_product_details

2. check ``lib/product_details_json/languages.json`` to see if the language is
   there.

   1. if not, you need to file a bug to get it added
   2. if it is, proceed

3. add the locale code to ``PROD_LANGUAGES`` in ``fjord/settings/base.py``

.. Note::

   To test this in a local instance, you need to have::

       DEV_LANGUAGES = PROD_LANGUAGES

   in your ``fjord/settings/local.py``. Otherwise ``DEV_LANGUAGES`` is
   the list of locales in ``locales/``.

   After making that change, you can go to
   ``https://127.0.0.1:8000/%NEWLOCALE%`` and it won't redirect to
   ``https://127.0.0.1:8000/en-US/%NEWLOCALE%``.