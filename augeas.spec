Name:               augeas
Version:            1.12.0
Release:            6
Summary:            Augeas is a configuration editing tool for changing configuration files
License:            LGPLv2+
URL:                https://augeas.net/
Source0:            https://download.augeas.net/%{name}-%{version}.tar.gz

BuildRequires:      gcc libselinux-devel libxml2-devel readline-devel
Provides:           bundled(gnulib)
Provides:           augeas-libs = %{version}-%{release} augeas-libs%{?_isa} = %{version}-%{release}
Obsoletes:          augeas-libs < %{version}-%{release}

%description
Augeas is a configuration editing tool. It parses configuration files in their native
formats and transforms them into a tree. Configuration changes are made by manipulating
this tree and saving it back into native config files.

Augeas is:
     An API provided by a C library
     A command line tool to manipulate configuration from the shell (and shell scripts)
     Language bindings to do the same from your favorite scripting language
     Canonical tree representations of common configuration files
     A domain-specific language to describe configuration file formats

%package        devel
Summary:        The development environment for %{name}
Requires:       %{name} = %{version}-%{release} pkgconfig
Provides:       augeas-static
Obsoletes:      augeas-static

%description    devel
Provide header files and libraries for the use of building a extension library for %{name}.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build

%configure
%make_build

%check
export SKIP_TEST_PRESERVE_SELINUX=1
%ifarch aarch64
sed -i '/^CFLAGS/s/$/ -fsigned-char/g' ./gnulib/tests/Makefile
%endif
make check

%install

%make_install
%delete_la

%ldconfig_scriptlets

%files
%defattr(-,root,root)
%license COPYING
%doc AUTHORS
%{_bindir}/au*
%{_bindir}/fadot
%{_libdir}/lib*.so.*
%{_datadir}/vim/vimfiles/*
%{_datadir}/augeas/lenses/dist/*
%exclude %{_datadir}/augeas/lenses/dist/tests
%exclude /usr/bin/dump

%files    devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.a

%files    help
%defattr(-,root,root)
%doc NEWS
%doc %{_mandir}/man1/au*.1.gz

%changelog
* Tue Mar 18 2021 chengguipeng <chengguipeng1@huawei.com> - 1.12.0-6
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix the last PR error

* Wed Mar 17 2021 chengguipeng <chengguipeng1@huawei.com> - 1.12.0-5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix the test-localeconv failed on aarch

* Wed Dec 25 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.12.0-4
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:modify the obsoletes

* Fri Dec 13 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.12.0-3
- Type:enhancement
- Id:NA
- SUG:NA
- DESC:Provides arch releated rpm

* Mon Oct 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.12.0-2
- Type:enhancement
- Id:NA
- SUG:NA
- DESC:modify the location of COPYING

* Mon Sep 9 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.12.0-1
- Type:enhancement
- Id:NA
- SUG:NA
- DESC:Reduce the amount of memory needed to evaluate complex path expressions
  against large files,Fix a segfault on OSX when 'augmatch' is run without any
  arguments (Issue #556),update gnulib to 91584ed6.

* Thu Aug 15 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.10.1-4
- Package init
