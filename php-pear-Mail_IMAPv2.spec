%include	/usr/lib/rpm/macros.php
%define		_class		Mail
%define		_subclass	IMAPv2
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides a c-client backend for webmail
Summary(pl):	%{_pearname} - dostarcza backend webmaila oparty o bibliotkê c-client
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	52d1d6783df6d2c2443a0b65a4abd9df
URL:		http://pear.php.net/package/Mail_IMAPv2/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-imap
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail_IMAPv2 provides a simplified backend for working with the
c-client (IMAP) extension. It serves as an OO wrapper for commonly
used c-client functions. It provides structure and header parsing as
well as body retrieval.

Mail_IMAPv2 may be used as a webmail backend or as a component in a
mailing list manager.

In PEAR status of this package is: %{_status}.

%description -l pl
Mail_IMAPv2 dostarcza uproszczonego backendu do pracy z rozszerzeniem
IMAP. Dzia³a jako zorientowany obiektowo wrapper na czêsto u¿ywane
funkcje biblioteki c-client. Przetwarza struktury oraz nag³ówki jak
równie¿ umo¿liwia odbiór tre¶ci wiadomo¶ci.

Mail_IMAPv2 mo¿e byæ u¿yty jako backend webmaila lub jako komponent
zarz±dcy list dyskusyjnych.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{Debug,ManageMB}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/Debug/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Debug
install %{_pearname}-%{version}/%{_subclass}/ManageMB/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/ManageMB

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
