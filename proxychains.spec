%define rname proxychains
%define major 4
%define libname %mklibname %rname %major
%define develname %mklibname %rname -d 


Name:		proxychains-ng
Version:	4.8.1
Release:	1
Summary:	This program forces any tcp connection to follow through proxy
License:	GPL
Group:		Networking/Other 
URL:		https://github.com/rofl0r/proxychains-ng
Source0:	http://downloads.sourceforge.net/project/proxychains-ng/%{rname}-%{version}.tar.bz2
Source1:	proxychains.conf
Requires:	%{libname} = %{EVRD}
Obsoletes: 	%{rname} < %version
Obsoletes: 	%{libname} < %version
Obsoletes:	proxychains
Requires:	glibc >= 2.12.1
Requires:	libstdc++6 >= 4.5.2

%package -n %{libname}
Summary:	This program forces any tcp connection to follow through proxy
Group:		System/Libraries
Obsoletes:	%{_lib}proxychains3 < 4.8

%package -n %{develname}
Summary:	This program forces any tcp connection to follow through proxy
Group:		Development/Other
Requires:	%{libname} = %{EVRD}

%description
This program allows you to use SSH, TELNET, VNC, FTP 
and any other Internet application from behind HTTP
(HTTPS) and SOCKS(4/5) proxy servers. This "proxifier" 
provides proxy server support to any app.

%description -n %{libname}
This program allows you to use SSH, TELNET, VNC, FTP 
and any other Internet application from behind HTTP
(HTTPS) and SOCKS(4/5) proxy servers. This "proxifier" 
provides proxy server support to any app.

%description -n %{develname}
Devel package for proxychains.

%prep
%setup -q -n %{rname}-%{version}

%build
%configure2_5x --enable-shared --disable-static

%make

%install
%makeinstall_std

# install sample conf file
install -d %{buildroot}/etc
install -m 644 %SOURCE1 %{buildroot}/etc

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files 
%doc README AUTHORS COPYING ChangeLog
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/*

%files -n %{libname}
%{_libdir}/libproxychains4.so

%files -n %{develname}
%{_libdir}/*.so

%clean
rm -rf %{buildroot}
rm -rf $RPM_BUILD_DIR/%{rname}-%{version}

