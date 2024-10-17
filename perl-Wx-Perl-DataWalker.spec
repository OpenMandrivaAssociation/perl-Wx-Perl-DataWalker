%define upstream_name    Wx-Perl-DataWalker
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl extension for blah blah blah
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Wx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::XSAccessor)
BuildRequires:	perl(Devel::Size)
BuildRequires:	perl(Wx)
BuildRequires:	perl(YAML::XS)
BuildArch:	noarch

%description
'Wx::Perl::DataWalker' implements a 'Wx::Frame' subclass that shows a
relatively simple Perl data structure browser. After opening such a frame
and supplying it with a reference to an essentially arbitrary data
structure, you can visually browse it by double-clicking references.

So far, there is no tree view but only a display of the current level of
the data structure. You can traverse back up the structure with a _back_
button.

Optionally, 'Wx::Perl::DataWalker' displays the (approximate!) size of the
data structure using 'Devel::Size'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# requires GTK display
#make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat May 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 381372
- adding missing buildrequires:
- import perl-Wx-Perl-DataWalker


* Sat May 30 2009 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist

