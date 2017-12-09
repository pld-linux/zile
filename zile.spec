Summary:	Zile - lightweight Emacs clone
Summary(pl.UTF-8):	Zile - lekki klon Emacsa
Name:		zile
Version:	2.4.14
Release:	1
License:	GPL v3+
Group:		Applications/Editors
Source0:	http://ftp.gnu.org/gnu/zile/%{name}-%{version}.tar.gz
# Source0-md5:	c7d7eec93231c6878f255978d9747a73
URL:		http://www.gnu.org/software/zile/
BuildRequires:	acl-devel
BuildRequires:	gc-devel >= 7.2
BuildRequires:	help2man
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pkgconfig
BuildRequires:	texinfo
Requires:	gc >= 7.2
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
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README THANKS
%attr(755,root,root) %{_bindir}/zile
%{_docdir}/%{name}
%{_mandir}/man1/zile.1*
