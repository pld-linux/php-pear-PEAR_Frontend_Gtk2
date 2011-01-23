%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	Frontend_Gtk2
%define		_status		stable
%define		_pearname	PEAR_Frontend_Gtk2

Summary:	%{_pearname} - graphical PEAR installer based on PHP-Gtk2
Summary(pl.UTF-8):	%{_pearname} - graficzny instalator PEAR oparty na PHP-Gtk2
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	2
Epoch:		0
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	777fab5bc424ac5d1cc9d9a7e5c2636c
URL:		http://pear.php.net/package/PEAR_Frontend_Gtk2/
BuildRequires:	php-pear-PEAR >= 1:1.4.5
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-gtk2
Requires:	php-pear
Requires:	php-pear-Config >= 1.10.4
Requires:	php-pear-Gtk2_EntryDialog >= 0.0.3
Requires:	php-pear-Gtk2_FileDrop >= 0.1.0
Requires:	php-pear-PEAR >= 1:1.4.5
Obsoletes:	php-pear-PEAR_Frontend_Gtk2-tests
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

%description -l pl.UTF-8
Program ten to graficzny frontend do PEAR, Repozytorium Rozszerzeń i
Aplikacji PHP (PHP Extension and Application Repository). Korzysta z
PHP-Gtk2 jako graficznego toolkitu i pozwala na łatwe przeglądanie
dostępnych pakietów i ich instalacje na komputerze.

Program został zaprojektowany z myślą o użytkowniku końcowym, proces
instalacji i deinstalacji został w możliwie największym stopniu
uproszczony.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

# pear/tests/pearname/tests -> pear/tests/pearname
install -d ./%{php_pear_dir}/tests/%{_pearname}
mv ./%{php_pear_dir}/{%{_class}/Frontend/tests/*,tests/%{_pearname}}

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
