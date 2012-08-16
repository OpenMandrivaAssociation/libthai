%define major 0
%define libname %mklibname thai %major
%define libnamedev %mklibname -d thai

Summary: Thai language support routines
Name:    libthai
Version: 0.1.18
Release: 1
License: LGPL
Group:   System/Libraries
URL:     http://linux.thai.net
Source0:  http://linux.thai.net/pub/thailinux/software/libthai/%name-%{version}.tar.gz
Patch0: libthai-0.1.9-doxygen-segfault.patch
BuildRequires: pkgconfig datrie-devel
# for trietool:
BuildRequires: trietool

%description
LibThai is a set of Thai language support routines aimed to ease
developers' tasks to incorporate Thai language support in their applications.
It includes important Thai-specific functions e.g. word breaking, input and
output methods as well as basic character and string supports.

%package -n %libname
Summary: Thai language support routines
Group:   System/Libraries
Requires: thai-data

%description -n %libname
LibThai is a set of Thai language support routines aimed to ease
developers' tasks to incorporate Thai language support in their applications.
It includes important Thai-specific functions e.g. word breaking, input and
output methods as well as basic character and string supports.

%package -n thai-data
Summary: Thai language support data 
Group:   System/Libraries
Requires: thai-data

%description -n thai-data
Data stuff for libthai.

%package -n %libnamedev
Summary:  Thai language support routines
Group:    Development/C
Requires: %{libname} = %{version}
Requires: pkgconfig
Provides: thai-devel = %{version}
Obsoletes: %{mklibname thai 0 -d}

%description -n %libnamedev
The libthai-devel package includes the header files and developer docs 
for the libthai package.

Install libthai-devel if you want to develop programs which will use
libthai.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%configure2_5x --disable-static --disable-doxygen-doc
%make

%install
%makeinstall_std

%files  -n %libname
%doc README AUTHORS COPYING ChangeLog
%{_libdir}/lib*.so.%{major}.*
%{_libdir}/lib*.so.%{major}

%files  -n %libnamedev
%{_includedir}/thai
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%files  -n thai-data
%{_datadir}/libthai
