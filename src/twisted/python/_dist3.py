# -*- test-case-name: twisted.python.test.test_dist3 -*-
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Python 3 porting metadata. Only necessary while parts of Twisted are unported.

@var notPortedModules: A list of fully-qualified Python names that correspond
    to modules in Twisted are not ported, for exclusion during installation.
"""

from __future__ import absolute_import, division

notPortedModules = [
    "twisted.conch.client.connect",
    "twisted.conch.client.direct",
    "twisted.conch.tap",
    "twisted.conch.test.test_cftp",
    "twisted.conch.test.test_ckeygen",
    "twisted.conch.test.test_conch",
    "twisted.conch.test.test_manhole",
    "twisted.conch.test.test_tap",
    "twisted.conch.ttymodes",
    "twisted.conch.ui.__init__",
    "twisted.conch.ui.ansi",
    "twisted.conch.ui.tkvt100",
    "twisted.internet._threadedselect",
    "twisted.internet.cfreactor",
    "twisted.internet.glib2reactor",
    "twisted.internet.gtk2reactor",
    "twisted.internet.pyuisupport",
    "twisted.internet.test.process_connectionlost",
    "twisted.internet.test.process_gireactornocompat",
    "twisted.internet.tksupport",
    "twisted.internet.wxreactor",
    "twisted.internet.wxsupport",
    "twisted.mail.__init__",
    "twisted.mail.alias",
    "twisted.mail.bounce",
    "twisted.mail.imap4",
    "twisted.mail.mail",
    "twisted.mail.maildir",
    "twisted.mail.pb",
    "twisted.mail.pop3",
    "twisted.mail.pop3client",
    "twisted.mail.protocols",
    "twisted.mail.relay",
    "twisted.mail.relaymanager",
    "twisted.mail.scripts.__init__",
    "twisted.mail.scripts.mailmail",
    "twisted.mail.smtp",
    "twisted.mail.tap",
    "twisted.mail.test.__init__",
    "twisted.mail.test.pop3testserver",
    "twisted.mail.test.test_bounce",
    "twisted.mail.test.test_imap",
    "twisted.mail.test.test_mail",
    "twisted.mail.test.test_mailmail",
    "twisted.mail.test.test_options",
    "twisted.mail.test.test_pop3",
    "twisted.mail.test.test_pop3client",
    "twisted.mail.test.test_scripts",
    "twisted.mail.test.test_smtp",
    "twisted.news.__init__",
    "twisted.news.database",
    "twisted.news.news",
    "twisted.news.nntp",
    "twisted.news.tap",
    "twisted.news.test.__init__",
    "twisted.news.test.test_database",
    "twisted.news.test.test_news",
    "twisted.news.test.test_nntp",
    "twisted.persisted.dirdbm",
    "twisted.plugins.twisted_conch",
    "twisted.plugins.twisted_ftp",
    "twisted.plugins.twisted_inet",
    "twisted.plugins.twisted_mail",
    "twisted.plugins.twisted_names",
    "twisted.plugins.twisted_news",
    "twisted.plugins.twisted_portforward",
    "twisted.plugins.twisted_runner",
    "twisted.plugins.twisted_socks",
    "twisted.plugins.twisted_words",
    "twisted.protocols.finger",
    "twisted.protocols.ftp",
    "twisted.protocols.ident",
    "twisted.protocols.mice.__init__",
    "twisted.protocols.mice.mouseman",
    "twisted.protocols.shoutcast",
    "twisted.protocols.sip",
    "twisted.python._pydoctor",
    "twisted.python._release",
    "twisted.python.finalize",
    "twisted.python.formmethod",
    "twisted.python.hook",
    "twisted.python.rebuild",
    "twisted.python.release",
    "twisted.python.shortcut",
    "twisted.python.test.cmodulepullpipe",
    "twisted.python.test.test_fakepwd",
    "twisted.python.test.test_htmlizer",
    "twisted.python.test.test_pydoctor",
    "twisted.python.test.test_release",
    "twisted.python.test.test_win32",
    "twisted.scripts.htmlizer",
    "twisted.spread.test.test_pbfailure",
    "twisted.tap.__init__",
    "twisted.tap.ftp",
    "twisted.tap.portforward",
    "twisted.tap.socks",
    "twisted.test.crash_test_dummy",
    "twisted.test.myrebuilder1",
    "twisted.test.myrebuilder2",
    "twisted.test.test_dirdbm",
    "twisted.test.test_finger",
    "twisted.test.test_formmethod",
    "twisted.test.test_ftp",
    "twisted.test.test_ftp_options",
    "twisted.test.test_hook",
    "twisted.test.test_ident",
    "twisted.test.test_rebuild",
    "twisted.test.test_shortcut",
    "twisted.test.test_sip",
    "twisted.test.test_strerror",
    "twisted.trial._dist.__init__",
    "twisted.trial._dist.distreporter",
    "twisted.trial._dist.disttrial",
    "twisted.trial._dist.managercommands",
    "twisted.trial._dist.options",
    "twisted.trial._dist.test.__init__",
    "twisted.trial._dist.test.test_distreporter",
    "twisted.trial._dist.test.test_disttrial",
    "twisted.trial._dist.test.test_options",
    "twisted.trial._dist.test.test_worker",
    "twisted.trial._dist.test.test_workerreporter",
    "twisted.trial._dist.test.test_workertrial",
    "twisted.trial._dist.worker",
    "twisted.trial._dist.workercommands",
    "twisted.trial._dist.workerreporter",
    "twisted.trial._dist.workertrial",
    "twisted.web.distrib",
    "twisted.web.domhelpers",
    "twisted.web.microdom",
    "twisted.web.rewrite",
    "twisted.web.soap",
    "twisted.web.sux",
    "twisted.web.test.test_cgi",
    "twisted.web.test.test_distrib",
    "twisted.web.test.test_domhelpers",
    "twisted.web.test.test_html",
    "twisted.web.test.test_soap",
    "twisted.web.test.test_xml",
    "twisted.web.twcgi",
    "twisted.words.ewords",
    "twisted.words.im.baseaccount",
    "twisted.words.im.interfaces",
    "twisted.words.im.ircsupport",
    "twisted.words.im.pbsupport",
    "twisted.words.iwords",
    "twisted.words.protocols.irc",
    "twisted.words.protocols.oscar",
    "twisted.words.service",
    "twisted.words.tap",
    "twisted.words.test.test_basesupport",
    "twisted.words.test.test_irc",
    "twisted.words.test.test_irc_service",
    "twisted.words.test.test_ircsupport",
    "twisted.words.test.test_oscar",
    "twisted.words.test.test_service",
    "twisted.words.test.test_tap",
]
