Summary:	Midi player for alsa
Summary(pl):	Odtwarzacz midi dla ALSY
Name:		pmidi
Version:	1.2.4
Release:	1
License:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://www.parabola.demon.co.uk/alsa/%{name}-%{version}.tar.gz
URL:		http://www.parabola.demon.co.uk/alsa/pmidi.html
BuildRequires:	alsa-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Midi player for alsa

%description -l pl
Program odtwarzaj±cy pliki midi poprzez drivery ALSA. U¿ycie 'pmidi -p
client:port plik.mid' Parametr client:port mo¿na uzyskaæ przez 'pmidi
-l' Przyk³ad: 'pmidi -p 65:0 impromptu.mid'

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -s %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1  $RPM_BUILD_ROOT%{_mandir}/man1/

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%doc README
%{_mandir}/man1/*
