Summary:	Midi player for alsa
Summary(pl):	Odtwarzacz midi dla ALSY
Name:		pmidi
Version:	1.5.5
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	43e97dd991c3bfc5ef019fec888d5d75
URL:		http://www.parabola.demon.co.uk/alsa/pmidi.html
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A straightforward command line program to play midi files through the
ALSA sequencer. Usage: 'pmidi -p client:port plik.mid'

%description -l pl
Program odtwarzaj±cy pliki midi poprzez drivery ALSA. U¿ycie 'pmidi -p
client:port plik.mid' Parametr client:port mo¿na uzyskaæ przez 'pmidi
- -l'. Przyk³ad: 'pmidi -p 65:0 impromptu.mid'

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--prefix=/usr

%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
