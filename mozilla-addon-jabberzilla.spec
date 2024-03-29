%define		_realname	jabberzilla
%define		_realname2	jabberxm
Summary:	Jabber client for Mozilla
Summary(pl.UTF-8):	Klient Jabbera dla Mozilli
Name:		mozilla-addon-jabberzilla
Version:	0.3.6beta
Release:	6
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://jabberzilla.mozdev.org/releases/%{_realname2}.xpi
# Source0-md5:	dfeabd63d8f47802a276d68a8f2818d1
Source1:	http://jabberzilla.mozdev.org/releases/%{_realname}.xpi
# Source1-md5:	b5168995df0cddfc5c30c6a5b03e70b7
Source2:	%{_realname}-installed-chrome.txt
URL:		http://jabberzilla.mozdev.org/
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	mozilla >= 5:1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 2:1.0-7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
Jabber client for Mozilla. It can integrate with sidebar or work in
separate window. It has module with conference calls support.

%description -l pl.UTF-8
Klient Jabbera dla mozilli. Integruje się z sidebarem lub działa w
osobnym okienku. Zawiera moduł rozmów konferencyjnych.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_chromedir},%{_libdir}/mozilla}

unzip -o %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
unzip -o %{SOURCE1} -d $RPM_BUILD_ROOT%{_chromedir}
cd $RPM_BUILD_ROOT%{_chromedir}/%{_realname}
zip -r -9 -m ../%{_realname}.jar $RPM_BUILD_ROOT%{_realname} ./
cd -
cd $RPM_BUILD_ROOT%{_chromedir}/%{_realname2}
zip -r -9 -m ../%{_realname2}.jar $RPM_BUILD_ROOT%{_realname2} ./
cd -
mv -f $RPM_BUILD_ROOT%{_chromedir}/components $RPM_BUILD_ROOT%{_libdir}/mozilla
install %{SOURCE2} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
	%{_sbindir}/mozilla-chrome+xpcom-generate
fi

%postun
[ ! -x %{_sbindir}/mozilla-chrome+xpcom-generate ] || %{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname2}.jar
%{_libdir}/mozilla/components/*
%{_chromedir}/%{_realname}-installed-chrome.txt
