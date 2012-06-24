Summary:	X interface to CLIPS
Summary(pl):	Iksowe mi�dzymordzie do CLIPSa
Name:		xclips
Version:	20020329
Release:	1
License:	Public Domain (?)
Group:		Development/Languages
Source0:	http://www.ghg.net/clips/download/source/x-prjct.tar.Z
Patch0:		%{name}-automake.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clips-devel >= 6.2
URL:		http://www.ghg.net/clips/CLIPS.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
CLIPS is a productive development and delivery expert system tool
which provides a complete environment for the construction of rule
and/or object based expert systems. CLIPS is being used by numerous
users throughout the public and private community including: all NASA
sites and branches of the military, numerous federal bureaus,
government contractors, universities, and many companies.

This package contains X interface to CLIPS.

%description -l pl
CLIPS jest narz�dziem do tworzenia i wdra�ania system�w eksperckich
zapewniaj�cym kompletne �rodowisko do tworzenia system�w eksperckich
opartych na regu�ach lub obiektach. CLIPS jest u�ywany przez wielu
u�ytkownik�w prywatnych i publicznych, tym: NASA i r�ne ga��zie
wojska, biura federalne, kontrahent�w rz�dowych, uniwersytety i wiele
firm.

Ten pakiet zawiera iksowe mi�dzymordzie do CLIPSa.

%prep
%setup -q -n x-prjct
%patch0 -p1
# this directory confuses make(1)
rm -rf makefile

%build
aclocal
autoheader
automake -a -c
autoconf

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xclips
