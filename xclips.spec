Summary:	X interface to CLIPS
Summary(pl.UTF-8):	Iksowe międzymordzie do CLIPSa
Name:		xclips
Version:	2.01
Release:	2
Epoch:		1
License:	Public Domain (?)
Group:		Development/Languages
Source0:	http://www.ghg.net/clips/download/source/x-prjct.tar.Z
# Source0-md5:	1bb0d0e684742188b8c14912c26f12cb
Patch0:		%{name}-automake.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clips-devel >= 6.24
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libX11-devel
URL:		http://www.ghg.net/clips/CLIPS.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLIPS is a productive development and delivery expert system tool
which provides a complete environment for the construction of rule
and/or object based expert systems. CLIPS is being used by numerous
users throughout the public and private community including: all NASA
sites and branches of the military, numerous federal bureaus,
government contractors, universities, and many companies.

This package contains X interface to CLIPS.

%description -l pl.UTF-8
CLIPS jest narzędziem do tworzenia i wdrażania systemów eksperckich
zapewniającym kompletne środowisko do tworzenia systemów eksperckich
opartych na regułach lub obiektach. CLIPS jest używany przez wielu
użytkowników prywatnych i publicznych, tym: NASA i różne gałęzie
wojska, biura federalne, kontrahentów rządowych, uniwersytety i wiele
firm.

Ten pakiet zawiera iksowe międzymordzie do CLIPSa.

%prep
%setup -q -n x-prjct
%patch0 -p1
# this directory confuses make(1)
rm -rf makefile

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xclips*
