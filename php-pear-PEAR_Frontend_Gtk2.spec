%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	Frontend_Gtk2
%define		_status		beta
%define		_pearname	PEAR_Frontend_Gtk2

Summary:	%{_pearname} - graphical PEAR installer based on PHP-Gtk2
Summary(pl):	%{_pearname} - graficzny instalator PEAR oparty na PHP-Gtk2
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1316e6ad9ebad4cb0021e99a98e0e5c0
URL:		http://pear.php.net/package/PEAR_Frontend_Gtk2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-dom
Requires:	php-gtk
Requires:	php-pear
Requires:	php-pear-Config >= 1.10.4
Requires:	php-pear-Gtk2_EntryDialog >= 0.0.3
Requires:	php-pear-PEAR >= 1:1.4.-0.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is a graphical frontend for PEAR, the PHP Extension and
Application Repository. It uses PHP-Gtk2 as graphical toolkit and lets
you easily browse available packages and install them on your
computer.

The program is designed to be used by end-users, making it as easy as
possible to install and uninstall programs.

In PEAR status of this package is: %{_status}.

%description -l pl
Program ten to graficzny frontend do PEAR, Repozytorium Rozszerze� i
Aplikacji PHP (PHP Extension and Application Repository). Korzysta z
PHP-Gtk2 jako graficznego toolkitu i pozwala na �atwe przegl�danie
dost�pnych pakiet�w i ich instalacje na komputerze.

Program zota� zaprojektowany z my�l� o u�ytkowniku ko�cowym, proces
instalacji i deinstalacji zosta� w mo�liwie najwi�kszym stopniu
uproszczony.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PEAR/Frontend/Gtk2
%{php_pear_dir}/PEAR/Frontend/Gtk2.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/PEAR/Frontend/tests/ConfigTest.php
%{php_pear_dir}/PEAR/Frontend/tests/ExpanderTest.phpw
%{php_pear_dir}/PEAR/Frontend/tests/PackageTest.php
%{php_pear_dir}/PEAR/Frontend/tests/runtests.php
%{php_pear_dir}/PEAR/Frontend/tests/TimeDiff.php
