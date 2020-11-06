%global upstream_name beerware
%global mainid 0.0.1

# some change

Name:           beer
Version:        0.1.0
Release:        1%{?dist}
Summary:        A tool to make you happy

License:        Beerware
# random source
Source:         https://github.com/pcahyna/auto-maintenance/archive/%{mainid}.tar.gz#/auto-maintenance-%{mainid}.tar.gz
# source with the specfile
Source1:        %{upstream_name}-%{version}.tar.gz
BuildArch:      noarch

%description
...but not too happy.

%prep
%setup -qc -a1

%changelog
* Mon Feb 25 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.1.0-1
- Initial brewing
