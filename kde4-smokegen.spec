%define         _state          stable
%define         orgname         smokegen
%define         qtver           4.8.0

Summary:	smokegen - A SMOKE library
Summary(pl.UTF-8):	smokegen - Biblioteka SMOKE
Name:		kde4-smokegen
Version:	4.9.4
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	1bc65233c94d0ee38a82d5b7ef3671ae
BuildRequires:	kde4-kdelibs-devel
Obsoletes:	kde4-kdebindings-smoke-qt < 4.6.99
Obsoletes:	smokegen <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMOKE library (Scripting Meta Object Kompiler Engine).

%description -l pl.UTF-8
Biblioteka SMOKE (Scripting Meta Object Kompiler Engine - silnik
kompilatora metaobiektów skryptowych).

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kde4-kdebindings-smoke-devel < 4.6.99
Obsoletes:	smokegen-devel <= 4.8.0

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/smokeapi
%attr(755,root,root) %{_bindir}/smokegen
%attr(755,root,root) %{_libdir}/libcppparser.so
%attr(755,root,root) %{_libdir}/libsmokebase.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokebase.so.?
%dir %{_libdir}/smokegen
%attr(755,root,root) %{_libdir}/smokegen/*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/smoke.h
%{_includedir}/smokegen
%{_datadir}/smoke
%{_datadir}/smokegen
%attr(755,root,root) %{_libdir}/libsmokebase.so
