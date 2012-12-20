.. contents:: **Table of contents**

Introduction
============

This product add a two new criteria for dates inside Plone, someway similar to the "*Today*" ones.

What you can't do with the default Plone relative criteria is configure a Collection that:

* show all news published this month
* show all file modified this year
* ... and so on.

As default Plone "today" criteria, the "this month" and "this year" values are taken automatically.

How to use
==========

The new criteria displays a simple selection between:

* This year
* This month

.. figure:: https://blog.redturtle.it/pypi-images/collective.periodcriterion/collective.periodcriterion-0.2.0-01.png/image_preview
   :target: https://blog.redturtle.it/pypi-images/collective.periodcriterion/collective.periodcriterion-0.2.0-01.png
   :alt: Period of time criteria

   New criteria added on Collection

Also, this product will backport the "Today" criteria added on new style collection content type to the old
Archetypes based ones. 

.. figure:: https://blog.redturtle.it/pypi-images/collective.periodcriterion/collective.periodcriterion-0.2.0-02.png/image_preview
   :target: https://blog.redturtle.it/pypi-images/collective.periodcriterion/collective.periodcriterion-0.2.0-02.png
   :alt: Period of time criteria (on old collections)

   New criteria added on old-style Collection

Requirements
============

Tested with *Plone 4.2* and *Plone 4.3*.

TODO
====

* Fix tests (the few there are GMT+1 specific)
* Right now the calculation of dates is sometimes crappy.

Credits
=======

Developed with the support of `Azienda USL Ferrara`__; Azienda USL Ferrara supports the `PloneGov initiative`__.

.. image:: http://www.ausl.fe.it/logo_ausl.gif
   :alt: Azienda USL's logo

__ http://www.ausl.fe.it/
__ http://www.plonegov.it/

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/


