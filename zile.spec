Summary:	Zile is another Emacs-clone
Summary(pl.UTF-8):	Zile jest jeszcze jednym klonem Emacsa
Name:		zile
Version:	2.3.11
Release:	1
License:	distributable
Group:		Applications/Editors
Source0:	http://ftp.gnu.org/gnu/zile/%{name}-%{version}.tar.gz
# Source0-md5:	eda8745c2681dd7bea478496c0178e90
URL:		http://www.gnu.org/software/zile/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zile is another Emacs-clone. Zile is a customizable, self-documenting
real-time display editor. Zile was written to be as similar as
possible to Emacs; every Emacs user should feel at home with Zile.

%description -l pl.UTF-8
Zile jest kolejnym klonem Emacsa. Jest konfigurowanym,
samo-dokumentującym się edytorem. Był pisany tak, aby być podobnym do
Emacsa jak to tylko możliwe.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/*
