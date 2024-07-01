#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sub-Uplevel
Version  : 0.2800
Release  : 28
URL      : http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/Sub-Uplevel-0.2800.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/Sub-Uplevel-0.2800.tar.gz
Summary  : 'apparently run a function in a higher stack frame'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Sub-Uplevel-license = %{version}-%{release}
Requires: perl-Sub-Uplevel-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Sub::Uplevel - apparently run a function in a higher stack frame
VERSION
version 0.2800

%package dev
Summary: dev components for the perl-Sub-Uplevel package.
Group: Development
Provides: perl-Sub-Uplevel-devel = %{version}-%{release}
Requires: perl-Sub-Uplevel = %{version}-%{release}

%description dev
dev components for the perl-Sub-Uplevel package.


%package license
Summary: license components for the perl-Sub-Uplevel package.
Group: Default

%description license
license components for the perl-Sub-Uplevel package.


%package perl
Summary: perl components for the perl-Sub-Uplevel package.
Group: Default
Requires: perl-Sub-Uplevel = %{version}-%{release}

%description perl
perl components for the perl-Sub-Uplevel package.


%prep
%setup -q -n Sub-Uplevel-0.2800
cd %{_builddir}/Sub-Uplevel-0.2800

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Sub-Uplevel
cp %{_builddir}/Sub-Uplevel-0.2800/LICENSE %{buildroot}/usr/share/package-licenses/perl-Sub-Uplevel/a7990567fc9afec6b13f5b4f775d6555255afef6
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sub::Uplevel.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Sub-Uplevel/a7990567fc9afec6b13f5b4f775d6555255afef6

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
