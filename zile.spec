Summary:	Zile is another Emacs-clone
Summary(pl):	Zile jest jeszcze jednym klonem Emacsa
Name:		zile
Version:	1.3
Release:	2
License:	distributable 
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplicações/Editores
Source0:	http://web.tiscalinet.it/ssigala/sandro/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://zile.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zile is another Emacs-clone. Zile is a customizable, self-documenting
real-time display editor. Zile was written to be as similar as
possible to Emacs; every Emacs user should feel at home with Zile.

%description -l pl
Zile jest kolejnym klonem Emacsa. Jest konfigurowanym,
samo-dokumentuj±cym siê edytorem. By³ pisany tak, aby byæ podobnym do
Emacsa jak to tylko mo¿liwe.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf COPYRIGHT CREDITS KNOWNBUGS NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_infodir}/%{name}*
