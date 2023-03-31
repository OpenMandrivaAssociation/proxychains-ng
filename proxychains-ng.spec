%define rname proxychains-ng
%define major 4
%define libname %mklibname %rname %major


Name:		proxychains-ng
Version:	4.16
Release:	2
Summary:	This program forces any tcp connection to follow through proxy
License:	GPLv2
Group:		Networking/Other 
URL:		https://github.com/rofl0r/proxychains-ng
Source0:	https://github.com/rofl0r/proxychains-ng/archive/v%{version}.tar.gz
Source1:	proxychains.conf
Requires:	%{libname} = %{EVRD}
Obsoletes: 	%{rname} < %version
Obsoletes: 	%{libname} < %version
Obsoletes:	proxychains

%package -n %{libname}
Summary:	This program forces any tcp connection to follow through proxy
Group:		System/Libraries
Obsoletes:	%{_lib}proxychains3 <= 3.1 

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

%prep
%setup -q -n %{rname}-%{version}

%build
%configure --enable-shared --disable-static

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
%doc README AUTHORS COPYING
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/*

%files -n %{libname}
%{_libdir}/libproxychains4.so
