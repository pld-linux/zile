Summary:	Zile - lightweight Emacs clone
Summary(pl.UTF-8):	Zile - lekki klon Emacsa
Name:		zile
Version:	2.6.2
Release:	1
License:	GPL v3+
Group:		Applications/Editors
Source0:	https://ftp.gnu.org/gnu/zile/%{name}-%{version}.tar.gz
# Source0-md5:	a35f44ac31e2d38f0d5920a36feb7583
URL:		http://www.gnu.org/software/zile/
BuildRequires:	acl-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	help2man
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	texinfo
BuildRequires:	vala >= 2:0.52
BuildRequires:	vala-libgee >= 0.8
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
