Summary:	Public domain version of lzip
Summary(pl.UTF-8):	Wersja lzipa wydana jako Public Domain
Name:		pdlzip
Version:	1.10
Release:	1
License:	Public Domain
Group:		Applications/Archiving
Source0:	http://download.savannah.gnu.org/releases/lzip/pdlzip/%{name}-%{version}.tar.lz
# Source0-md5:	ee357f3d9d662ecac2ee5ebacb62ae93
URL:		http://savannah.nongnu.org/projects/lzip/
BuildRequires:	lzip
BuildRequires:	tar >= 1:1.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pdlzip is a lossless data compressor with a user interface similar to
the one of lzip, bzip2 or gzip.

Pdlzip uses the lzip file format; the files produced by pdlzip are
(hope)fully compatible with lzip-1.4 or newer. Pdlzip is in fact a
"public domain" version of the lzip data compressor.

%description -l pl.UTF-8
Pdlzip to bezstratny kompresor danych z interfejsem użytkownika
podobnym do programów lzip, bzip2 i gzip.

Pdlzip wykorzystuje format plików lzip; pliki wytworzone pdlzipem
powinny być zgodne z lzipem 1.4 lub nowszym. Pdlzip to właściwie
wersja kompresora lzip wydana jako "public domain".

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/pdlzip
%{_mandir}/man1/pdlzip.1*
