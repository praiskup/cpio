dnl Process this file with autoconf to produce a configure script.
dnl This file is part of GNU cpio
dnl Copyright (C) 2003-2025 Free Software Foundation, Inc.
dnl
dnl This program is free software; you can redistribute it and/or modify
dnl it under the terms of the GNU General Public License as published by
dnl the Free Software Foundation; either version 3, or (at your option)
dnl any later version.
dnl
dnl This program is distributed in the hope that it will be useful,
dnl but WITHOUT ANY WARRANTY; without even the implied warranty of
dnl MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
dnl GNU General Public License for more details.
dnl
dnl You should have received a copy of the GNU General Public License
dnl along with this program.  If not, see <http://www.gnu.org/licenses/>.

AC_INIT([GNU cpio], [2.15], [bug-cpio@gnu.org],,
	[http://www.gnu.org/software/cpio])
AC_CONFIG_SRCDIR(src/cpio.h)
AC_CONFIG_AUX_DIR([build-aux])
AC_CONFIG_HEADERS([config.h])
AC_PREREQ([2.71])
AM_INIT_AUTOMAKE([1.16.5 gnits tar-ustar dist-bzip2 std-options silent-rules])

# Enable silent rules by default:
AM_SILENT_RULES([yes])

dnl Check for programs
AC_PROG_CC
AC_PROG_CPP
AC_PROG_GCC_TRADITIONAL
AC_PROG_INSTALL
AC_PROG_RANLIB
AC_PROG_YACC
gl_EARLY
AC_C_PROTOTYPES

AC_SYS_LARGEFILE
AC_HEADER_MAJOR
AC_C_CONST
AC_TYPE_UID_T
AC_CHECK_TYPE(gid_t, int)

AC_HEADER_DIRENT
AX_COMPILE_CHECK_RETTYPE([major], [0], [
#include <sys/types.h>
#ifdef MAJOR_IN_MKDEV
# include <sys/mkdev.h>
#endif
#ifdef MAJOR_IN_SYSMACROS
# include <sys/sysmacros.h>
#endif])
AX_COMPILE_CHECK_RETTYPE([minor], [0], [
#include <sys/types.h>
#ifdef MAJOR_IN_MKDEV
# include <sys/mkdev.h>
#endif
#ifdef MAJOR_IN_SYSMACROS
# include <sys/sysmacros.h>
#endif])

AC_CHECK_FUNCS([fchmod fchown])
# This is needed for mingw build
AC_CHECK_FUNCS([setmode getpwuid getpwnam getgrgid getgrnam pipe fork getuid geteuid])

# gnulib modules
gl_INIT
# paxutils modules
cpio_PAXUTILS
# Additional system dependencies (for mingw)
CPIO_SYSDEP
CPIO_PACKED_STRUCTS

CPIO_DEFAULT_QUOTING_STYLE(escape)

AC_ARG_ENABLE(mt,
 AS_HELP_STRING([--enable-mt],[Enable building of mt program]))

AM_CONDITIONAL([CPIO_MT_COND], [test "$enable_mt" = yes])

AC_CHECK_HEADERS([unistd.h stdlib.h string.h fcntl.h pwd.h grp.h sys/io/trioctl.h utmp.h getopt.h locale.h libintl.h sys/wait.h utime.h locale.h process.h sys/ioctl.h])

AC_CHECK_DECLS([errno, getpwnam, getgrnam, getgrgid, strdup, strerror, getenv, atoi, exit], , , [
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#ifdef HAVE_STRING_H
# include <string.h>
#else
# include <strings.h>
#endif
#include <pwd.h>
#include <grp.h>])

# Gettext.
AM_ICONV
AM_GNU_GETTEXT([external], [need-formatstring-macros])
AM_GNU_GETTEXT_VERSION(0.19)

LIBS="$LIBS $LIB_CLOCK_GETTIME"

# Initialize the test suite.
AC_CONFIG_TESTDIR(tests)
AC_CONFIG_FILES([tests/Makefile tests/atlocal]) # FIXME: tests/preset?
AM_MISSING_PROG([AUTOM4TE], [autom4te])

AC_CONFIG_FILES([Makefile
 doc/Makefile
 gnu/Makefile
 lib/Makefile
 rmt/Makefile
 src/Makefile
 po/Makefile.in])
AC_OUTPUT
