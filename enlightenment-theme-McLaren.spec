%define	_theme	McLaren
Summary:	A theme oriented for those who like dark and soft colors
Summary(pl.UTF-8):   Motyw zorientowany pod kątem osób lubiących ciemne i miękkie kolory
Name:		enlightenment-theme-%{_theme}
Version:	0.1.0
Release:	1
License:	BSD
Group:		Themes
Source0:	http://www.get-e.org/Themes/E17/_files/%{_theme}-%{version}.edj
# Source0-md5:	debde6b5b20af334daea0dea3a1124c3
URL:		http://www.get-e.org/Themes/E17/
Requires:	enlightenment >= 0.16.999
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A theme oriented for those who like dark and soft colors.

%description -l pl.UTF-8
Motyw zorientowany pod kątem osób lubiących ciemne i miękkie kolory.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/enlightenment/data/themes

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/enlightenment/data/themes/%{_theme}.edj

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/enlightenment/data/themes/%{_theme}.edj
