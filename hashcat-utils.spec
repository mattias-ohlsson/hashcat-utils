Name:           hashcat-utils
Version:        1.9
Release:        1%{?dist}
Summary:        Small utilities that are useful in advanced password cracking

License:        MIT
URL:            https://hashcat.net/wiki/doku.php?id=hashcat_utils
Source0:        https://github.com/hashcat/%{name}/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
Hashcat-utils are a set of small utilities that are useful in advanced password
cracking. They all are packed into multiple stand-alone binaries. All of these
utils are designed to execute only one specific function. Since they all work
with STDIN and STDOUT you can group them into chains.

%prep
%autosetup

%build
cd src
%make_build CFLAGS=-g

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 755 src/{*.bin,*.pl} %{buildroot}%{_datadir}/%{name}

%files
%license LICENSE
%doc README.md CHANGES
%{_datadir}/%{name}/*.bin
%{_datadir}/%{name}/*.pl

%changelog
* Wed Feb 12 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 1.9-1
- Initial build
