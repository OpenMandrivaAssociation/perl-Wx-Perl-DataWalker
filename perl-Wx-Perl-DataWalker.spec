%define upstream_name    Wx-Perl-DataWalker
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl extension for blah blah blah
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Wx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::XSAccessor)
BuildRequires: perl(Devel::Size)
BuildRequires: perl(Wx)
BuildRequires: perl(YAML::XS)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


