Summary:	Midi player for alsa
Summary(pl):	Odtwarzacz midi dla ALSY
Name:		pmidi
Version:	1.4.1
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://download.sourceforge.net/pmidi/%{name}-%{version}.tar.gz
URL:		http://www.parabola.demon.co.uk/alsa/pmidi.html
BuildRequires:	alsa-lib-devel
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
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%doc *.gz
%{_mandir}/man1/*
