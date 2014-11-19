

%define prefix /usr
%define name proxychains-ng
%define version 4.8.1
%define release %mkrel 1
%define url http://sourceforge.net/projects/proxychains/

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Other
URL:		%{url}
Source0:		%{name}-%{version}.tar.xz
# example the new source comes without anything
Source1:	proxychains.conf
#Patch0:		proxychains-3.1-ld_preload.patch
Summary:	ProxyChains - HTTP and SOCKS
Summary(de):	ProxyChains - HTTP und SOCKS
BuildRoot:	%{_tmppath}/%{name}-buildroot
Obsoletes: 	%{name} < %version
Obsoletes:	proxychains
Requires:	glibc >= 2.12.1
Requires:	libstdc++6 >= 4.5.2

%description
This program allows you to use SSH, TELNET, VNC, FTP 
and any other Internet application from behind HTTP
(HTTPS) and SOCKS(4/5) proxy servers. This "proxifier" 
provides proxy server support to any app.

#german
%description -l de
Dieses Programm ermöglicht es Ihnen, SSH, Telnet, VNC, 
FTP und andere Internet-Anwendung hinter HTTP (HTTPS) 
und Socks (5.4)-Proxy-Server verwenden. Diese "proxifier" 
bietet Proxy-Server unterstützen zu jeder App.

%prep

%setup -q -n %{name}-%{version}
#%patch0 -p1

%build

%configure2_5x --enable-shared --disable-static

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

# install sample conf file
install -d %{buildroot}/etc
install -m 644 %SOURCE1 %{buildroot}/etc


%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/proxychains4
%{_libdir}/libproxychains4.so
%attr(644,-,-)%config(noreplace)%{_sysconfdir}/proxychains.conf


%clean
rm -rf %{buildroot}
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%changelog
* Tue Jul 22 2014 ghostbunny <ghostbunny at gmx dot de> 4.8.1-1pclos2014
- 4.8.1

* Tue Jun 10 2014 ghostbunny <ghostbunny at gmx dot de> 4.7-1pclos2014
- 4.7

* Mon Apr 11 2011 Texstar <texstar at gmail.com> 3.1-3pclos2011
- add patch to fix linkage

* Sat Apr 09 2011 Texstar <texstar at gmail.com> 3.1-2pclos2011
- fix specfile

* Mon Mar 28 2011 leiche <meisssw01 at aol.com> 3.1-1leiche2011
- import to PCLinuxOS
