%define upstream_name    MooseX-MultiInitArg
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Attributes with aliases for constructor arg
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
If you've ever wanted to be able to call an attribute any number of things
while you're passing arguments to your object constructor, Now You Can.

The primary motivator is that I have some attributes that were named
inconsistently, and I wanted to rename them without breaking backwards
compatibility with my existing API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.10.0-2mdv2011.0
+ Revision: 654256
- rebuild for updated spec-helper

* Mon Apr 26 2010 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 539197
- import perl-MooseX-MultiInitArg


* Mon Apr 26 2010 cpan2dist 0.01-1mdv
- initial mdv release, generated with cpan2dist
