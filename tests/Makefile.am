# Makefile for GNU cpio regression tests.

# Copyright (C) 2004-2025 Free Software Foundation, Inc.

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3, or (at your option)
## any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

EXTRA_DIST = $(TESTSUITE_AT) testsuite package.m4
DISTCLEANFILES       = atconfig $(check_SCRIPTS)
MAINTAINERCLEANFILES = Makefile.in $(TESTSUITE)

## ------------ ##
## package.m4.  ##
## ------------ ##

$(srcdir)/package.m4: $(top_srcdir)/configure.ac
	{                                      \
	  echo '# Signature of the current package.'; \
	  echo 'm4_define([AT_PACKAGE_NAME],      [@PACKAGE_NAME@])'; \
	  echo 'm4_define([AT_PACKAGE_TARNAME],   [@PACKAGE_TARNAME@])'; \
	  echo 'm4_define([AT_PACKAGE_VERSION],   [@PACKAGE_VERSION@])'; \
	  echo 'm4_define([AT_PACKAGE_STRING],    [@PACKAGE_STRING@])'; \
	  echo 'm4_define([AT_PACKAGE_BUGREPORT], [@PACKAGE_BUGREPORT@])'; \
	} >$(srcdir)/package.m4

#

## ------------ ##
## Test suite.  ##
## ------------ ##

TESTSUITE_AT = \
 testsuite.at\
 inout.at\
 interdir.at\
 setstat01.at\
 setstat02.at\
 setstat03.at\
 setstat04.at\
 setstat05.at\
 symlink.at\
 symlink-bad-length.at\
 symlink-long.at\
 symlink-to-stdout.at\
 version.at\
 big-block-size.at\
 CVE-2015-1197.at\
 CVE-2019-14866.at\
 linktime.at\
 linktime01.at

TESTSUITE = $(srcdir)/testsuite

AUTOTEST = $(AUTOM4TE) --language=autotest
$(TESTSUITE): package.m4 $(TESTSUITE_AT)
	$(AUTOTEST) -I $(srcdir) testsuite.at -o $@.tmp
	mv $@.tmp $@

atconfig: $(top_builddir)/config.status
	cd $(top_builddir) && ./config.status tests/$@

clean-local:
	$(SHELL) $(TESTSUITE) --clean

check-local: atconfig atlocal $(TESTSUITE)
	$(SHELL) $(TESTSUITE) $(TESTSUITEFLAGS)

# Run the test suite on the *installed* tree.
installcheck-local:
	$(SHELL) $(TESTSUITE) $(TESTSUITEFLAGS) AUTOTEST_PATH=$(exec_prefix)/bin


## ------------------ ##
## Auxiliary programs ##
## ------------------ ##

check_PROGRAMS = genfile sizemax

genfile_SOURCES = genfile.c argcv.c argcv.h
sizemax_SOURCES = sizemax.c

localedir = $(datadir)/locale
AM_CPPFLAGS = \
 -I$(top_srcdir)/gnu -I../gnu -I$(top_srcdir)/lib\
 -DLOCALEDIR=\"$(localedir)\"

LDADD=../gnu/libgnu.a @LIB_CLOCK_GETTIME@ @INTLLIBS@

