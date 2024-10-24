Summary:	User-space access to Linux kernel SCTP
Summary(pl.UTF-8):	Dostęp do linuksowego SCTP z przestrzeni użytkownika
Name:		lksctp-tools
Version:	1.0.21
Release:	1
License:	LGPL v2.1+ (library), GPL v2+ (programs)
Group:		Applications
#Source0Download: https://github.com/sctp/lksctp-tools/tags
Source0:	https://github.com/sctp/lksctp-tools/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d0f50c93720d0e73516b30e8ac7d2d9c
URL:		https://github.com/sctp/lksctp-tools/wiki
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
Requires:	libsctp = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is for Linux Kernel SCTP Reference Implementation. It
includes command-line utilities.

%description -l pl.UTF-8
Ten pakiet jest przeznaczony dla linuksowej implementacji SCTP.
Zawiera narzędzia działające z linii poleceń.

%package -n libsctp
Summary:	User-space library to access Linux kernel SCTP implementation
Summary(pl.UTF-8):	Biblioteka pozwalająca na dostęp do linuksowej implementacji SCTP
License:	LGPL v2.1+
Group:		Libraries

%description -n libsctp
User-space library to access Linux kernel SCTP implementation.

%description -n libsctp -l pl.UTF-8
Biblioteka pozwalająca na dostęp do linuksowej implementacji SCTP.

%package -n libsctp-devel
Summary:	Header files for libsctp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libsctp
Group:		Development/Libraries
License:	LGPL v2.1+
Requires:	libsctp = %{version}-%{release}

%description -n libsctp-devel
Header files for libsctp library.

%description -n libsctp-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libsctp.

%package -n libsctp-static
Summary:	Static libsctp library
Summary(pl.UTF-8):	Statyczna biblioteka libsctp
Group:		Development/Libraries
License:	LGPL v2.1+
Requires:	libsctp-devel = %{version}-%{release}

%description -n libsctp-static
Static libsctp library.

%description -n libsctp-static -l pl.UTF-8
Statyczna biblioteka libsctp.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# loadable modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/*.{la,a}
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsctp.la

# withsctp sources???
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/*.[ch]
rmdir $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libsctp -p /sbin/ldconfig
%postun	-n libsctp -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/checksctp
%attr(755,root,root) %{_bindir}/sctp_darn
%attr(755,root,root) %{_bindir}/sctp_status
%attr(755,root,root) %{_bindir}/sctp_test
%attr(755,root,root) %{_bindir}/withsctp
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libwithsctp.so*

%files -n libsctp
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/draft-*.txt
%attr(755,root,root) %{_libdir}/libsctp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsctp.so.1

%files -n libsctp-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsctp.so
%{_includedir}/netinet/sctp.h
%{_pkgconfigdir}/libsctp.pc
%{_mandir}/man3/sctp_*.3*
%{_mandir}/man7/sctp.7*

%files -n libsctp-static
%defattr(644,root,root,755)
%{_libdir}/libsctp.a
