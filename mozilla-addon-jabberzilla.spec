Summary:	Jabber client for Mozilla
Summary(pl):	Klient jabbera dla Mozilli
Name:		mozilla-addon-jabberzilla
%define		_realname	jabberzilla
Version:	0.3.6beta
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://jabberzilla.mozdev.org/releases/jabberxm.xpi
Source1:	http://jabberzilla.mozdev.org/releases/%{_realname}.xpi
Source2:	%{_realname}-installed-chrome.txt
URL:		http://jabberzilla.mozdev.org/
BuildRequires:	unzip
Requires:	mozilla >= 1.0
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_chromedir	%{_libdir}/mozilla/chrome

%description
Jabber client for Mozilla. It can integrate with sidebar or work in
separate window. It has module with conference calls support.

%description -l pl
Klient jabbera dla mozilli. Integruje siê z sidebarem lub dzia³a w
osobnym okienku. Zawiera modu³ rozmów konferencyjnych.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
mv -f $RPM_BUILD_ROOT%{_chromedir}/components $RPM_BUILD_ROOT%{_libdir}/mozilla
rm -f $RPM_BUILD_ROOT%{_chromedir}/*.{txt,js}
unzip %{SOURCE1} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_chromedir}
cat %{_realname}-installed-chrome.txt >> installed-chrome.txt

%postun
cd %{_chromedir}
cat installed-chrome.txt | grep -vE "%{_realname}"\|"jabberxm" > installed-chrome.txt.tmp
cat installed-chrome.txt.tmp > installed-chrome.txt
rm -f installed-chrome.txt.tmp

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}
%{_chromedir}/jabberxm
%{_libdir}/mozilla/components
%{_chromedir}/%{_realname}-installed-chrome.txt
