Summary:	Jabber client for Mozilla
Summary(pl):	Klient jabbera dla Mozilli
Name:		mozilla-addon-jabberzilla
%define		_realname	jabberzilla
%define		_realname2	jabberxm
Version:	0.3.6beta
Release:	4
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://jabberzilla.mozdev.org/releases/%{_realname2}.xpi
Source1:	http://jabberzilla.mozdev.org/releases/%{_realname}.xpi
Source2:	%{_realname}-installed-chrome.txt
URL:		http://jabberzilla.mozdev.org/
BuildRequires:	unzip
BuildRequires:	zip
BuildArch:	noarch
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_chromedir	%{_libdir}/mozilla/chrome

%description
Jabber client for Mozilla. It can integrate with sidebar or work in
separate window. It has module with conference calls support.

%description -l pl
Klient jabbera dla mozilli. Integruje si� z sidebarem lub dzia�a w
osobnym okienku. Zawiera modu� rozm�w konferencyjnych.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip -o %{SOURCE0} -d  $RPM_BUILD_ROOT%{_chromedir}
unzip -o %{SOURCE1} -d  $RPM_BUILD_ROOT%{_chromedir}
cd $RPM_BUILD_ROOT%{_chromedir}/%{_realname}
zip -r -9 -m ../%{_realname}.jar $RPM_BUILD_ROOT%{_realname} ./
cd -
cd $RPM_BUILD_ROOT%{_chromedir}/%{_realname2}
zip -r -9 -m ../%{_realname2}.jar $RPM_BUILD_ROOT%{_realname2} ./
cd -
mv -f $RPM_BUILD_ROOT%{_chromedir}/components $RPM_BUILD_ROOT%{_libdir}/mozilla
install %{SOURCE2} $RPM_BUILD_ROOT%{_chromedir}

%post
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname2}.jar
%{_libdir}/mozilla/components/*
%{_chromedir}/%{_realname}-installed-chrome.txt
