%define major 0
%define libname %mklibname thai %major
%define libnamedev %mklibname -d thai

Summary:	Thai language support routines
Name:		libthai
Version:	0.1.19
Release:	1
License:	LGPL
Group:		System/Libraries
URL:		http://linux.thai.net
Source0:	http://linux.thai.net/pub/thailinux/software/libthai/%name-%{version}.tar.xz
Patch0:		libthai-0.1.9-doxygen-segfault.patch
BuildRequires:	datrie-devel
# for trietool:
BuildRequires:	trietool

%description
LibThai is a set of Thai language support routines aimed to ease
developers' tasks to incorporate Thai language support in their applications.
It includes important Thai-specific functions e.g. word breaking, input and
output methods as well as basic character and string supports.

%package -n %{libname}
Summary:	Thai language support routines
Group:		System/Libraries
Requires:	thai-data

%description -n %{libname}
LibThai is a set of Thai language support routines aimed to ease
developers' tasks to incorporate Thai language support in their applications.
It includes important Thai-specific functions e.g. word breaking, input and
output methods as well as basic character and string supports.

%package -n thai-data
Summary:	Thai language support data 
Group:		System/Libraries
Requires:	thai-data

%description -n thai-data
Data stuff for libthai.

%package -n %{libnamedev}
Summary:	Thai language support routines
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	thai-devel = %{version}
Obsoletes:	%{mklibname thai 0 -d}

%description -n %libnamedev
The libthai-devel package includes the header files and developer docs 
for the libthai package.

Install libthai-devel if you want to develop programs which will use
libthai.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x \
		--disable-static \
        --disable-doxygen-doc
%make

%install
%makeinstall_std

%files  -n %{libname}
%{_libdir}/lib*.so.%{major}.*
%{_libdir}/lib*.so.%{major}

%files  -n %{libnamedev}
%doc README AUTHORS COPYING ChangeLog
%{_includedir}/thai
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%files  -n thai-data
%{_datadir}/libthai


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.14-2mdv2011.0
+ Revision: 661532
- mass rebuild

* Mon Nov 29 2010 Funda Wang <fwang@mandriva.org> 0.1.14-1mdv2011.0
+ Revision: 602822
- new version 0.1.14 (doxygen disabled, because of wrongly listed man pages)

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Fri Jan 15 2010 Frederik Himpe <fhimpe@mandriva.org> 0.1.13-1mdv2010.1
+ Revision: 491923
- update to new version 0.1.13

* Sun Jun 21 2009 Frederik Himpe <fhimpe@mandriva.org> 0.1.12-1mdv2010.0
+ Revision: 387601
- Update to new version 0.1.12

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 0.1.9-7mdv2009.1
+ Revision: 364636
- use configure2_5x

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.9-7mdv2009.0
+ Revision: 229755
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.9-5mdv2008.1
+ Revision: 179004
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 05 2007 Anssi Hannula <anssi@mandriva.org> 0.1.9-3mdv2008.0
+ Revision: 80182
- obsolete the old devel package instead of the providing+obsoleting
  the current main library package in the devel package

* Wed Sep 05 2007 Thierry Vignaud <tv@mandriva.org> 0.1.9-2mdv2008.0
+ Revision: 80068
- cleanups
- do not provides itself

* Tue Aug 28 2007 Götz Waschk <waschk@mandriva.org> 0.1.9-1mdv2008.0
+ Revision: 72629
- new version
- new devel name

* Fri Apr 20 2007 Thierry Vignaud <tv@mandriva.org> 0.1.8-2mdv2008.0
+ Revision: 16236
- new release


* Mon Jan 22 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.1.7-1mdv2007.0
+ Revision: 111945
- require trietool
- fix buildrequire
- Import libthai

* Mon Jan 22 2007 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1.7-1mdv2007.1
- initial release

