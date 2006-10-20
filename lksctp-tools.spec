Summary:	User-space access to Linux kernel SCTP
Summary(pl):	Dostêp do linuksowego SCTP z przestrzeni u¿ytkownika
Name:		lksctp-tools
Version:	1.0.6
Release:	1
License:	LGPL v2.1+ (library), GPL v2+ (programs)
Group:		Applications
Source0:	http://dl.sourceforge.net/lksctp/%{name}-%{version}.tar.gz
# Source0-md5:	6dcacb7cf4ce8c21b343e5578ccdaa2f
URL:		http://lksctp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	libsctp = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is for Linux Kernel SCTP Reference Implementation. It
includes command-line utilities.

%description -l pl
Ten pakiet jest przeznaczony dla linuksowej implementacji SCTP.
Zawiera narzêdzia dzia³aj±ce z linii poleceñ.

%package -n libsctp
Summary:	User-space library to access Linux kernel SCTP implementation
Summary(pl):	Biblioteka pozwalaj±ca na dostêp do linuksowej implementacji SCTP
License:	LGPL v2.1+
Group:		Libraries

%description -n libsctp
User-space library to access Linux kernel SCTP implementation.

%description -n libsctp -l pl
Biblioteka pozwalaj±ca na dostêp do linuksowej implementacji SCTP.

%package -n libsctp-devel
Summary:	Header files for libsctp library
Summary(pl):	Pliki nag³ówkowe biblioteki libsctp
Group:		Development/Libraries
License:	LGPL v2.1+
Requires:	libsctp = %{version}-%{release}

%description -n libsctp-devel
Header files for libsctp library.

%description -n libsctp-devel -l pl
Pliki nag³ówkowe biblioteki libsctp.

%package -n libsctp-static
Summary:	Static libsctp library
Summary(pl):	Statyczna biblioteka libsctp
Group:		Development/Libraries
License:	LGPL v2.1+
Requires:	libsctp-devel = %{version}-%{release}

%description -n libsctp-static
Static libsctp library.

%description -n libsctp-static -l pl
Statyczna biblioteka libsctp.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libsctp -p /sbin/ldconfig
%postun	-n libsctp -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/checksctp
%attr(755,root,root) %{_bindir}/sctp_darn
%attr(755,root,root) %{_bindir}/sctp_test
%attr(755,root,root) %{_bindir}/withsctp
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libwithsctp.so*

%files -n libsctp
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/draft-*.txt
%attr(755,root,root) %{_libdir}/libsctp.so.*.*.*

%files -n libsctp-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsctp.so
%{_libdir}/libsctp.la
%{_includedir}/netinet/sctp.h
%{_mandir}/man3/sctp_*.3*
%{_mandir}/man7/sctp.7*

%files -n libsctp-static
%defattr(644,root,root,755)
%{_libdir}/libsctp.a
