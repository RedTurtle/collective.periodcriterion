.. contents:: **Table of contents**

Introduction
============

This product add a new criteria for dates inside Plone, someway similar to the "*Relative date*" ones,
but beeing able to perform some impossible search if using standard date criteria.

What you can't do with the default Plone relative criteria is configure a Collection that:

* show all events that begin today
* show all news published this month
* show all file modified this year
* ... and so on.

The today, this month and this year values change automatically.

How to use
==========

The new criteria displays a simple selection between:

* Today
* This year
* This month

.. image:: http://keul.it/images/plone/collective.periodcriterion-0.1.0.png
   :alt: Period of time criteria

Where those values are relative to the current date.

Going back to first example of the previous section: at 12:55 PM of January 21 I will see an event that
starts at 8 AM of January 21.
As soon as I visit the Collection again at midnight of January 22 I will no see the event again, but
automatically begin to see all events that starts January 22

Requirements
============

Tested with *Plone 3.3*.

TODO
====

* More tests (the few there are GMT+1 specific)
* Right now the calculation of dates is crappy. Think about replace the ``DateTime`` use with
  standard ``datetime`` module.
  Are Collection still working with ``datetime``?
* Adding Plone 4 compatibility
* Translations issues (I fear will be worst when using on Plone 4)

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

.. image:: http://www.redturtle.net/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.net/


