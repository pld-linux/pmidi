Summary:	MIDI player for ALSA sequencer
Summary(pl.UTF-8):	Odtwarzacz MIDI dla sekwencera ALSA
Name:		pmidi
Version:	1.6.0
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	e81a92626dbcc1deb917e49f0737fb32
URL:		http://www.parabola.demon.co.uk/alsa/pmidi.html
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pmidi is a command line MIDI player for ALSA.  It can play to any
MIDI device that is supported by ALSA.

%description -l pl.UTF-8
pmidi jest odtwarzaczem plików MIDI dla ALSA, działającym z linii
poleceń. Może odtwarzać do każdego z urządzeń MIDI wspieranych
przez ALSA.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
