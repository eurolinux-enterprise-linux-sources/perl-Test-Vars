Name:		perl-Test-Vars
Version:	0.005
Release:	3%{?dist}
Summary:	Detects unused variables
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Test-Vars/
Source0:	http://search.cpan.org/CPAN/authors/id/G/GF/GFUJI/Test-Vars-%{version}.tar.gz
BuildArch:	noarch
# ===================================================================
# Build requirements
# ===================================================================
BuildRequires:	perl(Module::Build) >= 0.38
BuildRequires:	perl(CPAN::Meta)
BuildRequires:	perl(CPAN::Meta::Prereqs)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(strict)
BuildRequires:	perl(utf8)
BuildRequires:	perl(warnings)
# ===================================================================
# Module requirements
# ===================================================================
BuildRequires:	perl >= 4:5.10.0
BuildRequires:	perl(B)
BuildRequires:	perl(constant)
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(parent)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Test::Builder::Module)
# ===================================================================
# Test suite requirements
# ===================================================================
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More) >= 0.88
# ===================================================================
# Author/Release test requirements
# ===================================================================
BuildRequires:	perl(Test::Pod::Coverage) >= 1.04
BuildRequires:	perl(Test::Pod) >= 1.14
BuildRequires:	perl(Test::Synopsis)
# ===================================================================
# Runtime requirements
# ===================================================================
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Test::Vars finds unused variables in order to keep the source code tidy.

%prep
%setup -q -n Test-Vars-%{version}

# Placate rpmlint about script interpreters in examples
sed -i -e '1s|^#!perl|#!/usr/bin/perl|' example/*.t

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}

%check
./Build test
./Build test --test_files="xt/*.t"

%files
%doc Changes LICENSE README.md example/
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Vars.3pm*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.005-3
- Mass rebuild 2013-12-27

* Mon Jul 01 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.005-2
- Update dependencies

* Fri May 31 2013 Paul Howarth <paul@city-fan.org> - 0.005-1
- Update to 0.005
  - Use skip_all instead of planning 0 tests (#4)

* Sun May  5 2013 Paul Howarth <paul@city-fan.org> - 0.004-1
- Update to 0.004
  - Re-package with Module::Build
  - Remove an unnecessary use of smart match operator
- Switch to Module::Build flow
- Classify buildreqs by usage
- Drop Test::Spelling requirement, no longer used

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-2
- Specify all dependencies.

* Wed Oct 10 2012 Paul Howarth <paul@city-fan.org> - 0.002-1
- Update to 0.002
  - Fix compatibility with Perl 5.16 (CPAN RT#72133)
- Drop upstreamed patch for 5.16 compatibility

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Paul Howarth <paul@city-fan.org> - 0.001-5
- Fix compatibility with Perl 5.16 (CPAN RT#72133)
- Don't need to remove empty directories from buildroot

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.001-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug  8 2011 Paul Howarth <paul@city-fan.org> - 0.001-2
- Sanitize for Fedora submission
- Clean up for modern rpm

* Mon Aug  8 2011 Paul Howarth <paul@city-fan.org> - 0.001-1
- Initial RPM version
