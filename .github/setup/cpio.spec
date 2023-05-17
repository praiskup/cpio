Summary: A GNU archiving program
Name: cpio
Version: <GENERATED>
Release: <GENERATED>
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/cpio/
Source: https://ftp.gnu.org/gnu/cpio/cpio-%{version}.tar.bz2

Provides: bundled(gnulib)
Provides: bundled(paxutils)
Provides: /bin/cpio

BuildRequires: gcc
BuildRequires: texinfo, autoconf, automake, gettext, gettext-devel
BuildRequires: make

%description
GNU cpio copies files into or out of a cpio or tar archive.  Archives
are files which contain a collection of other files plus information
about them, such as their file name, owner, timestamps, and access
permissions.  The archive can be another file on the disk, a magnetic
tape, or a pipe.  GNU cpio supports the following archive formats:  binary,
old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old tar and POSIX.1
tar.  By default, cpio creates binary format archives, so that they are
compatible with older cpio programs.  When it is extracting files from
archives, cpio automatically recognizes which kind of archive it is reading
and can read archives created on machines with a different byte-order.

Install cpio if you need a program to manage file archives.


%prep
%autosetup -p1


%build
autoreconf -fi
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE64_SOURCE -pedantic -fno-strict-aliasing -Wall $CFLAGS"
%configure --with-rmt="%{_sysconfdir}/rmt"
%make_build
(cd po && make update-gmo)


%install
%make_install

rm -f $RPM_BUILD_ROOT%{_libexecdir}/rmt
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang %{name}

%check
rm -f ${RPM_BUILD_ROOT}/test/testsuite
make check || {
    echo "### TESTSUITE.LOG ###"
    cat tests/testsuite.log
    exit 1
}


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%license COPYING
%{_bindir}/*
%{_mandir}/man*/*
%{_infodir}/*.info*

%changelog
* Wed May 17 2023 Pavel Raiskup <praiskup@redhat.com>
- no changelog here in git, see Fedora spec file
