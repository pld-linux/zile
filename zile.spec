Summary:	Zile is another Emacs-clone
Summary(pl):	Zile jest jeszcze jednym klonem Emacsa
Name:		zile
Version:	1.6.1
Release:	1
License:	distributable
Group:		Applications/Editors
Source0:	http://web.tiscalinet.it/ssigala/sandro/files/%{name}-%{version}.tar.gz
# Source0-md5:	5bb3159b921ea44c9f62c288225a661a
Patch0:		%{name}-info.patch
URL:		http://zile.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	texinfo
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
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc COPYRIGHT CREDITS KNOWNBUGS NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/*
%{_infodir}/%{name}*
